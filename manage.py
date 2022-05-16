from app import create_app ,db
from flask_script import Manager,Server
from  flask_migrate import Migrate, MigrateCommand
from app.models import *
# from flask_admin import Admin
# from flask_admin.contrib.sqla import ModelView
# Creating app instance
app = create_app('development')
# app = create_app('test')
# app = create_app('production')

manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('server',Server)
manager.add_command('db',MigrateCommand)
# admin = Admin(app)
# admin.add_view(ModelView(User, db.session)) 
# admin.add_view(ModelView(Blog, db.session))
# admin.add_view(ModelView(Comment, db.session)) 
 


@manager.shell
def make_shell_context():
    return dict(app = app, db = db)

if __name__ == '__main__':
    manager.run()
