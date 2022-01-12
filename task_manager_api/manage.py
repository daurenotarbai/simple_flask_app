import click
from flask.cli import with_appcontext


@click.group()
def cli():
    """Main entry point"""


@cli.command("init")
@with_appcontext
def init():
    """Create a new admin user"""
    from task_manager_api.extensions import db
    from task_manager_api.models import User

    click.echo("create user")
    user = User(username="Aydardev", email="admin@qazna.com", password="admin123", active=True)
    db.session.add(user)
    db.session.commit()
    click.echo("created user admin")


if __name__ == "__main__":
    cli()
