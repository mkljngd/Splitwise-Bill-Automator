import argparse
from config import USERS_DICT


def parse_cli_args():
    parser = argparse.ArgumentParser(description="Splitwise Bill Adder")
    parser.add_argument(
        "--payer",
        required=True,
        choices=USERS_DICT.keys(),
        help="Initial of the person who paid (e.g., M, D, H)",
    )
    parser.add_argument("--bill", default="bills/star_bill.txt", help="Bill file path")
    parser.add_argument("--group", default="Roomies", help="Group name on Splitwise")
    parser.add_argument("--title", default="Shared Expense", help="Expense title")
    return parser.parse_args()
