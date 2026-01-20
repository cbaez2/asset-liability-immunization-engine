# ==================================================
# USER-EDITABLE PARAMETERS
# ==================================================
# ONLY EDIT THIS FILE TO CHANGE MODEL PARAMETERS
# ==================================================

# --------------------------------------------------
# IMMUNIZATION TYPE
# --------------------------------------------------
# "full"       → Full immunization (PV + Duration matching + ALA cashflow structure)
# "redington"  → Redington immunization (PV + Duration + convexity of assets > convexity of liabilities )
IMMUNIZATION_TYPE = "full"


# --------------------------------------------------
# BASE INTEREST RATE
# --------------------------------------------------
# i0 : interest rate to immunize asset portfolio
# Domain: i0 >= 0
i0 = 0.05


# --------------------------------------------------
# LIABILITY CASH FLOWS
# --------------------------------------------------
# liabilities[k] : amount of the k-th liability
# l_times[k]     : time at which liabilities[k] is due
# Liability structure is summarized and evaluated at i0
#
# Conventions:
# - liabilities and l_times must have the same length
# - l_times are assumed to be sorted in ascending order
# - No duplicate liability times

liabilities = [2600]*12
l_times     = [0,1,2,3,4,5,6,7,8,9,10,11]


# --------------------------------------------------
# ASSET CASH FLOW TIMES
# --------------------------------------------------
# a_times : times (years) of the two asset cash flows
#
# Output:
# - cf_x, cf_y: asset cash flow amounts and their PVs
# - All PVs computed at t = 0 using i0
a_times = [0,12]


# --------------------------------------------------
# REBALANCING / EVALUATION PARAMETERS
# --------------------------------------------------
# i_n : new interest rate, domain (0, ∞)
# t_n : rebalancing time, domain (0, last asset time)
#
# Output:
# - Re-immunized asset cash flows (cf_x, cf_y) and PVs based on chosen i_n and t_n
# - PVs computed at t = 0 using i_n
# - If Redington: interval of solvency { i : S(i) ≥ 0 }

i_n = 0.50
t_n = 10
