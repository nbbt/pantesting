from pantesting.db.orm import User

__author__ = 'Anya'



class PanetesterApi(object):
    def __init__(self, session):
        self._session = session

    def add_user(self, name, password, company_name):
        user = User(name=name, password=password, company_name=company_name)
        self._session.add(user)


