import math

annual_demand = 12000        # units per year 
setup_cost = 50              # cost per production run, in Rand 
holding_cost = 2             # cost per unit per year, in Rand 
daily_demand_rate = 40       # units produced/sold per day 
daily_production_rate = 100  # units your process can make per day

#EPQ:
def calculate_epq(demand, setup, hold_cost, d_rate, p_rate): 
    return math.sqrt((2 * demand * setup) / (hold_cost * (1 - d_rate / p_rate))) 
  
epq = calculate_epq(annual_demand, setup_cost, holding_cost, 
                    daily_demand_rate, daily_production_rate) 

print("Optimal production quantity:", round(epq, 2))

#Production runs per year and run length
runs_per_year = annual_demand / epq 
run_length_days = epq / daily_production_rate 
  
print("Production runs per year:", round(runs_per_year, 2)) 
print("Length of each run (days):", round(run_length_days, 1)) 

#Max inventory level
max_inventory = epq * (1 - daily_demand_rate / daily_production_rate) 
print("Maximum inventory level:", round(max_inventory, 2))

