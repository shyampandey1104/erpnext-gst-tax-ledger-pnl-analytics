"""Accounting, GST Tax Ledger, Real-Time Profit & Loss (P&L) and Balance Sheet Ratios Engine."""

from typing import Dict, Any, List, Optional
from dataclasses import dataclass, field


@dataclass
class PeriodTrialBalance:
    revenue_from_operations: float
    other_income: float
    cost_of_materials_consumed: float
    employee_benefit_expenses: float
    other_operating_expenses: float
    depreciation_and_amortization: float
    finance_costs: float
    cash_and_bank_balances: float
    trade_receivables: float
    trade_payables: float
    current_liabilities: float
    shareholder_equity: float


@dataclass
class ExecutiveFinancialSummary:
    gross_turnover: float
    gross_profit: float
    gross_profit_margin_pct: float
    ebitda: float
    ebitda_margin_pct: float
    net_profit_before_tax: float
    net_profit_margin_pct: float
    current_ratio: float           # Current Assets / Current Liabilities (Benchmark >= 1.5)
    debt_to_equity_ratio: float
    financial_health_rating: str  # ROBUST_AAA, HEALTHY_AA, STRESSED_LIQUIDITY


class FinancialAnalyticsEngine:
    """Computes executive Profit & Loss margins, EBITDA, working capital health, and statutory GST tax balances."""

    def generate_pnl_and_ratios(self, tb: PeriodTrialBalance) -> ExecutiveFinancialSummary:
        gross_turnover = tb.revenue_from_operations + tb.other_income
        gross_profit = tb.revenue_from_operations - tb.cost_of_materials_consumed
        gp_margin = round((gross_profit / tb.revenue_from_operations) * 100.0, 2) if tb.revenue_from_operations > 0 else 0.0

        # EBITDA = Revenue - (COGS + Employee Expenses + Other Operating Expenses)
        operating_expenses = tb.cost_of_materials_consumed + tb.employee_benefit_expenses + tb.other_operating_expenses
        ebitda = round(gross_turnover - operating_expenses, 2)
        ebitda_margin = round((ebitda / gross_turnover) * 100.0, 2) if gross_turnover > 0 else 0.0

        # Net Profit = EBITDA - Depreciation - Finance Costs
        npbt = round(ebitda - tb.depreciation_and_amortization - tb.finance_costs, 2)
        np_margin = round((npbt / gross_turnover) * 100.0, 2) if gross_turnover > 0 else 0.0

        # Balance Sheet Ratios
        current_assets = tb.cash_and_bank_balances + tb.trade_receivables
        curr_ratio = round(current_assets / tb.current_liabilities, 2) if tb.current_liabilities > 0 else 1.0

        d_e_ratio = round(tb.trade_payables / tb.shareholder_equity, 2) if tb.shareholder_equity > 0 else 0.0

        if curr_ratio >= 1.5 and np_margin >= 10.0:
            rating = "ROBUST_AAA"
        elif curr_ratio >= 1.1 and np_margin >= 5.0:
            rating = "HEALTHY_AA"
        else:
            rating = "STRESSED_LIQUIDITY"

        return ExecutiveFinancialSummary(
            gross_turnover=gross_turnover,
            gross_profit=round(gross_profit, 2),
            gross_profit_margin_pct=gp_margin,
            ebitda=ebitda,
            ebitda_margin_pct=ebitda_margin,
            net_profit_before_tax=npbt,
            net_profit_margin_pct=np_margin,
            current_ratio=curr_ratio,
            debt_to_equity_ratio=d_e_ratio,
            financial_health_rating=rating
        )
