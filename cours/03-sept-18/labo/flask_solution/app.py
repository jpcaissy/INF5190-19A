import json
from flask import Flask, url_for, redirect, request, abort

app = Flask(__name__)
app.debug = True

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
        try:
            return self.addresses[id]
        except IndexError:
            return None

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

    return view + """
        </ul>
    <br /><a href="{0}">Rajouter une adresse</a>
    </body></html>""".format(url_for("new_address"))

@app.route('/<int:id>')
def address(id):
    address_book = AddressBook.load_from_file(FILENAME)
    address = address_book.get_address(id)
    if(address == None):
        return abort(404)
    else:
        view =   """
        <html>
        <body>
            <ul>
        """
        view += f"""
            <li>
               {address.name}
            </li>
            <li>
               {address.address}
            </li>
            <li>
               {address.phone_numbers}
            </li>
            <li>
               {address.email}
            </li>
            """
        return view + """
            </ul>
        </body></html>"""

@app.route('/new', methods=['GET'])
def new_address():
    return """
    <html>
    <body>
        <h1>Carnet d'aresse</h1>
        <form method="POST">
            <label for="name">Nom : </label><input type="text" name="name" /><br />
            <label for="name">Adresse : </label><input type="text" name="address" /><br />
            <label for="name">Téléphone : </label><input type="text" name="telephone" /><br />
            <label for="name">Email : </label><input type="text" name="email" /><br />
            <button type="submit">Créer</button>
        </form>
    </body>
    </html>
    """

@app.route('/new', methods=['POST'])
def create_address():
    name = request.values.get('name')
    adress = request.values.get('address')
    phone = request.values.get('telephone')
    email = request.values.get('email')
    with open(FILENAME) as f:
        data = json.load(f)
    return redirect(url_for("index"))
