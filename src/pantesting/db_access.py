from flask import Blueprint, jsonify
from pantesting.db.api import PanetesterApi

__author__ = 'newt'

db_access = Blueprint('db_access', __name__)
api = PanetesterApi()

@db_access.route('/get_hosts/<host_id>')
def get_hosts(host_id):
    if host_id == 'all':
        hosts = api.get_hosts()
    else:
        hosts = api.get_hosts(id=host_id)
    return jsonify({'all': [host.to_dict() for host in hosts]})

@db_access.route('/example', methods=['GET', 'POST'])
def example():
    return 'foo'

