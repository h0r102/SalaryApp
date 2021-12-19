import enum


class PAYMENT_TYPE(enum.Enum):
    BASE = enum.auto()


class DEDUCTION_TYPE(enum.Enum):
    TAX = enum.auto()
