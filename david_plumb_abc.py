# ABC classification ranks SKUs by annual usage value (demand times unit cost) and
# groups them into tiers A, B, and C by cumulative share of total value.
# Default cutoffs are 80 percent for A and 95 percent for B; the remainder is C.

skus = [
    {"sku": "BRK-100", "demand": 2000, "cost": 45},
    {"sku": "GSK-220", "demand": 1500, "cost": 30},
    {"sku": "BLT-010", "demand": 10000, "cost": 2},
    {"sku": "BRG-330", "demand": 800, "cost": 60},
    {"sku": "SEAL-500", "demand": 3000, "cost": 5},
    {"sku": "MTR-700", "demand": 50, "cost": 800},
    {"sku": "WSH-050", "demand": 20000, "cost": 0.5},
    {"sku": "CBL-900", "demand": 400, "cost": 25},
]


def usage_value(demand, cost):
    return demand * cost


def assign_tier(cum_pct, a_limit=80, b_limit=95):
    if cum_pct <= a_limit:
        return "A"
    elif cum_pct <= b_limit:
        return "B"
    else:
        return "C"


def classify_inventory(skus, a_limit=80, b_limit=95):
    """Steps 2-6: value, sort, cumulative %, tier. Returns a new sorted, classified list
    (the input list is not modified)."""
    items = [dict(item) for item in skus]
    for item in items:
        item["value"] = usage_value(item["demand"], item["cost"])
    items_sorted = sorted(items, key=lambda item: item["value"], reverse=True)
    total_value = sum(item["value"] for item in items_sorted)
    running_total = 0
    for item in items_sorted:
        running_total += item["value"]
        item["cum_pct"] = (running_total / total_value) * 100
        item["tier"] = assign_tier(item["cum_pct"], a_limit, b_limit)
    return items_sorted


def count_tiers(items):
    tier_counts = {"A": 0, "B": 0, "C": 0}
    for item in items:
        tier_counts[item["tier"]] += 1
    return tier_counts


def print_report(items, title):
    print("=" * 55)
    print(title)
    print("=" * 55)
    for item in items:
        print(item["sku"], "| value:", item["value"],
              "| cum %:", round(item["cum_pct"], 1),
              "| tier:", item["tier"])
    print("SKUs per tier:", count_tiers(items))


if __name__ == "__main__":
    result = classify_inventory(skus)
    print_report(result, "Worked example (A <= 80%, B <= 95%)")

    # Brief exercise 1: two additional SKUs
    extra = skus + [
        {"sku": "FLT-120", "demand": 600, "cost": 35},
        {"sku": "PMP-410", "demand": 30, "cost": 1200},
    ]
    print_report(classify_inventory(extra), "Try it yourself 1: 10 SKUs (two added)")

    # Brief exercise 2: thresholds 70% / 90%
    print_report(classify_inventory(skus, 70, 90),
                 "Try it yourself 2: thresholds A <= 70%, B <= 90%")
