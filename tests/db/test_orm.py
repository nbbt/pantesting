from pantesting.db.orm import connect, User, Host, Bounty

__author__ = 'Anya'


def test_orm():
    """
    Check the the orm basically works.
    """
    session = connect()
    user_details = {"name": "foo", "password": "bar", "company_name": "foobar"}
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