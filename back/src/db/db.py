import datetime


class BaseTbl:
    def __init__(self, cur, tblname, logger):
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

    def create_table(self, *dicts_column):
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
                # error
                str_column = ''
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

    def insert(self, columns, inserts):
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


class PayTbl(BaseTbl):
    def __init__(self, cur, logger):
        super().__init__(cur, 'pay', logger.getChild('PayTbl'))
        if not self.is_exist():
            self.create_table()

    def create_table(self):
        id = {'name': 'id', 'type': 'INTEGER',
              'primary': True, 'auto_increment': True}
        payday = {'name': 'payday', 'type': 'DATE'}
        registed_date = {'name': 'registed_date', 'type': 'DATE'}
        return super().create_table(id, payday, registed_date)

    def insert(self, payday):
        columns = ['payday', 'registed_date']
        str_payday = payday.strftime('"%Y-%m-%d"')
        registed_date = datetime.datetime.now()
        str_registed_date = registed_date.strftime('"%Y-%m-%d"')
        inserts = [str_payday, str_registed_date]
        return super().insert(columns, inserts)


class Database:
    def __init__(self, cfgname):
        self.cfgname = cfgname

    # def open(self):
    #     with open(self.cfgname, 'rb') as fp:
    #         self._cfg = json.load(fp)
    #     self.dbname = self._cfg.get('dbname')

    #     self._conn = sqlite3.connect(self.dbname)
    #     self._cur = self._conn.cursor()

    # def close(self):
    #     self._conn.close()
