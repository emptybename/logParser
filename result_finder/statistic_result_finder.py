from .result_finder import ResultFinder
from prettytable import PrettyTable


class StatisticResultFinder(ResultFinder):
    def __init__(self, db):
        super(StatisticResultFinder, self).__init__(db)
        self.result = []

    def prepare_result(self):
        log_dict = {}
        for log in self.db.logs:
            key = (log.url, log.method)
            if log_dict.get(key) is None:
                log_dict[key] = {
                    'min': log.response_time,
                    'max': log.response_time,
                    'avg': log.response_time,
                    'total': log.response_time,
                    'frequency': 1
                }
            else:
                log_dict[key]['min'] = min(log_dict[key]['min'], log.response_time)
                log_dict[key]['max'] = max(log_dict[key]['max'], log.response_time)
                log_dict[key]['total'] += log.response_time
                log_dict[key]['frequency'] += 1
                log_dict[key]['avg'] = "{:.2f}".format(log_dict[key]['total'] / log_dict[key]['frequency'])
        for item in log_dict.items():
            self.result.append([
                item[0][1], item[0][0], str(item[1]['min']),
                str(item[1]["max"]), str(item[1]['avg'])
            ])

    def get_result(self):
        table = PrettyTable(['Method', 'URL', 'Min TIme', 'Max Time', 'Average Time'])
        for row in self.result:
            table.add_row(row)
        return table

    def print_result(self):
        print("********* Statistic Result ************\n")
        print(self.get_result())
