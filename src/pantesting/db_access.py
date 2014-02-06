import json
from flask import Blueprint, jsonify, request
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

@db_access.route('/new_host', methods=['POST'])
def new_host():
    request_dict = json.loads(request.data)
    user = api.get_users(id=request_dict["userId"])[0]
    host = user.add_host(name=request_dict["hostName"], description=request_dict["description"], url=request_dict["url"])
    for bounty in request_dict["bounties"]:
        host.add_bounty(type_=bounty["type"], amount=int(bounty["amount"]))
    api.commit()
    return ""


@db_access.route("/remove_host/<host_id>", methods=["DELETE"])
def remove_host(host_id):
    pass






@db_access.route('/example', methods=['GET', 'POST'])
def example():
    return 'foo'

