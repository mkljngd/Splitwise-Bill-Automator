from api_client import get_splitwise_object
from bill_parser import parse_text_bill
from cli import parse_cli_args
from expense_handler import create_expense_user, submit_expense
from config import USERS_DICT


def main():
    args = parse_cli_args()
    payer_name = USERS_DICT[args.payer]

    sObj = get_splitwise_object()
    group = next((g for g in sObj.getGroups() if g.getName() == args.group), None)

    if not group:
        print(f"[ERROR] Group '{args.group}' not found!")
        return

    with open(args.bill) as f:
        bill_text = f.read()

    bill_shares = parse_text_bill(bill_text)

    group_members = {m.getFirstName(): m.getId() for m in group.getMembers()}
    users = []

    for name, user_id in group_members.items():
        paid = sum(bill_shares.values()) if name == payer_name else 0
        owed = bill_shares.get(name, 0)
        users.append(create_expense_user(user_id, paid, owed))

    submit_expense(sObj, group, users, sum(bill_shares.values()), args.title, bill_text)


if __name__ == "__main__":
    main()
