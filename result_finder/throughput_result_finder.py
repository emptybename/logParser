from .result_finder import ResultFinder
from utilities import ThroughputConstant
from prettytable import PrettyTable


class ThroughputResultFinder(ResultFinder):
    def __init__(self, db):
        super().__init__(db)
        self.result = []
        self.number_of_top_logs = ThroughputConstant.TOP

    def prepare_result(self):
        log_frequency = {}
        for log in self.db.logs:
            key = (log.url, log.method)
            log_frequency[key] = log_frequency.get(key, 0) + 1

        sorted_log_frequency = sorted(log_frequency.items(), key=lambda kv: kv[1])
        # self.result.append("Method    URL    Frequency")
        for _log_frequency in sorted_log_frequency[:(self.number_of_top_logs + 1) * -1:-1]:
            self.result.append([_log_frequency[0][1], _log_frequency[0][0], str(_log_frequency[1])])
            # log_template = _log_frequency[0][1] + "    " + _log_frequency[0][0] + "    " + str(_log_frequency[1])
            # self.result.append(log_template)

    def get_result(self):
        table = PrettyTable(['Method', 'URL', 'Frequency'])
        for row in self.result:
            table.add_row(row)
        return table

    def print_result(self):
        print("************ Throughput Result **************\n")
        print(self.get_result())
