import datetime as dt
from decimal import Decimal
from enum import Enum

from pydantic import BaseModel, Field, computed_field


class Category(str, Enum):
    RENTAL_INCOME = "Rental Income"
    SECURITY_DEPOSIT = "Security Deposit"
    TRANSFER = "Transfer"
    MORTGAGE_INTEREST = "Mortgage Interest"
    MORTGAGE_PRINCIPAL = "Mortgage Principal"
    PROPERTY_TAX = "Property Tax"
    INSURANCE = "Insurance"
    REPAIRS = "Repairs & Maintenance"
    UTILITIES = "Utilities"
    HOA_FEES = "HOA Fees"
    BANK_FEES = "Bank Fees"
    NEEDS_REVIEW = "Needs Review"


class RawTransaction(BaseModel):
    """One row as read from the file, before any categorization."""

    row_number: int
    date: dt.date
    description: str
    amount: Decimal  # positive = money in, negative = money out


class CategorizedTransaction(BaseModel):
    """A transaction after the brain has decided what it is."""

    id: int
    date: dt.date
    description: str
    normalized: str
    amount: Decimal
    category: Category
    confidence: float = Field(ge=0, le=1)
    explanation: str
    is_duplicate: bool = False

    @computed_field
    @property
    def needs_review(self) -> bool:
        return self.category == Category.NEEDS_REVIEW