import csv
from utilities import Singleton
from .helper import UrlHelper
from .log import Log


# class Log:
#     def __init__(self, timestamp, url, method, response_time, response_code):
#         self.timestamp = timestamp
#         self.url = url
#         self.method = method
#         self.response_time = response_time
#         self.response_code = response_code


class LogDatabase(metaclass=Singleton):

    def __init__(self, file_path):
        self.logs = []
        with open(file_path, 'r') as file:
            csv_file = csv.DictReader(file)
            for row in csv_file:
                self.logs.append(Log(
                    row['timestamp'],
                    UrlHelper.mask_url(row['url']),
                    row['method'],
                    row['response_time'],
                    row['response_code']
                ))
