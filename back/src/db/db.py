

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
