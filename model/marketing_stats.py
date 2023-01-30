from sqlalchemy import Column, Integer, String, Boolean

from db import Base

class MarketingStats(Base):
    __tablename__ = 'marketing_stats'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    updated_at = Column(Integer, nullable=False)
    miner_count = Column(Integer, nullable=False)
    wallet_count = Column(Integer, nullable=False)
    source_file_cids = Column(Integer, nullable=False)
    user_uploads = Column(Integer, nullable=False)
    active_deals = Column(Integer, nullable=False)
    pinned_ipfs_size = Column(Integer, nullable=False)
    sealed_storage = Column(Integer, nullable=False)
    bucket_count = Column(Integer, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "updated_at": self.updated_at,
            "miner_count": self.miner_count,
            "wallet_count": self.wallet_count,
            "source_file_cids": self.source_file_cids,
            "user_uploads": self.user_uploads,
            "active_deals": self.active_deals,
            "pinned_ipfs_size": self.pinned_ipfs_size,
            "pinned_ipfs_size": self.pinned_ipfs_size,
            "bucket_count": self.bucket_count}