from sqlalchemy import Column, Boolean, Integer, String, Text

from db import Base

class Wallet(Base):
    __tablename__ = 'wallet'

    id = Column(Integer,primary_key=True, autoincrement=True, nullable=False)
    type = Column(Integer, nullable=False)
    address = Column(String(100), nullable=False)
    create_at = Column(Integer, nullable=False)
    is_dao = Column(Boolean)
    update_at = Column(Integer, nullable=False)
    nonce = Column(String(45))