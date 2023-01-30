from sqlalchemy import Column, Integer, String

from db import Base

class Miner(Base):
    __tablename__ = 'miner'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    fid = Column(String(100))
    create_at = Column(Integer)