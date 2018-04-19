from sqlalchemy import Column, Integer, Unicode, UniqueConstraint, ForeignKey, create_engine


CBase = declarative_base()

class CUsers(CBase):

    __tablename__ = 'users'

    uid = Column(Integer(), primary_key=True)
    login = Column(Unicode())

    check_1 = UniqueConstraint('login')