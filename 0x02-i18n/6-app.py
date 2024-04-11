#!/usr/bin/env python3
"""
Flask app
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel


class Config:
    """
    Configuration for Babel
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)
app.url_map.strict_slashes = False


# Mock user table
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


# Define get_user function
def get_user():
    """Return user dictionary or None if the ID cannot be found.
    """
    login_id = request.args.get('login_as')
    if login_id:
        return users.get(int(login_id))
    return None


# Define before_request function
@app.before_request
def before_request() -> None:
    """_summary_
    """

    g.user = get_user()


@babel.localeselector
def get_locale():
    """Retrieves the locale for a web page.

    Returns:
        str: best match
    """
    # Check if the 'locale' parameter is present
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale

    # Check if a user is logged in
    if g.user:
        locale = g.user.get('locale')
        if locale and locale in app.config['LANGUAGES']:
            return locale

    # ocale from request header
    locale = request.headers.get('locale', None)
    if locale in app.config['LANGUAGES']:
        return locale

    # Fall back to using the request's accepted languages
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    '''default route'''
    return render_template('6-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
