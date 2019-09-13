from urllib.parse import parse_qs
# parse_qs
#
# https://docs.python.org/3/library/urllib.parse.html#urllib.parse.parse_qs
#
# Méthode qui prend en paramètre les query strings envoyé par la requête web et retourne un dictionnaire.
# Par exemple :
#
# key_1=value_1&key_2=value_2&key_1=autre_value_1
#
# va retourner
#
# {'key_1': ['value_1', 'autre_value_1'], 'key_2': ['value_2']}


def not_found(environ, start_response):
    # TODO : Retourner un status HTTP 404 Not Found avec une réponse HTML indiquant que la ressource n'existe pas
    return

def index(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])

    # Nous devons retourner des bytes, et non pas une chaine de caractère.
    # La méthode `str.encode` permet de convertir une chaine de caractère unicode en bytes.
    return [str.encode("<html><body><h1>Hello world!</h1></body></html>")]

def echo(environ, start_response):
    # TODO: Retourner un 200 OK et afficher dans le template la valeur des paramètres de l'URI :
    #
    # /echo?cle_1=valeur_1&cle_2=valeur_2
    #
    # devrait afficher une page Web avec un tableau correspondant à
    # <table>
    #     <tbody>
    #         <tr>
    #             <td>cle_1</td>
    #             <td>valeur_1</td>
    #         </tr>
    #             <td>cle_2</td>
    #             <td>valeur_2</td>
    #         </tr>
    #     </tbody>
    # </table>

    query_string = parse_qs(environ['QUERY_STRING'])

    return

def application(environ, start_response):
    # environ['PATH_INFO'] contient le URI de la requête Web
    path = environ['PATH_INFO']

    if path == '/':
        return index(environ, start_response)
    elif path.startswith('/echo'):
        # On utilise la méthode startswith puisqu'on va avoir des paramètre à la requête.
        return echo(environ, start_response)

    return not_found(environ, start_response)


if __name__ == "__main__":
    import waitress
    waitress.serve(application, port=8080)

