"""
Starting point of the program.
"""

import argparse
from extraction import extraction
from datetime import datetime
import evaluators
from support import results_logger, data_exporter


def get_args() -> any:
    """
    Used to retrieve the program arguments.
    :return: the program arguments.
    """
    parser = argparse.ArgumentParser(description="Gather unit tests from Java files")
    parser.add_argument("--directory", help="Path to the directory containing Java files")
    args = parser.parse_args()
    return args


def run() -> None:
    """
    Runs the analysis.
    """
    results_logger.setup_logger()

    args = get_args()
    directory = args.directory
    if directory is None:
        exit("Error: missing --directory argument.")

    time_stamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    scalabrino_analysis(directory, time_stamp)
    complexity_analysis(directory, time_stamp)


def scalabrino_analysis(directory: str, time_stamp: str) -> None:
    """
    Scalabrino analysis.
    """
    scalabrino_logged_data = {'Class': [], 'Scalabrino score': []}
    scalabrino_results = evaluators.calculate_scalabrino_score(directory)
    for result in scalabrino_results:
        print(f'Class: {result[0]:<40} | Score: {result[1]}')
        scalabrino_logged_data['Class'].append(result[0])
        scalabrino_logged_data['Scalabrino score'].append(result[1])

    data_exporter.write_scalabrino(scalabrino_logged_data, time_stamp)


def complexity_analysis(directory: str, time_stamp: str) -> None:
    """
    Complexity checker
    """
    test_classes = extraction.extract_test_classes(directory)

    for test_class in test_classes:
        total_lines = 0
        total_reoccurring_code = 0
        total_assertions = 0
        total_flow_constructs = 0
        complexitest_logged_data = {'Number of Lines': [], 'Setup points': [],
                                    'Assertion points': [], 'Flow constructs': []}
        # reoccurring code, two or more lines of identical code in two tests awards points
        reoccurring_code = evaluators.run_reoccurring_code_checker(test_class)

        # lines, points for LOC in test. discards empty lines, assertions and comments
        lines = evaluators.run_number_of_lines_checker(test_class)

        # assertions, returns list with different types of assertions found.
        assertions = evaluators.run_count_assertions(test_class)

        # flow constructs - returns list of number of is single flow constructs, second value is nested flow constructs
        flow_constructs = evaluators.run_flow_constructs_checker(test_class)

        # Calculations
        # Formatting of scores
        # five types of assertions, sum of all for score
        # one point for flow constructs, two points for nested ones
        total_lines += reoccurring_code
        total_reoccurring_code += reoccurring_code
        total_assertions += assertions
        total_flow_constructs += flow_constructs

        # logging
        print("logging...")
        complexitest_logged_data['Number of Lines'].append(str(lines))
        complexitest_logged_data['Setup points'].append(str(reoccurring_code))
        complexitest_logged_data['Assertion points'].append(str(assertions))
        complexitest_logged_data['Flow constructs'].append(str(total_flow_constructs))
        data_exporter.write_complexity(complexitest_logged_data, str(test_class.name), time_stamp)


if __name__ == "__main__":
    run()
