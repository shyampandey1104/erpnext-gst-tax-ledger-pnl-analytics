# ERPNext GST Tax Ledger & P&L Financial Analytics Engine

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Finance](https://img.shields.io/badge/Accounting-P%26L%20%26%20Balance%20Sheet-darkgreen.svg)](https://frappe.io)

Delivers real-time C-Suite financial visibility: computing EBITDA, gross margins, working capital liquidity ratios (Current Ratio, Debt-to-Equity), and statutory GST tax balances directly from ERPNext trial balance accounts.

## Features
- **P&L Margin Engine:** Automated derivation of Gross Margin %, EBITDA, and Net Profit Before Tax (NPBT).
- **Liquidity Health Ratios:** Continuously assesses Current Ratios against standard 1.5x working capital solvency benchmarks.
- **GST 3B Liability Audit:** Balances output tax liabilities against available Input Tax Credit ledgers.

## Tests
```bash
python3 -m unittest discover tests
```
