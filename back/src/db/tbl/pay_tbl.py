import sqlite3
import logging
import datetime

from db.tbl.base_tbl import BaseTbl


class PayTbl(BaseTbl):
    def __init__(self, cur: sqlite3.Cursor, logger: logging.Logger):
        super().__init__(cur, 'pay', logger.getChild('PayTbl'))
        if not self.is_exist():
            self.create_table()

    def create_table(self):
        id = {'name': 'id', 'type': 'INTEGER',
              'primary': True, 'auto_increment': True}
        payday = {'name': 'payday', 'type': 'DATE'}
        registed_date = {'name': 'registed_date', 'type': 'DATE'}
        return super().create_table(id, payday, registed_date)

    def insert(self, payday: datetime.date):
        columns = ['payday', 'registed_date']
        str_payday = payday.strftime('"%Y-%m-%d"')
        registed_date = datetime.datetime.now()
        str_registed_date = registed_date.strftime('"%Y-%m-%d"')
        inserts = [str_payday, str_registed_date]
        return super().insert(columns, inserts)
