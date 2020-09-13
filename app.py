from database.log_database import LogDatabase
from result_finder import MixedResultFinder, ThroughputResultFinder


def main():
    print('Please Enter file path')
    file_path = input('')
    file_path = file_path or 'database.csv'

    # Creating in memory Object
    db = LogDatabase(file_path)

    # Creating Object for first type of result(Throughput)
    throughput = ThroughputResultFinder(db)
    throughput.prepare_result()
    print(throughput)

    # Creating Object for 2nd type of result(Min, Max, Average)
    mixed_result = MixedResultFinder(db)
    mixed_result.prepare_result()
    print()
    print()
    print(mixed_result)


if __name__ == '__main__':
    main()
