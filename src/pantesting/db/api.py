import os
from pantesting.db.orm import User, Host, connect, Bounty, Exploit

__author__ = 'Anya'


class PanetesterApi(object):
    """
    API fot the pantesting model.
    """
    def __init__(self, path="db.db"):
        self._session = connect(path)

    def get_users(self, **kwargs):
        """
        Return all users that feet the given conditions (via kwargs).
        """
        return self._session.query(User).filter_by(**kwargs).all()

    def get_hosts(self, **kwargs):
        """
        Return all hosts that feet the given conditions (via kwargs).
        """
        return self._session.query(Host).filter_by(**kwargs).all()

    def get_bounties(self, **kwargs):
        return self._session.query(Bounty).filter_by(**kwargs).all()

    def get_exploits(self, **kwargs):
        return self._session.query(Exploit).filter_by(**kwargs).all()

    def add_user(self, name, password, company_name):
        user = User(name=name, password=password, company_name=company_name)
        self._session.add(user)
        self._session.commit()
        return user

    def commit(self):
        self._session.commit()

    def remove(self, obj):
        self._session.delete(obj)