from flask import Blueprint

__author__ = 'newt'

db_access = Blueprint('db_access', __name__)

@db_access.route('/example', methods=['GET', 'POST'])
def example():
    return 'foo'