import sqlite3
import logging


class BaseTbl:
    def __init__(self, cur: sqlite3.Cursor, tblname: str, logger: logging.Logger):
        self._cur = cur
        self.tblname = tblname
        self.logger = logger

    def is_exist(self):
        str_exe = """
            SELECT COUNT(*) FROM sqlite_master
            WHERE TYPE='table' AND name='{}'
            """.format(self.tblname)
        self._cur.execute(str_exe)
        if self._cur.fetchone()[0] == 0:
            return False
        return True

    def create_table(self, *dicts_column: dict):
        # dicts_column
        #   'name': column name
        #   'type': 'STRING' or 'INTEGER'
        #   'primary': True or False
        columns = []
        for d in dicts_column:
            str_column = ''
            name = d.get('name')
            type = d.get('type')
            if (name is None) or (type is None):
                self.logger.error(
                    'Invalid column. dict_column={}'.format(d))
                return
            else:
                str_column += '{} {}'.format(name, type)
            primary = d.get('primary')
            if primary:
                str_column += ' PRIMARY KEY'
            auto_increment = d.get('auto_increment')
            if auto_increment:
                str_column += ' AUTOINCREMENT'
            columns.append(str_column)
        str_columns = ', '.join(columns)
        str_exe = 'CREATE TABLE {}({})'.format(
            self.tblname, str_columns)
        self._cur.execute(str_exe)
        self.logger.info('Table was created. table={}'.format(self.tblname))

    def del_table(self):
        str_exe = 'DROP TABLE ' + self.tblname
        self._cur.execute(str_exe)
        self.logger.info('Table was deleted. table={}'.format(self.tblname))

    def insert(self, columns: list[str], inserts: list[str]):
        str_exe = 'INSERT INTO {}({}) values({})'.format(
            self.tblname,
            ', '.join(columns),
            ', '.join(inserts))
        self._cur.execute(str_exe)
        self.logger.info(
            'Item was inserted. table={}, item={}'.format(
                self.tblname, inserts))

    def print_all(self):
        str_exe = 'SELECT * FROM ' + self.tblname
        self._cur.execute(str_exe)
        for row in self._cur:
            self.logger.debug(row)
