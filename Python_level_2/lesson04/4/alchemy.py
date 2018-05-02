
from sqlalchemy import Column, Integer, Unicode, UniqueConstraint, ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

CBase = declarative_base()

class CUsers(CBase):

    __tablename__ = "users"

    uid = Column(Integer(), primary_key = True)
    login = Column(Unicode())

    check_1 = UniqueConstraint("login")

    def __repr__(self):

        return "CUsers<uid = %d, login = %s>" % (self.uid, self.login)

class CMessages(CBase):

    __tablename__ = "messages"

    mid = Column(Integer(), primary_key = True)
    user_from = Column(Integer(), ForeignKey("users.uid"))
    user_to = Column(Integer(), ForeignKey("users.uid"))
    message = Column(Unicode())

    p_user_from = relationship("CUsers", foreign_keys = [ user_from ])
    p_user_to = relationship("CUsers", foreign_keys = [ user_to ])

    def __repr__(self):

        return "CMessages<mid = %d, user_from = %d, user_to = %d, message = %s>" % (self.mid, self.user_from, self.user_to, self.message)

#########################################################

engine = create_engine("sqlite:///messages.db")
session = sessionmaker(bind = engine)()

"""
msg = CMessages(user_from = 2, user_to = 2, message = "Hello from 2 to 2")
session.add(msg)
session.commit()

msgs = session.query(CMessages).filter_by(user_from = 2).all()

for msg in msgs[ : 2]:

    print(msg)

    msg.message += "FROM UPDATE"

session.commit()
"""

msgs = session.query(CMessages).filter_by(user_from = 1).limit(2).all()

for msg in msgs:

    print(msg)

