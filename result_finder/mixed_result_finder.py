from .result_finder import ResultFinder


class MixedResultFinder(ResultFinder):
    def __init__(self, db):
        super(MixedResultFinder, self).__init__(db)
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
                    'frequency': 1
                }
            else:
                log_dict[key]['min'] = min(log_dict[key]['min'], log.response_time)
                log_dict[key]['max'] = max(log_dict[key]['max'], log.response_time)
                total = (log_dict[key]['avg'] * log_dict[key]['frequency'] + log.response_time)
                log_dict[key]['frequency'] += 1
                log_dict[key]['avg'] = total / log_dict[key]['frequency']
        self.result.append("Method  URL  Min Time  Max Time  Average Time")
        for item in log_dict.items():
            self.result.append(
                item[0][1] + "  " + item[0][0] + "  " + str(item[1]['min']) + "  " + str(item[1]["max"]) + "  " + (
                    str(item[1]['avg'])
                )
            )

    def get_result(self):
        return "\n".join(self.result)

    def __str__(self):
        return self.get_result()
