import sqlite3
import logging

from db.tbl.base_tbl import BaseTbl


class PaymentItemTbl(BaseTbl):
    def __init__(self, cur: sqlite3.Cursor, logger: logging.Logger):
        super().__init__(cur, 'payment_item', logger.getChild('PaymentItemTbl'))
        if not self.is_exist():
            self.create_table()

    def create_table(self):
        item = {'name': 'item', 'type': 'STRING', 'primary': True}
        type = {'name': 'type', 'type': 'STRING'}
        return super().create_table(item, type)

    def insert(self, item: str, type: str):
        columns = ['item', 'type']
        inserts = [item, type]
        return super().insert(columns, inserts)
