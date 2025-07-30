import re
from collections import defaultdict
from config import USERS_DICT


def parse_text_bill(input_text: str) -> dict:
    person_totals = defaultdict(float)
    lines = input_text.strip().split("\n")

    for line in lines:
        match = re.match(r"(.+?)\s+\$([\d.]+)\s+\[(.+?)\]", line)
        if match:
            item, price, people = match.groups()
            price = float(price)
            people_list = people.split(",")
            share = round(price / len(people_list), 2)
            for person in people_list:
                person_totals[person.strip()] += share

    return {
        USERS_DICT[person]: round(total, 2) for person, total in person_totals.items()
    }
