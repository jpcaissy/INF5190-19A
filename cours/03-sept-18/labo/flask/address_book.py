import json
from flask import Flask

app = Flask(__name__)

FILENAME = "./data.json"

class AddressBook(object):
    @classmethod
    def load_from_file(cls, filename):
        addresses = []

        with open(filename) as f:
            data = json.load(f)
            for i, address in enumerate(data):
                addresses.append(
                    Address(
                        id=i,
                        name=address['name'],
                        address=address['address'],
                        phone_numbers=address['phone'],
                        email=address['email']
                    )
                )

        return AddressBook(addresses)

    def __init__(self, addresses):
        self.addresses = addresses

    def get_address(self, id):
        return self.addresses[id]

class Address(object):
    def __init__(self, id, name, address, email, phone_numbers):
        self.id = id
        self.name = name
        self.address = address
        self.phone_numbers = phone_numbers
        self.email = email


@app.route('/')
def index():
    view = """
    <html>
    <body>
        <h1>Carnet d'aresse</h1>
        <ul>
    """

    address_book = AddressBook.load_from_file(FILENAME)
    for address in address_book.addresses:
        view += """
            <li>
                <a href="/{id}">{name}</a>
            </li>""".format(id=address.id, name=address.name)

    return view + "</ul></body></html?"

@app.route('/<int:id>')
def address(id):
    address_book = AddressBook.load_from_file(FILENAME)
    address = address_book.get_address(id)

    return ""
