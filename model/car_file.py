from sqlalchemy import Column, Integer, String, Boolean

from db import Base

class CarFile(Base):
    __tablename__ = 'car_file'

    car_file_name = Column(String(200), nullable=False)
    car_file_path = Column(String(1000), nullable=False)
    car_file_size = Column(Integer, nullable=False)
    create_at = Column(Integer, nullable=False)
    duration = Column(Integer, nullable=False)
    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    is_free = Column(Boolean, nullable=False)
    max_price = Column(String(100), nullable=False)
    payload_cid = Column(String(200), nullable=False)
    piece_cid = Column(String(200), nullable=False)
    status = Column(String(100), nullable=False)
    task_uuid = Column(String(100), nullable=False)
    update_at = Column(Integer, nullable=False)