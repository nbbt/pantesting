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

@db_access.route('/get_hosts_by_user/<user_id>')
def get_hosts_by_user(user_id):
    hosts = api.get_hosts(id=user_id)
    return jsonify({'hosts': [host.to_dict() for host in hosts]})

@db_access.route('/get_submitted_exploits/<user_id>')
def get_submitted_exploits(user_id):
    bounties = sum([host.bounties for host in api.get_hosts(id=user_id)], [])
    exploits = []
    for bounty in bounties:
        exploits += list(bounty.exploits)
    return jsonify({'exploits': [exploit.to_dict() for exploit in exploits]})


@db_access.route('/get_bounties/<host_id>')
def get_bounties(host_id):
    return jsonify({'bounties': [b.to_dict() for b in api.get_bounties(host_id=host_id)]})


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
    host = api.get_hosts(id=host_id)[0]
    api.remove(host)
    api.commit()
    return ""

@db_access.route("/submit_exploit", methods=["POST"])
def add_exploit():
    request_dict = json.loads(request.data)
    bounty = api.get_bounties(id=request_dict["bountyId"])[0]
    exploit = bounty.add_exploit(user_id=request_dict["userId"], description=request_dict["description"])
    api.commit()
    return ""

@db_access.route("/add_bounty", methods=["POST"])
def add_bounty():
    request_dict = json.loads(request.data)
    host = api.get_hosts(id=request_dict["hostId"])[0]
    bounty = host.add_bounty(type_=request_dict["type"], amount=request_dict["amount"])
    api.commit()
    return ""

@db_access.route("/approve_exploit/<exploit_id>", methods=["PUT"])
def approve_exploit():
    pass


@db_access.route('/example', methods=['GET', 'POST'])
def example():
    return 'foo'

