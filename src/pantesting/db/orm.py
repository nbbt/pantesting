from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy import create_engine

__author__ = 'Anya'


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()


class Dictable(object):
    """
    Mixinm, adds to_dict method to the class.
    """
    def to_dict(self):
        dct = self.__dict__
        for key, value in dct.items():
            if key[:2] == "__":
                dct.pop(key)
            if self._is_complex_object(value):
                dct[key] = value.to_dict()
        return dct

    def _is_complex_object(self, obj):
        return not (isinstance(obj, int) or isinstance(obj, str))


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    password = Column(String)
    company_name = Column(String)

    def __repr__(self):
        return "<User(name='%s', company_name='%s', password='%s')>" % (
            self.name, self.company_name, self.password)


class Host(Base, Dictable):
    __tablename__ = "hosts"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    url = Column(String)
    user = ForeignKey("users.user_id")
    bounties = relationship("Bounty", backref="hosts")

    def add_bounty(self, type_, amount):
        self.bounties.append(Bounty(type=type_, amount=amount, host_id=self.id, status=Bounty.ACTIVE))

    def to_dict(self):
        pass


class Bounty(Base, Dictable):
    __tablename__ = 'bounties'

    #Types
    CODE_EXEC = "code exec"
    READ = "read file"
    XSS = "XSS"

    #Statusses
    ACTIVE = "active"
    APPLIED = "applied"
    EXPIRED = "expired"

    id = Column(Integer, primary_key=True)
    type = Column(String)
    host_id = Column(Integer, ForeignKey('hosts.id'))
    amount = Column(Integer)
    status = Column(String)
    exploits = relationship("Exploit", backref="bounties")

    def add_exploit(self, user_id, description):
        """
        Add exploit. Make sure thr bounty is active before calling this method!
        """
        self.status = Bounty.APPLIED
        self.exploits.append(Exploit(bounty=self, status=Exploit.OPEN, user_id=user_id, description=description))


class Exploit(Base, Dictable):
    __tablename__ = "exploits"

    #Statussesh
    OPEN = "open"
    CONFIRMED = "confirmed"
    REJECTED = "rejected"

    id = Column(Integer, primary_key=True)
    bounty = Column(Integer, ForeignKey('bounties.id'))
    status = Column(String)
    description = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))


def connect(db_path=":memory:", echo=False):
    """
    Connect to the db.
    :param db_path: path to create the sqlite file in.`
    :type: str
    :param echo: to print log messages pass True.
    :type echo:bool
    :return: The session object
    """
    engine = create_engine("sqlite:///" + db_path, echo=echo)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session
