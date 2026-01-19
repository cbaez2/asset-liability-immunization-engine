# Asset–Liability Immunization Engine (Python)

## Overview

This project is a **deterministic Asset–Liability Immunization engine** implemented in Python using **SymPy**.

Given:
- an interes rate i0
- a fixed set of liability cashflow amounts,
- corresponding liability times, and
- exactly **two asset times**,

the program computes the **two asset cashflows** required to achieve either:

- **Full Immunization**, or
- **Redington Immunization**.

The engine also supports **rebalancing** after:
- a change in interest rate, and/or
- the passage of time.

For **Redington Immunization**, the engine additionally computes a **finite interval of solvency** over which the surplus function remains non-negative.

---

## Features

### Full Immunization

- Matches:
  - Present Value
  - First derivative (duration)
- Enforces classical ALA constraints
- Computes exact asset cashflows symbolically
- Supports rebalancing at arbitrary time `t_n` and interest rate `i_n`

---

### Redington Immunization

- Matches:
  - Present Value
  - Duration
  - Positive second derivative (convexity)
- Allows liabilities outside the asset interval
- Supports rebalancing at arbitrary time `t_n` and interest rate `i_n`
- Computes a **finite interval of solvency** directly from the surplus function

---

# Asset–Liability Immunization Engine (Python)

## Overview

This project is a **deterministic Asset–Liability Immunization engine** implemented in Python using **SymPy**.

Given:
- a fixed set of liability cashflow amounts,
- corresponding liability times, and
- exactly **two asset times**,

the program computes the **two asset cashflows** required to achieve either:

- **Full Immunization**, or
- **Redington Immunization**.

The engine also supports **rebalancing** after:
- a change in interest rate, and/or
- the passage of time.

For **Redington Immunization**, the engine additionally computes a **finite interval of solvency** over which the surplus function remains non-negative.

This project is a **computational tool**, not a proof system.

---

## Features

### Full Immunization

- Matches:
  - Present Value
  - First derivative (duration)
- Enforces classical ALA constraints
- Computes exact asset cashflows symbolically
- Supports rebalancing at arbitrary time `t_n` and interest rate `i_n`

---

### Redington Immunization

- Matches:
  - Present Value
  - First derivative
  - Positive second derivative (convexity)
- Allows liabilities outside the asset interval
- Supports rebalancing at arbitrary time `t_n` and interest rate `i_n`
- Computes a **finite interval of solvency** directly from the surplus function

---

## File Descriptions

### `main.py`

- Central control file
- User specifies:
  - Immunization type (`FULL` or `REDINGTON`)
  - Base interest rate `i0`
  - Asset times
  - Liability amounts and times
  - Rebalancing time `t_n` and rate `i_n`
- Executes the full pipeline and prints results
- No runtime user input is required

---

### `full_imm.py`

- Computes the two asset cashflows required to achieve **full immunization**
- Solves for present value and duration matching

---

### `full_rebalancer.py`

- Rebalances a fully immunized portfolio after:
  - a change in interest rate, and/or
  - the passage of time
- Correctly handles cases where one asset cashflow has already been received

---

### `red_imm.py`

- Computes the two asset cashflows required to achieve **Redington immunization**
- Enforces:
  - present value matching,
  - first derivative matching,
  - positive second derivative at `i0`

---

### `red_rebalancer.py`

- Rebalances a Redington-immunized portfolio after:
  - a change in interest rate, and/or
  - the passage of time
- Preserves Redington conditions locally

---

### `interval_finder.py`

- Analyzes the Redington surplus function
- Computes the **interval of solvency**:
  - the set of interest rates for which the surplus remains non-negative

## Example Output

A typical run reports:

- Initial immunization success
- Required asset cashflows
- Present values at time 0
- Rebalancing requirements after a rate shock
- Interval of solvency (Redington only)

Example excerpt:

=== REDINGTON IMMUNIZATION ===

Redington immunization succeeded at i₀ = 0.1000

Liabilities:
  amounts = [1000, 1000, 1000, 1000, 1000]
  times   = [0, 1, 2, 3, 4]

Required asset cashflows:
  cf_x = $3,843.6664 at t = 1  (PV₀ = $3,494.2422 at i₀)
  cf_y = $1,196.9078 at t = 6  (PV₀ = $675.6232 at i₀)


--- REBALANCING ---

The original surplus function evaluated at iₙ = 0.5000 is:
$62.5843

To be Redington immunized at iₙ = 0.5000 and t = 0, you need:
cf_x = $3,843.6664 at t = 1 (PV₀ = $2,562.4443 @ iₙ)
cf_y = $1,196.9078 at t = 6 (PV₀ = $105.0783 @ iₙ)

--- INTERVAL OF SOLVENCY ---

S(i) ≥ 0  ∀  i ∈ (0, 1.01475833214883]


