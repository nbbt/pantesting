import os
from pantesting.db.orm import User, Host, connect

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
        return self._session.query(User).filter(**kwargs).all()

    def get_hosts(self, **kwargs):
        """
        Return all hosts that feet the given conditions (via kwargs).
        """
        return self._session.query(Host).filter(**kwargs).all()

    def add_user(self, name, password, company_name):
        user = User(name=name, password=password, company_name=company_name)
        self._session.add(user)
        self._session.commit()

    def commit(self):
        self._session.commit()