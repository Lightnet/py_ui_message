# https://click.palletsprojects.com/en/8.1.x/commands/#decorating-commands
import click

@click.group()
def cli1():
    pass

@cli1.command('test')
def cmd1():
    """Command on cli1"""
    print("test")

@click.group()
def cli2():
    pass

@cli2.command()
def cmd2():
    """Command on cli2"""

cli = click.CommandCollection(sources=[cli1, cli2])

if __name__ == '__main__':
    cli()
    print("test")


"""import click
#from flask import cli

@click.command('init-db')
def hello():
  click.echo('Hello World!')

@click.command()
def initdb():
  click.echo('Initialized the database')

@click.command()
def dropdb():
  click.echo('Dropped the database')

cli = click.CommandCollection(sources=[hello, initdb, dropdb])

#cli.add_command(initdb)
#cli.add_command(dropdb)

if __name__ == '__main__':
  hello()
"""