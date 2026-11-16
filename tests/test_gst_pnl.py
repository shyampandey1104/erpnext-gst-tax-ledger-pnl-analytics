import unittest
from gst_pnl.engine import FinancialAnalyticsEngine, PeriodTrialBalance

class TestFinancialAnalytics(unittest.TestCase):
    def test_pnl_margins_and_ratios(self):
        engine = FinancialAnalyticsEngine()
        tb = PeriodTrialBalance(
            revenue_from_operations=10000000.0, # ₹1 Crore
            other_income=200000.0,
            cost_of_materials_consumed=4000000.0, # 40 Lakhs COGS -> 60% GP
            employee_benefit_expenses=2000000.0,  # 20 Lakhs
            other_operating_expenses=1000000.0,   # 10 Lakhs -> EBITDA = 1.02 Cr - 70L = 32L
            depreciation_and_amortization=500000.0, # 5L
            finance_costs=200000.0,               # 2L -> NPBT = 25 Lakhs
            cash_and_bank_balances=2500000.0,
            trade_receivables=3500000.0,          # CA = 60 Lakhs
            trade_payables=1500000.0,
            current_liabilities=3000000.0,        # Current Ratio = 60/30 = 2.0
            shareholder_equity=5000000.0
        )

        fin = engine.generate_pnl_and_ratios(tb)
        self.assertEqual(fin.gross_profit, 6000000.0)
        self.assertEqual(fin.gross_profit_margin_pct, 60.0)
        self.assertEqual(fin.ebitda, 3200000.0)
        self.assertEqual(fin.net_profit_before_tax, 2500000.0)
        self.assertEqual(fin.current_ratio, 2.0)
        self.assertEqual(fin.financial_health_rating, "ROBUST_AAA")

if __name__ == "__main__":
    unittest.main()
