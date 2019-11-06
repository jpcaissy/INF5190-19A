from flask import escape

def index(polls):
    view = """
<html>
    <body>
        <h1>Sondages</h1>
        <table>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Nom</th>
                </tr>
            </thead>
            <tbody>
    """

    if polls:
        for poll in polls:
            view += """
                    <tr>
                        <td>{id}</td>
                        <td><a href="/polls/{id}">{name}</a></td>
                    </tr>
            """.format(id=poll.id, name=poll.name)

    return view + """</tbody></table><hr /><a id="new-poll" href="/polls/new">Nouveau sondage</a></body></html>"""

def index_empty():
    return """
<html>
    <body>
        <h1>Sondages</h1>
        <h2>Aucuns sondages actifs</h2>

        <a id="new-poll" href="/polls/new">Nouveau sondage</a>
    </body>
</html>
    """

def new_poll(poll):
    view = """
<html>
    <body>
        <h1>Sondages</h1>
        <h2>Nouveau</h2>

        <form method="POST">
            <label for="name">Nom : </label><input type="text" name="name" /><br />
            <button type="submit">Créer</button>
        </form>
    </body>
</html>
    """

    return view

def view_poll(poll):
    view = """
<html>
    <body>
        <h1>Sondages</h1>
        <h2>{name}</h2>
        <p>{total_votes} vote(s) au total</p>
    """.format(name=escape(poll.name), total_votes=poll.number_of_votes())

    if poll.choices.count():
        view += """<form method="POST" action="/polls/{poll_id}/vote">""".format(poll_id=poll.id)
        for choice in poll.choices.select():
            view += """
            <label for="choice-{id}">{choice} (<strong>{votes} vote(s)</strong>): </label>
            <input type="radio" name="choice_id" id="choice-{id}" value="{id}" />
            <br />
            """.format(id=choice.id, choice=choice.choice, votes=choice.number_of_votes())
        view += """<button type="submit">Soumettre le vote</button></form>"""
    else:
        view += "Il n'y a aucun choix de disponible.<br />"

    view += """
    <hr />
    <form method="POST" action="/polls/{poll_id}/choices/new">
        <p>Rajouter un choix au sondage : </p>
        <label for="choice">Choix : </label><input type="text" id="choice" name="choice" /><br />
        <button type="submit" id="add-choice">Rajouter</button>
    </form>""".format(poll_id=poll.id)

    return view + """<hr /><a href="/">Retourner à la liste des sondages</a></body></html>"""
