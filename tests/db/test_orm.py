from pantesting.db.orm import connect, User, Host, Bounty, Exploit
import pytest
__author__ = 'Anya'


def test_orm():
    """
    Check the the orm basically works.
    TODO: Split this test into real unit tests.
    """
    session = connect()
    user_details = {"name": "foo", "password": "bar", "company_name": "foobar", "uid": "12345"}
    user = User(**user_details)
    host_details = {"name": "facebook", "url": "http://www.facebook.com", "user": user.id, "bounties": []}
    host = Host(**host_details)


    bounty_details = [{"type": Bounty.CODE_EXEC, "amount": 10},
                      {"type": Bounty.XSS, "amount": 20},
                      {"type": Bounty.READ, "amount": 30}]

    for details in bounty_details:
        host.add_bounty(type_=details["type"], amount=details["amount"])

    session.add(user)
    session.add(host)

    session.commit()

    user_from_db = session.query(User).filter(User.name == user_details["name"]).first()
    host_from_db = session.query(Host).filter(Host.name == host_details["name"]).first()
    bounties_from_db = session.query(Bounty).filter().all()


    assert user_from_db.company_name == user_details["company_name"]
    assert host_from_db.url == host_details["url"]
    assert len(bounties_from_db) == 3

    for bounty in bounties_from_db:
        assert bounty.host_id == host_from_db.id

    bounty = bounties_from_db[0]
    exploit_details = {"user_id": user.id, "description": "An exlpoint"}
    bounty.add_exploit(**exploit_details)
    session.commit()

    exploit_from_db = session.query(Exploit).first()
    assert exploit_from_db.id == user.id


def test_add_host():
    session = connect()
    user = User(name="Mat", password="123", company_name="PayPal", uid="123")
    url = "http://www.google.com"
    user.add_host("host_name", "bla bla", "http://www.google.com")
    session.add(user)
    session.commit()
    host = session.query(Host).first()
    assert host.user_id == user.id
    assert host.url == host.url


def test_add_user_with_email():
    session = connect()
    email = "matt@gmail.com"
    user = User(name="Matt", email=email, password="123", company_name="PayPal", uid="123")
    session.add(user)
    session.commit()
    user = session.query(User).first()
    assert user.email == email

