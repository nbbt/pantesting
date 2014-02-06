from pantesting.db.orm import User, Host

__author__ = 'Anya'



class PanetesterApi(object):
    """
    API fot the pantesting model.
    """
    def __init__(self, session):
        self._session = session

    def get_users(self, **kwargs):
        """
        Return all users that feet the given conditions (via kwargs).
        """
        self._session.query(User).filter(**kwargs)

    def get_hosts(self, **kwargs):
        """
        Return all hosts that feet the given conditions (via kwargs).
        """
        self._session.query(Host)(**kwargs)


