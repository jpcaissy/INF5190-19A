from datetime import datetime
from http.cookies import SimpleCookie

cache = {}

def get_session_from_cookie(cookies_value):
    cookies = SimpleCookie()
    cookies.load(cookies_value)
    if 'session' in cookies:
        session = cookies['session']
        return session.value

    return None

def mon_application(env, start_response):
    cookies = env.get('HTTP_COOKIE', "")
    session_id = get_session_from_cookie(cookies)

    if session_id not in cache:
        cache[session_id] = 1
    else:
        cache[session_id] += 1

    start_response('200 OK', [('Content-Type','text/plain')])
    return [
                str.encode(
                    "Hello World!\n" \
                    "Session : {0}\n" \
                    "Nombre de visite(s) : {1}\n".format(
                        session_id, cache[session_id]
                    )
                )
            ]
