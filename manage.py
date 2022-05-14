from flask import Flask
from app import create_app
from flask_script import Manager,Server

# Creating app instance
app = create_app('development')
# app = create_app('test')
# app = create_app('production')

manager = Manager(app)
manager.add_command('server',Server)


@manager.shell
def make_shell_context():
    return dict(app = app)

if __name__ == '__main__':
    manager.run()
