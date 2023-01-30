from sqlalchemy import Column, Boolean, Integer, String, Text

from db import Base

class SourceFileUpload(Base):
    __tablename__ = 'source_file_upload'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    source_file_id = Column(Integer, nullable=False)
    file_type = Column(Integer, nullable=False)
    file_name = Column(String(200), nullable=False)
    uuid = Column(String(100), nullable=False)
    wallet_id = Column(Integer, nullable=False)
    status = Column(String(100), nullable=False)
    duration = Column(Integer, nullable=False)
    create_at = Column(Integer, nullable=False)
    update_at = Column(Integer, nullable=False)
    pin_status = Column(String(100), nullable=False)
    is_free = Column(Boolean, nullable=False)