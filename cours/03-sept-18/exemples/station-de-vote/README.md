# Station de vote

Petite application flask largement insprié [du tutoriel officle de Flask](https://github.com/pallets/flask/tree/master/examples/tutorial).

## Installation

Les packages suivants sont nécéessaire :

```
$ pip install flask pytest pytest-flask selenium pytest-selenium
```

## Utilisation

Pour rouler l'application :

```
$ FLASK_DEBUG=True FLASK_APP=poll flask run
 * Serving Flask app "poll" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 137-450-813
```

Ensuite l'application Web sera disponible à l'adresse suivante : [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## Tests

Pour rouler les tests :

```
$ python -m pytest tests/
============================= test session starts ==============================
platform linux -- Python 3.6.8, pytest-5.1.2, py-1.8.0, pluggy-0.13.0
sensitiveurl: .*
rootdir: /home/jpcaissy/src/INF5190/cours/03-sept-18/exemples/station-de-vote
plugins: metadata-1.8.0, selenium-1.17.0, variables-1.8.0, base-url-1.4.1, html-2.0.0
collected 13 items

tests/test_browser.py s                                                  [  7%]
tests/test_functionnal.py .......                                        [ 61%]
tests/test_integration.py .                                              [ 69%]
tests/test_unit.py ....                                                  [100%]

======================== 12 passed, 1 skipped in 0.25s =========================
```

### Tests de navigateurs

Pour rouler les tests de navigateurs, il est préférable d'utiliser Ubuntu.

Pré-requis :

```
$ apt-get install firefox-geckodriver
```

Ensuite il suffit de mettre la variable d'environnement `BROWSER_TEST=1` :

```
$ BROWSER_TEST=1 python -m pytest --driver=firefox tests/
============================= test session starts ==============================
platform linux -- Python 3.6.8, pytest-5.1.2, py-1.8.0, pluggy-0.13.0
driver: firefox
sensitiveurl: .*
rootdir: /home/jpcaissy/src/INF5190/cours/03-sept-18/exemples/station-de-vote
plugins: flask-0.15.0, metadata-1.8.0, selenium-1.17.0, variables-1.8.0, base-url-1.4.1, html-2.0.0
collected 13 items

tests/test_browser.py .                                                  [  7%]
tests/test_functionnal.py .......                                        [ 61%]
tests/test_integration.py .                                              [ 69%]
tests/test_unit.py ....                                                  [100%]

============================== 13 passed in 7.03s ==============================
sys:1: ResourceWarning: unclosed <socket.socket fd=13, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=6, laddr=('127.0.0.1', 39122), raddr=('127.0.0.1', 59457)>
```
