from sqlalchemy import Column, Boolean, Integer, String, Text

from db import Base

class OfflineDeal(Base):
    __tablename__ = 'offline_deal'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    car_file_id = Column(Integer, nullable=False)
    deal_cid = Column(String(100), nullable=False)
    miner_id = Column(Integer, nullable=False)
    verified = Column(Boolean, nullable=False)
    start_epoch = Column(Integer, nullable=False)
    sender_wallet_id = Column(Integer, nullable=False)
    status = Column(String(100), nullable=False)
    deal_id = Column(Integer)
    on_chain_status = Column(String(100))
    unlock_tx_hash = Column(String(100))
    unlock_at = Column(Integer)
    create_at = Column(Integer, nullable=False)
    update_at = Column(Integer, nullable=False)
    note = Column(Text)