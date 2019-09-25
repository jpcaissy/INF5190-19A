import pytest

from app import app, AddressBook, Address

FILENAME = "./static_data.json"

class TestAddressBook(object):
    def test_get_address(self):
        address = Address(
            id=0,
            name="Toto",
            address="Tata",
            email="john@example.com",
            phone_numbers=["555 555-5555"]
        )

        book = AddressBook([address])
        a = book.get_address(0)

        assert a.id == 0
        assert a.name == "Toto"
        assert a.address == "Tata"
        assert a.email == "john@example.com"
        assert a.phone_numbers == ["555 555-5555"]


    def test_load_from_file(self):
        address_book = AddressBook.load_from_file(FILENAME)
        assert len(address_book.addresses) == 3

class TestApp(object):
    def test_index(self):
        client = app.test_client()
        response = client.get("/")
        assert response.status_code == 200
        assert b"Gaston Lagaffe" in response.data
        assert b"Tintin" in response.data
        assert b"Lucky Luke" in response.data

    def test_address(self):
        client = app.test_client()

        response = client.get("/0")
        assert response.status_code == 200
        assert b"Gaston Lagaffe" in response.data

    def test_address_does_not_exist(self):
        client = app.test_client()

        response = client.get("/999")
        assert response.status_code == 404

    def test_new_address(self):
        client = app.test_client()

        response = client.get("/new")
        assert response.status_code == 200
