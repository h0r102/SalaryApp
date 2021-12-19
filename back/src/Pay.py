import datetime
import pandas as pd

from defines import PAYMENT_TYPE
from defines import DEDUCTION_TYPE


class Pay:
    def __init__(self):
        df_columns = ['name', 'type', 'amount']
        self._payments = pd.DataFrame(columns=df_columns)
        self._deductions = pd.DataFrame(columns=df_columns)
        self.payday = datetime.date(0, 0, 0)

    def calc_total_payments(self):
        """ 支給総額取得 """
        total_payments = self._payments['amount'].sum()
        return total_payments

    def calc_total_deductions(self):
        """ 控除総額取得 """
        total_deductions = self._deductions['amount'].sum()
        return total_deductions

    def calc_net_payment(self):
        """ 差引支給額取得 """
        total_payments = self.calc_total_payments()
        total_deductions = self.calc_total_deductions()
        net_payment = total_payments - total_deductions
        return net_payment

    def calc_sum_payments_by(self, type: PAYMENT_TYPE):
        """ 支給種別合計額取得 """
        targets = (self._payments['type'] == type)
        target_df = self._payments[targets]
        sum_payments = target_df['amount'].sum()
        return sum_payments

    def calc_sum_deductions_by(self, type: DEDUCTION_TYPE):
        """ 控除種別合計額取得 """
        targets = (self._deductions['type'] == type)
        target_df = self._deductions[targets]
        sum_deductions = target_df['amount'].sum()
        return sum_deductions

    def add_payment(self, name: str, type: PAYMENT_TYPE, amount: int):
        series = pd.Series([name, type, amount], index=self._payments.columns)
        self._payments.append(series)

    def add_deduction(self, name: str, type: DEDUCTION_TYPE, amount: int):
        series = pd.Series([name, type, amount],
                           index=self._deductions.columns)
        self._deductions.append(series)
