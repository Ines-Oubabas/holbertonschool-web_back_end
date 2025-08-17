#!/usr/bin/env python3
"""Flask app with gettext-parametrized templates - task 3."""
from typing import Any, List
from flask import Flask, render_template, request
from flask_babel import Babel, gettext as _


class Config:
    """Babel/Flask configuration."""
    LANGUAGES: List[str] = ["en", "fr"]
    BABEL_DEFAULT_LOCALE: str = "en"
    BABEL_DEFAULT_TIMEZONE: str = "UTC"


app: Flask = Flask(__name__)
app.config.from_object(Config)

babel: Babel = Babel()


def get_locale() -> str:
    """Use Accept-Language to find a best match."""
    best = request.accept_languages.best_match(app.config["LANGUAGES"])
    return best or app.config["BABEL_DEFAULT_LOCALE"]


babel.init_app(app, locale_selector=get_locale)


@app.route("/", strict_slashes=False)
def index() -> Any:
    """Render the parametrized home page."""
    # Values will be resolved via translations
    return render_template("3-index.html")


if __name__ == "__main__":
    app.run()
