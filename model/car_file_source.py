from sqlalchemy import Column, Integer

from db import Base

class CarFileSource(Base):
    __tablename__ = 'car_file_source'

    car_file_id = Column(Integer, nullable=False)
    create_at = Column(Integer, nullable=False)
    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    source_file_upload_id = Column(Integer, nullable=False)