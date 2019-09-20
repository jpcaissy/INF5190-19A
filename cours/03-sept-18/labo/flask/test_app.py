import pytest

from address_book import app, AddressBook, Address

class TestAddressBook(object):
    def test_load_from_file(self):
        pass

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
        #TODO : test qui assure que le fichier JSON est lu et que la classe est instanciée
        pass

class TestApp(object):
    def test_index(self):
        #TODO : rajouter un test qui assure que l'index retourne un 200 avec le nom des personnes du carnet d'adresse
        pass

    def test_address(self):
        client = app.test_client()

        response = client.get("/0")
        assert response.status_code == 200
        assert b"Gaston Lagaffe" in response.data

    def test_address_does_not_exist(self):
        client = app.test_client()

        response = client.get("/999")
        assert response.status_code == 404
