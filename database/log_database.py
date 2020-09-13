import csv
from utilities import Singleton
from .helper import UrlHelper
from .log import Log


class LogDatabase(metaclass=Singleton):

    def __init__(self, file_path):
        self.logs = []
        with open(file_path, 'r') as file:
            csv_file = csv.DictReader(file)
            for row in csv_file:
                self.logs.append(Log(
                    int(row['timestamp']),
                    UrlHelper.mask_url(row['url']),
                    row['method'],
                    float(row['response_time']),
                    int(row['response_code'])
                ))
