import json
from urllib.error import HTTPError
from urllib.request import Request, urlopen

BASE_URL = "http://localhost:5000"


class ApiError(Exception):
    pass


def perform_request(uri, method="GET", data=None):
    request = Request('http://localhost:5000/{0}'.format(uri))
    request.method = method
    request.add_header("content-type", "application/json")

    if data:
        request.data = json.dumps(data).encode('utf-8')

    try:
        with urlopen(request) as response:
            data = response.read()
            headers = response.headers

            if headers['content-type'] == "application/json":
                 return json.loads(data)
            else:
                return None
    except HTTPError as e:
        code = e.code
        headers = e.headers
        data = e.read()

        error = ApiError()
        error.code = code
        if headers['content-type'] == "application/json":
            error.content = json.loads(data)

        raise error


def get_accounts():
    return perform_request("accounts")

def get_account(account_id):
    assert isinstance(account_id, int)

    try:
        return perform_request("accounts/{0}".format(account_id))
    except ApiError as e:
        if e.code == 404:
            return None
        else:
            raise

def get_transactions(account_id):
    assert isinstance(account_id, int)
    return perform_request("accounts/{0}/transactions".format(account_id))

def get_transaction(account_id, transaction_id):
    assert isinstance(account_id, int)
    assert isinstance(transaction_id, int)

    return perform_request("accounts/{0}/transactions/{1}".format(account_id, transaction_id))

def create_account(owner, balance):
    assert balance >= 0

    return perform_request("accounts", "POST", {
        "account": { "owner": owner, "current_balance": balance }
    })

def create_transaction(from_account_id, to_account_id, amount):
    assert isinstance(from_account_id, int)
    assert isinstance(to_account_id, int)
    assert amount >= 0

    try:
        return perform_request("transactions", "POST", {
            "transaction": { "from_account": from_account_id, "to_account": to_account_id, "amount": amount }
        })
    except ApiError as e:
        if e.code == 422:
            if e.content['error']['code'] == "insuffisant-funds":
                print("Les fonds ne sont pas suffisant")

            if e.content['error']['code'] == "account-not-found":
                print("Le compte n'existe pas")

            return None
        else:
            raise
