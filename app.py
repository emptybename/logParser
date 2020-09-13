import sys
from database.log_database import LogDatabase
from result_finder import StatisticResultFinder, ThroughputResultFinder


def main(file_path):
    file_path = file_path or 'database.csv'

    # Creating in memory Object
    db = LogDatabase(file_path)

    # Creating Object for first type of result(Throughput)
    throughput_result = ThroughputResultFinder(db)
    throughput_result.prepare_result()
    throughput_result.print_result()
    print("\n\n")

    # Creating Object for 2nd type of result(Min, Max, Average)
    statistic_result = StatisticResultFinder(db)
    statistic_result.prepare_result()
    statistic_result.print_result()


if __name__ == '__main__':
    main(sys.argv[1:][0])
