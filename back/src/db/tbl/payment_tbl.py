import sqlite3
import logging

from db.tbl.base_tbl import BaseTbl


class PaymentTbl(BaseTbl):
    def __init__(self, cur: sqlite3.Cursor, logger: logging.Logger):
        super().__init__(cur, 'payment', logger.getChild('PaymentTbl'))
        if not self.is_exist():
            self.create_table()

    def create_table(self):
        pay_id = {'name': 'pay_id', 'type': 'INTEGER', 'primary': True}
        item = {'name': 'item', 'type': 'STRING', 'primary': True}
        amount = {'name': 'amount', 'type': 'INTEGER'}
        return super().create_table(pay_id, item, amount)

    def insert(self, pay_id: int, item: str, amount: int):
        columns = ['pay_id', 'item', 'amount']
        inserts = [str(pay_id), item, str(amount)]
        return super().insert(columns, inserts)
