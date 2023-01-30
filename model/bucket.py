from sqlalchemy import Column, Integer, String, Boolean, DateTime

from db import Base

class Bucket(Base):
    __tablename__ = 'bucket'

    bucket_uid = Column(String(255))
    address = Column(String(255))
    max_size = Column(Integer)
    size = Column(Integer)
    is_free = Column(Boolean)
    is_deleted = Column(Boolean)
    bucket_name = Column(String(255))
    file_number = Column(Integer)
    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)
    is_active = Column(DateTime)