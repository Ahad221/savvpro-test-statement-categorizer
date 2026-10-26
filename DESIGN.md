# Design

## Use case
A small landlord with 1-3 rental properties who uses one bank account
(and optionally one credit card) for rental activity. At tax time they
need every transaction sorted into categories, with mortgage payments
split into interest and principal. The app produces totals the landlord
can hand to their accountant. It does not give tax advice.

## Categories
- Income: Rental Income
- Not income or spending: Security Deposit, Transfer
- Expenses: Mortgage Interest, Mortgage Principal, Property Tax,
  Insurance, Repairs & Maintenance, Utilities, HOA Fees, Bank Fees
- Special: Needs Review

## Edge cases and how each is handled
1. Mortgage payment is part interest, part principal. Split it using an
   amortization calculation from loan details the user provides. If no
   loan details exist, the row goes to Needs Review. Never a guess.
2. Security deposit received is not income -> Security Deposit.
3. Security deposit returned to a tenant is not an expense -> Security Deposit.
4. A refund from a vendor (e.g. plumber) is a negative expense, not income.
5. Transfers between the user's own accounts are neither income nor spending.
6. Rent paid in two partial payments: both rows are Rental Income.
7. Ambiguous merchants (HOME DEPOT: repair or improvement? AMAZON: supplies
   or personal?) -> Needs Review.
8. Duplicate rows (same date, amount, description) are flagged, not dropped,
   because a real repeat charge is possible.
9. Different bank CSV formats: different column names, date formats, and
   either one signed amount column or separate debit/credit columns.
10. Unknown merchants -> Needs Review.

## How the brain decides
1. Normalize the description: uppercase, strip store numbers, *, POS, dates.
2. Special-case checks first: transfers, deposits, refunds, mortgage.
3. Rule matching: keyword/merchant patterns, each with a weight.
4. Fuzzy matching as a fallback for near matches.
5. Confidence score from 0 to 1. Below the threshold (0.75) -> Needs Review.
6. Every decision carries a human-readable explanation.
7. User corrections are saved as new rules and applied to similar rows.

## Out of scope
Multi-property attribution, real bank integrations, tax filing.