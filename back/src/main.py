import json
import sqlite3
import datetime

from db.tbl.pay_tbl import PayTbl
from log.log import Log


if __name__ == '__main__':
    with open('../config.json') as f:
        config = json.load(f)
    log = Log(config)
    logger = log.get_logger()
    dbname = '../salary.db'
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()
    pay_tbl = PayTbl(cur, logger)
    payday = datetime.date(2021, 11, 23)
    registed_date = datetime.datetime.now()
    pay_tbl.insert(payday)
    pay_tbl.print_all()
    conn.commit()
    conn.close()
