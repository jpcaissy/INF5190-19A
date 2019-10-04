import json
import datetime

import click
from flask import Flask, jsonify, request, abort, redirect, url_for
import peewee as p
from playhouse.shortcuts import model_to_dict, dict_to_model

app = Flask(__name__)

db = p.SqliteDatabase("db.sqlite")

class BaseModel(p.Model):
    class Meta:
        database = db


class Account(BaseModel):
    id = p.AutoField(primary_key=True)
    owner = p.CharField(unique=True, null=False)
    current_balance = p.IntegerField(default=0, constraints=[
        p.Check('current_balance >= 0')
    ])


class Transaction(BaseModel):
    id = p.AutoField(primary_key=True)
    from_account = p.ForeignKeyField(Account, backref="transactions_from", null=False)
    to_account = p.ForeignKeyField(Account, backref="transactions_to", null=False)
    timestamp = p.DateTimeField(default=datetime.datetime.now)
    amount = p.IntegerField(constraints=[
        p.Check('amount > 0')
    ])


@app.route('/accounts', methods=['GET'])
def accounts():
    accounts = []
    for account in Account.select():
        accounts.append(model_to_dict(account))

    return jsonify(accounts)


@app.route('/accounts/<int:id>', methods=['GET'])
def accounts_get(id):
    account = Account.get_or_none(id)
    if account is None:
        return abort(404)

    return jsonify(model_to_dict(account))


@app.route('/accounts/<int:id>/transactions', methods=['GET'])
def accounts_transactions(id):
    account = Account.get_or_none(id)
    if account is None:
        return abort(404)

    transactions = []
    for transaction in account.transactions_from:
        transactions.append(model_to_dict(transaction))

    for transaction in account.transactions_to:
        transactions.append(model_to_dict(transaction))

    return jsonify(transactions)


@app.route('/accounts/<int:id>/transactions/<int:transaction_id>', methods=['GET'])
def accounts_transactions_get(id, transaction_id):
    transaction = Transaction.get_or_none(Transaction.id == transaction_id)
    if transaction is None:
        return abort(404)

    if transaction.to_account.id == id or transaction.from_account.id == id:
        return jsonify((model_to_dict(transaction)))

    return abort(404)


@app.route('/accounts', methods=['POST'])
def accounts_create():
    if not request.is_json:
        return abort(400)

    json_payload = request.json['account']
    json_payload['id'] = None

    new_account = dict_to_model(Account, json_payload)

    try:
        new_account.save()
    except p.IntegrityError:
        return jsonify({
            "error": "Un compte avec le même propriétaire existe déjà"
        }), 422

    return redirect(url_for("accounts_get", id=new_account.id))


@app.route('/transactions', methods=['POST'])
def transactions_create():
    if not request.is_json:
        return abort(400)

    json_payload = request.json['transaction']
    json_payload['id'] = None

    new_transaction = dict_to_model(Transaction, json_payload)
    with db.atomic() as transaction:
        try:
            new_transaction.save()

            Account.update(
                current_balance = Account.current_balance - new_transaction.amount
            ).where(Account.id == new_transaction.from_account.id).execute()

            Account.update(
                current_balance = Account.current_balance + new_transaction.amount
            ).where(Account.id == new_transaction.to_account.id).execute()

            transaction.commit()
        except Account.DoesNotExist:
            transaction.rollback()

            return jsonify({
                "error": {
                    "code": "account-not-found",
                    "text": "Un des comptes n'existe pas"
                }
            }), 422
        except p.IntegrityError:
            return jsonify({
                "error": {
                    "code": "insuffisant-funds",
                    "error": "Fonds insuffisants",
                }
            }), 422
        except:
            transaction.rollback()
            return abort(400)

    return redirect(url_for("transactions_get", id=new_transaction.id))


@app.route('/transactions/<int:id>', methods=['GET'])
def transactions_get(id):
    transaction = Transaction.get_or_none(id)
    if transaction is None:
        return abort(404)

    return jsonify(model_to_dict(transaction))


@app.cli.command("init-db")
def init_db():
    db.create_tables([Account, Transaction])
