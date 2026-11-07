# Economic Production Quantity (EPQ) finds the batch size per production run that
# balances setup cost against holding cost when stock is used while it is made.
# EPQ = sqrt(2*D*S / (H * (1 - d/p))), and the production rate must exceed the demand rate.

import math


def calculate_epq(demand, setup, hold_cost, d_rate, p_rate):
    """EPQ = sqrt(2DS / (H * (1 - d/p)))."""
    if p_rate <= d_rate:
        raise ValueError("Production rate must be greater than demand rate.")
    return math.sqrt((2 * demand * setup) / (hold_cost * (1 - d_rate / p_rate)))


def calculate_eoq(demand, setup, hold_cost):
    """Plain EOQ = sqrt(2DS / H), used for comparison."""
    return math.sqrt((2 * demand * setup) / hold_cost)


def epq_report(demand, setup, hold_cost, d_rate, p_rate, title):
    epq = calculate_epq(demand, setup, hold_cost, d_rate, p_rate)
    runs_per_year = demand / epq
    run_length_days = epq / p_rate
    max_inventory = epq * (1 - d_rate / p_rate)
    print("=" * 50)
    print(title)
    print("=" * 50)
    print("Optimal production quantity:", round(epq, 2))
    print("Production runs per year:", round(runs_per_year, 2))
    print("Length of each run (days):", round(run_length_days, 1))
    print("Maximum inventory level:", round(max_inventory, 2))
    return epq, runs_per_year, run_length_days, max_inventory


# Inputs (worked example)
annual_demand = 12000          # units per year
setup_cost = 50                # Rand per production run
holding_cost = 2               # Rand per unit per year
daily_demand_rate = 40         # units sold/used per day
daily_production_rate = 100    # units the process can make per day

if __name__ == "__main__":
    epq_report(annual_demand, setup_cost, holding_cost,
               daily_demand_rate, daily_production_rate,
               "Worked example (p = 100 units/day)")

    # Brief exercise 1: faster machine
    epq_report(annual_demand, setup_cost, holding_cost,
               daily_demand_rate, 150,
               "Try it yourself 1: faster machine (p = 150 units/day)")
    print("-> EPQ goes DOWN: with faster production, less of each batch is used up")
    print("   during the run, so peak stock (and holding cost) is higher; smaller")
    print("   batches become cheaper overall.")

    # Brief exercise 2: very large p approaches EOQ
    epq_big, *_ = epq_report(annual_demand, setup_cost, holding_cost,
                             daily_demand_rate, 100000,
                             "Try it yourself 2: very fast production (p = 100,000)")
    eoq = calculate_eoq(annual_demand, setup_cost, holding_cost)
    print("Plain EOQ (same D, S, H):", round(eoq, 2))
    print("Difference EPQ - EOQ:", round(epq_big - eoq, 2))
    print("-> When p is huge, d/p is close to 0, so (1 - d/p) is close to 1 and")
    print("   the EPQ formula becomes the EOQ formula (the batch arrives almost instantly).")
