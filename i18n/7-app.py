#!/usr/bin/env python3
"""
Flask app: locale + timezone selection with Flask-Babel.

Priority rules:
- Locale: URL (?locale) > user setting > Accept-Language > default
- Timezone: URL (?timezone) > user setting > default ("UTC")
"""
from typing import Any, Dict, Optional, List
from flask import Flask, render_template, request, g
from flask_babel import Babel
import pytz
from pytz.exceptions import UnknownTimeZoneError


class Config:
    """
    App config for Flask-Babel.

    Attributes:
        LANGUAGES (list[str]): Supported locales.
        BABEL_DEFAULT_LOCALE (str): Fallback locale.
        BABEL_DEFAULT_TIMEZONE (str): Default timezone ("UTC").
    """
    LANGUAGES: List[str] = ["en", "fr"]
    BABEL_DEFAULT_LOCALE: str = "en"
    BABEL_DEFAULT_TIMEZONE: str = "UTC"


# Mock users database
users: Dict[int, Dict[str, Optional[str]]] = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

app: Flask = Flask(__name__)
app.config.from_object(Config)

babel: Babel = Babel()


def get_user() -> Optional[Dict[str, Optional[str]]]:
    """Return mocked user dict from ?login_as=<id>, else None."""
    uid = request.args.get("login_as", type=int)
    return users.get(uid) if uid in users else None


@app.before_request
def before_request() -> None:
    """Attach current user to flask.g for this request."""
    g.user = get_user()


def get_locale() -> str:
    """
    Locale selector with priority:
    URL param -> user setting -> Accept-Language -> default.
    """
    # 1) URL param
    forced = request.args.get("locale", type=str)
    if forced in app.config["LANGUAGES"]:
        return forced

    # 2) User setting
    user = getattr(g, "user", None)
    if user:
        uloc = user.get("locale")
        if uloc in app.config["LANGUAGES"]:
            return str(uloc)

    # 3) Accept-Language header
    match = request.accept_languages.best_match(app.config["LANGUAGES"])
    if match:
        return match

    # 4) Default
    return app.config["BABEL_DEFAULT_LOCALE"]


def get_timezone() -> str:
    """
    Timezone selector with priority:
    URL param -> user setting -> default ("UTC").

    Validates provided timezones using pytz.timezone.
    """
    # 1) URL param
    tz = request.args.get("timezone", type=str)
    if tz:
        try:
            pytz.timezone(tz)
            return tz
        except UnknownTimeZoneError:
            pass  # ignore invalid URL-provided timezone

    # 2) User setting
    user = getattr(g, "user", None)
    if user:
        utz = user.get("timezone")
        if isinstance(utz, str):
            try:
                pytz.timezone(utz)
                return utz
            except UnknownTimeZoneError:
                pass  # ignore invalid user timezone

    # 3) Default
    return app.config["BABEL_DEFAULT_TIMEZONE"]


# Bind Babel with our selectors
babel.init_app(
    app,
    locale_selector=get_locale,
    timezone_selector=get_timezone,
)


@app.route("/", strict_slashes=False)
def index() -> Any:
    """Render translated home page for step 7."""
    return render_template("7-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
