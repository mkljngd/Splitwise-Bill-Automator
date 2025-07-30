# Splitwise Bill Automator

A Python CLI tool to simplify adding custom-split expenses (like groceries) to Splitwise — built to save time, avoid manual math, and automate the annoying parts of shared living.

---

## Features

- Parses simple text bills like:
- NOTE: Custom mapping of names should be added in `config.py`

Chicken $10.00 [M, D]
Milk $4.50 [M, H]
Snacks $6.00 [M, D, H]

- Calculates individual shares fairly
- Adds expenses to Splitwise groups via API
- Uses initials (e.g., `--payer M`) and maps them to full names
- Modular: easily add support for other bills

---

## Installation

1.  Clone the repo
2.  Set up a virtual environment (recommended):

python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

3.  Install dependencies:

pip install -r requirements.txt


4.	Set up your environment variables:

cp .env.example .env

# Then edit .env with your Splitwise API credentials



⸻

🚀 Usage

✅ Add a grocery bill:

python main.py --payer M --bill bills/star_bill.txt --group Roomies

	•	--payer M: Initial of the person who paid (e.g., M for Mukul)
	•	--bill: Path to your itemized bill text file
	•	--group: Splitwise group name

⸻
