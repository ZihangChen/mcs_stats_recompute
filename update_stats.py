import time, logging, math, toml
from sqlalchemy import func

from db import get_db
from model.miner import Miner
from model.offline_deal import OfflineDeal
from model.source_file import SourceFile
from model.source_file_upload import SourceFileUpload
from model.wallet import Wallet
from model.car_file import CarFile
from model.car_file_source import CarFileSource
from model.marketing_stats import MarketingStats
from model.oss_file import OSSFile
from model.bucket import Bucket

def scan():
    base_val = toml.load('config.toml')['basevalue']
    
    try:
        session = get_db()
        records = session.query(MarketingStats).all()

        for record in records:
            query = ("SELECT SUM(file_size) FROM source_file_upload \
                        INNER JOIN source_file \
                        ON source_file_upload.source_file_id=source_file.id \
                        WHERE source_file_upload.source_file_id \
                        IN (SELECT id from source_file) and \
                        (source_file_upload.pin_status='Pinned' or source_file_upload.pin_status='UnPinned') \
                        and source_file_upload.create_at <= :x")
            result = session.execute(query, {"x": record.updated_at}).fetchone()[0]
            record.pinned_ipfs_size = base_val['pinned_ipfs_size'] + result

            query = ("SELECT sum(power(2,ceil(log2(cast(car_file_size as unsigned))))) FROM offline_deal \
                    INNER JOIN car_file \
                    ON offline_deal.car_file_id=car_file.id \
                    WHERE (offline_deal.status='Success' or offline_deal.status='Active') and offline_deal.car_file_id is not null \
                    and offline_deal.create_at <= :x")
            result = session.execute(query, {"x": record.updated_at}).fetchone()[0]
            record.sealed_storage = base_val['sealed_storage'] + result
    finally:
        session.add_all(records)
        session.commit()
        session.close()

if __name__ == "__main__":
    scan()