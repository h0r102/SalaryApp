import enum


class PAYMENT_TYPE(enum.Enum):
    BASE = enum.auto()      # 基準賃金
    ALLOWANCE = enum.auto()  # 手当
    BENEFIT = enum.auto()   # 福利厚生
    REFUND = enum.auto()    # 還付金
    OTHER = enum.auto()


class DEDUCTION_TYPE(enum.Enum):
    TAX = enum.auto()       # 税金
    INSURANCE = enum.auto()  # 保険料
    DUES = enum.auto()      # 会費
    STOCK = enum.auto()     # 株
    PURCHACE = enum.auto()  # 購入費
    OTHER = enum.auto()
