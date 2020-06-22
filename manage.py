import click
from flask.cli import FlaskGroup

from onesixeight.app import create_app


def create_onesixeight(info):
    return create_app(cli=True)


@click.group(cls=FlaskGroup, create_app=create_onesixeight)
def cli():
    """Main entry point"""


@cli.command("init")
def init():
    """Create a new admin user
    """
    from onesixeight.extensions import db
    from onesixeight.models import User

    click.echo("create user")
    user = User(username="admin", email="brian@localhost", password="fishface", active=True)
    db.session.add(user)
    db.session.commit()
    click.echo("created user admin")


if __name__ == "__main__":
    cli()
