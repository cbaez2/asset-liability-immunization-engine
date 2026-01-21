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
# a_times : times of the two asset cash flows
#
# Output:
# - cf_x, cf_y: asset cash flow amounts and their PVs
# - All PVs computed at t = 0 under i0
a_times = [0,12]


# --------------------------------------------------
# RE-IMMUNIZATION / EVALUATION PARAMETERS
# --------------------------------------------------
# i_n : new interest rate, domain (0, ∞)
# t_n : re-immunization time, domain (0, last asset time)
#
# Output:
# - asset cash flows (cf_x, cf_y) needed to re-immunize asset portfolio at t_n under i_n and their PVs
# - All PVs computed at t = 0 using i_n 
# - If Redington: interval of solvency { i : S(i) ≥ 0 } where S(i) = PV_A(i) - PV_L(i), the surplus as a function of i

i_n = 0.50
t_n = 10
