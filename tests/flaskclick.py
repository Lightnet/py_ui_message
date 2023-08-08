# note you need to run cmd
# flask namefile.py --help # works
# py namefile.py --help # note it will not work

import click
from flask import Flask

app = Flask(__name__)

@app.cli.command("createuser")
@click.argument("name")
def create_user(name):
    print("Name", name)
    pass

@app.cli.command("init-db")
def init_db():
    print("init db")
    pass


app.cli.add_command(create_user)

if __name__ == '__main__':
    app.run()
    print("cmd test...")