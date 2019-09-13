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
    start_response('404 Not Found', [('Content-Type', 'text/html; charset=utf-8')])

    return [str.encode("<html><body><h1>Not Found!</h1>La page demandée n'existe pas")]

def index(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])

    # Nous devons retourner des bytes, et non pas une chaine de caractère.
    # La méthode `str.encode` permet de convertir une chaine de caractère unicode en bytes.
    return [str.encode("<html><body><h1>Hello world!</h1></body></html>")]

def echo(environ, start_response):
    # TODO: Retourner un 200 OK et afficher dans le template la valeur des paramètres de l'URI :
    #
    # /echo?key_1=value_1&key_2=value_2&key_1=autre_value_1
    #
    # devrait afficher une page Web avec un tableau correspondant à
    # <table>
    #     <tbody>
    #         <tr>
    #             <td>cle_1</td>
    #             <td>value_1, autre_valeur,</td>
    #         </tr>
    #             <td>cle_2</td>
    #             <td>value_2,</td>
    #         </tr>
    #     </tbody>
    # </table>

    query_string = parse_qs(environ['QUERY_STRING'])

    body = """
        <html>
        <style>
              table, th, td {
                border: 1px solid black;
              }
        </style>
        <body>
        <h1>Echo</h1>
        <table style="border: 1 solid black">
            <tbody>"""

    for cle, valeurs in query_string.items():
        body += "<tr><td>{0}</td><td>".format(cle)
        for valeur in valeurs:
            body += "{0},".format(valeur)
        body += "</tr>"

    start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])
    return [str.encode("{0}</tbody></table></body></html>".format(body))]

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
