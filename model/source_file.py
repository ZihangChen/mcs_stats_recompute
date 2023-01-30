from sqlalchemy import Column, Boolean, Integer, String, Text

from db import Base

class SourceFile(Base):
    __tablename__ = 'source_file'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    payload_cid = Column(String(100), nullable=False)
    resource_uri = Column(String(750), nullable=False)
    ipfs_url = Column(String(1000), nullable=False)
    file_size = Column(Integer, nullable=False)
    dataset = Column(String(100))
    pin_status = Column(String(100), nullable=False)
    create_at = Column(Integer, nullable=False)
    update_at = Column(Integer, nullable=False)