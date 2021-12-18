import os
import logging
import logging.handlers


class Log:
    def __init__(self, config):
        self.config = config
        self.logger = logging.getLogger('root')
        self._set_level()
        self._set_stream_handler()
        self._set_file_handler()

    def _set_level(self):
        level = self.config['log_level']
        if level == 'CRITICAL':
            self.logger.setLevel(logging.CRITICAL)
        elif level == 'ERROR':
            self.logger.setLevel(logging.ERROR)
        elif level == 'WARNING':
            self.logger.setLevel(logging.WARNING)
        elif level == 'INFO':
            self.logger.setLevel(logging.INFO)
        else:  # level == 'DEBUG'
            self.logger.setLevel(logging.DEBUG)

    def _get_formatter(self):
        fmt = self.config['log_format']
        formatter = logging.Formatter(fmt)
        return formatter

    def _set_stream_handler(self):
        handler = logging.StreamHandler()
        formatter = self._get_formatter()
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def _set_file_handler(self):
        dirpath = self.config['log_dirpath']
        dirpath = os.path.expanduser(dirpath)
        os.makedirs(dirpath, exist_ok=True)
        filename = self.config['log_filename']
        filepath = dirpath + filename
        max_bytes = self.config['log_max_kbytes'] + 1024
        backup_count = self.config['log_backup_count']
        encoding = self.config['log_encoding']
        handler = logging.handlers.RotatingFileHandler(
            filepath,
            maxBytes=max_bytes,
            backupCount=backup_count,
            encoding=encoding)
        formatter = self._get_formatter()
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def get_logger(self):
        return self.logger
