from app import create_application
from flask_script import Manager, Server

app = create_application('development')

manager = Manager(app)
manager.add_command('server', Server)
@manager.add_command
def test():
    '''
    This function will run the unit tests
    '''
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)

if __name__ == '__main__':
    manager.run()