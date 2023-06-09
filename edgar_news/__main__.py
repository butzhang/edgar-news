import click
from flask.cli import FlaskGroup
import os

from . import create_app_wsgi


@click.group(cls=FlaskGroup, create_app=create_app_wsgi)
def main():
    """Management script for the edgar_news application."""

    os.environ["OPENAI_API_KEY"] = "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"


if __name__ == "__main__":  # pragma: no cover
    main()
