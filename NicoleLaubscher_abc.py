#Web Application Assessment Project 2
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


#Calculate usage value per SKU
def usage_value(demand, cost):
    return demand * cost


for item in skus:
    item["value"] = usage_value(item["demand"], item["cost"])


#Sort descending by value
skus_sorted = sorted(skus, key=lambda item: item["value"], reverse=True)


#Calculate cumulative %
total_value = sum(item["value"] for item in skus_sorted)

running_total = 0

for item in skus_sorted:
    running_total += item["value"]
    item["cum_pct"] = (running_total / total_value) * 100


#Assign a tier
def assign_tier(cum_pct):
    if cum_pct <= 80:
        return "A"
    elif cum_pct <= 95:
        return "B"
    else:
        return "C"


for item in skus_sorted:
    item["tier"] = assign_tier(item["cum_pct"])


print("ORIGINAL ABC INVENTORY CLASSIFICATION")
print("-------------------------------------")

for item in skus_sorted:
    print(
        item["sku"],
        "| value:", item["value"],
        "| cum %:", round(item["cum_pct"], 1),
        "| tier:", item["tier"]
    )


# Count SKUs per tier
tier_counts = {"A": 0, "B": 0, "C": 0}

for item in skus_sorted:
    tier_counts[item["tier"]] += 1

print("\nOriginal tier counts:")
print(tier_counts)


# TRY IT YOURSELF
print("--------------------------------")

print("TRY IT YOURSELF")

#Try it yourself
# 1)Add two more SKUs

print("\nQUESTION 1 - ADD TWO MORE SKUs")
print("--------------------------------")
skus_try_1 = [
    {"sku": "BRK-100", "demand": 2000, "cost": 45},
    {"sku": "GSK-220", "demand": 1500, "cost": 30},
    {"sku": "BLT-010", "demand": 10000, "cost": 2},
    {"sku": "BRG-330", "demand": 800, "cost": 60},
    {"sku": "SEAL-500", "demand": 3000, "cost": 5},
    {"sku": "MTR-700", "demand": 50, "cost": 800},
    {"sku": "WSH-050", "demand": 20000, "cost": 0.5},
    {"sku": "CBL-900", "demand": 400, "cost": 25},
    {"sku": "NUT-120", "demand": 5000, "cost": 1},
    {"sku": "FLT-600", "demand": 100, "cost": 50},
]
for item in skus_try_1:
    item["value"] = usage_value(item["demand"], item["cost"])


skus_try_1_sorted = sorted(
    skus_try_1,
    key=lambda item: item["value"],
    reverse=True
)


total_value_try_1 = sum(
    item["value"] for item in skus_try_1_sorted
)


running_total_try_1 = 0

for item in skus_try_1_sorted:
    running_total_try_1 += item["value"]
    item["cum_pct"] = (
        running_total_try_1 / total_value_try_1
    ) * 100


for item in skus_try_1_sorted:
    item["tier"] = assign_tier(item["cum_pct"])


tier_counts_try_1 = {"A": 0, "B": 0, "C": 0}

for item in skus_try_1_sorted:
    tier_counts_try_1[item["tier"]] += 1


for item in skus_try_1_sorted:
    print(
        item["sku"],
        "| value:", item["value"],
        "| cum %:", round(item["cum_pct"], 1),
        "| tier:", item["tier"]
    )


print("\nTier counts after adding two SKUs:")
print(tier_counts_try_1)



# 2)Change classification thresholds to 70% / 90%
print("\nQUESTION 2 - CHANGE THRESHOLDS TO 70% / 90%")
print("--------------------------------------------")


def assign_tier_try(cum_pct):
    if cum_pct <= 70:
        return "A"
    elif cum_pct <= 90:
        return "B"
    else:
        return "C"


for item in skus_try_1_sorted:
    item["tier"] = assign_tier_try(item["cum_pct"])


tier_counts_try_2 = {"A": 0, "B": 0, "C": 0}

for item in skus_try_1_sorted:
    tier_counts_try_2[item["tier"]] += 1


for item in skus_try_1_sorted:
    print(
        item["sku"],
        "| value:", item["value"],
        "| cum %:", round(item["cum_pct"], 1),
        "| tier:", item["tier"]
    )


print("\nTier counts using 70% / 90% thresholds:")
print(tier_counts_try_2)


# 3)Wrap Steps 2-6 into classify_inventory(skus)
print("\nQUESTION 3 - CLASSIFY_INVENTORY FUNCTION")
print("----------------------------------------")


def classify_inventory(skus):

    for item in skus:
        item["value"] = usage_value(item["demand"], item["cost"])

    skus_sorted = sorted(
        skus,
        key=lambda item: item["value"],
        reverse=True
    )

    total_value = sum(
        item["value"] for item in skus_sorted
    )

    running_total = 0

    for item in skus_sorted:
        running_total += item["value"]
        item["cum_pct"] = (
            running_total / total_value
        ) * 100

    for item in skus_sorted:
        item["tier"] = assign_tier_try(item["cum_pct"])

    for item in skus_sorted:
        print(
            item["sku"],
            "| value:", item["value"],
            "| cum %:", round(item["cum_pct"], 1),
            "| tier:", item["tier"]
        )

    return skus_sorted


skus_try_3_sorted = classify_inventory(skus_try_1)