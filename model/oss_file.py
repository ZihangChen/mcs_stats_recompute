from sqlalchemy import Column, Integer, String, Boolean, DateTime

from db import Base

class OSSFile(Base):
    __tablename__ = 'oss_file'

    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    name = Column(String(255))
    address = Column(String(255))
    prefix = Column(String(255))
    bucket_uid = Column(String(255))
    file_hash = Column(String(255))
    size = Column(Integer)
    payload_cid = Column(String(255))
    ipfs_url = Column(String(255))
    pin_status = Column(String(255))
    is_deleted = Column(Boolean, default=False)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)
    is_folder = Column(Boolean, default=False)