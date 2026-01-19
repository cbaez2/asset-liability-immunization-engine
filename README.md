# Asset–Liability Immunization Engine

A deterministic Python engine for constructing and rebalancing **two-asset portfolios** that immunize a given stream of liabilities under either **Full Immunization** or **Redington Immunization**.

The engine supports:
- exact asset cashflow construction,
- dynamic rebalancing after interest-rate changes and/or passage of time,
- and (for Redington) computation of a finite **interval of solvency**.

This project is intended as an **actuarial / ALM tool**, not a theoretical proof framework.

---

## Features

### 1. Full Immunization
- Constructs two asset cashflows that match:
  - Present Value
  - First derivative w.r.t. interest rate (duration)
- Enforces classical actuarial assumptions on the interest-rate domain.
- Supports rebalancing after:
  - rate shocks,
  - passage of time,
  - receipt of asset cashflows.

### 2. Redington Immunization
- Constructs two asset cashflows that satisfy:
  - Present Value matching,
  - Duration matching,
  - Positive surplus convexity at the base rate.
- Allows liability timing both inside and outside the asset interval.
- Supports dynamic rebalancing after rate/time changes.
- Computes a **finite interval of solvency** from the surplus function.

### 3. Rebalancing Engine
For both immunization types:
- Handles rebalancing at arbitrary times \( t_n \),
- Handles interest-rate changes from \( i_0 \) to \( i_n \),
- Correctly accounts for already-received asset cashflows.

### 4. Reporting
- All outputs are:
  - rounded to 4 decimal places,
  - clearly labeled with units,
  - expressed with actuarially standard notation.
- Asset cashflows are reported together with:
  - **PV₀ evaluated at the current rate** (e.g. `PV₀ = … @ iₙ`).

---

## Project Structure

asset-liability-immunization-engine/
│
├── main.py # Control file: select parameters and run the engine
├── full_imm.py # Full immunization constructor
├── full_rebalancer.py # Full immunization rebalancing logic
├── red_imm.py # Redington immunization constructor
├── red_rebalancer.py # Redington rebalancing logic
├── interval_finder.py # Interval of solvency computation (Redington)
└── README.md


---

## How to Run

1. Open `main.py`.
2. Set:
   - base interest rate `i0`,
   - liability amounts and times,
   - asset times,
   - immunization type (`FULL` or `REDINGTON`),
   - rebalancing parameters (`i_n`, `t_n`).
3. Run:
   ```bash
   python main.py
The engine prints:

initial asset construction,

rebalancing requirements,

and (if applicable) the interval of solvency.

Scope and Assumptions
Exactly two asset cashflows are used.

Deterministic interest-rate framework.

Classical actuarial discounting 
(
1
+
𝑖
)
−
𝑡
(1+i) 
−t
 .

The engine is constructive and diagnostic, not stochastic or optimization-based.

Intended Use
This project is suitable for:

actuarial ALM demonstrations,

immunization mechanics analysis,

portfolio rebalancing studies,

academic or internship portfolio projects.

Author
Created by Christopher Baez
Actuarial Science / Risk Management
Python • SymPy • Asset–Liability Management
