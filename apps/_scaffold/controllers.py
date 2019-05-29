"""
This file defines actions, i.e. functions the URLs are mapped into
The @action(path) decorator exposed the function at URL:

    http://127.0.0.1:8000/{app_name}/{path}

If app_name == '_default' then simply

    http://127.0.0.1:8000/{path}

If path == 'index' it can be omitted:

    http://127.0.0.1:8000/

The path follows the bottlepy syntax.

@action.uses('generic.html')  indicates that the action uses the generic.html template
@action.uses(session)         indicates that the action uses the session
@action.uses(db)              indicates that the action uses the db
@action.uses(T)               indicates that the action uses the i18n & pluralization
@action.uses(auth.user)       indicates that the action requires a logged in user
@action.uses(auth)            indicates that the action requires the auth object

session, db, T, auth, and tempates are examples of Fixtures.
Warning: Fixtures MUST be declared with @action.uses({fixtures}) else your app will result in undefined behavior
"""

from web3py import action, request, abort, redirect, URL
from yatl.helpers import A
from . common import db, session, T, cache, auth

# define your actions below, here is an example of /<app_name>/index

@action('index', method='GET')
@action.uses('generic.html', session, db, T, auth)
def index():
    message = A('Click me', _class='button', _href=URL('welcome'))
    return dict(message=message, user=auth.get_user())

@action('welcome', method='GET')
@action.uses('generic.html', session, db, T, auth.user)
def index2():
    user = auth.get_user()
    message = T('Hello {first_name}'.format(**user))
    return dict(message=message, user=user)