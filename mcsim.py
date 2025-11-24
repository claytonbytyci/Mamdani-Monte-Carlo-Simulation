#%%
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

# np.random.seed(42)

# Model Parameters (based on reported claims on policy costs)
grocery_mean = 60_000_000
grocery_std = grocery_mean * 0.2

free_bus_mean = 711_507_000 
free_bus_std = 150_000_000

rent_freeze_mean =  6_840_000_000 / 4
rent_freeze_std = 400_000_000

'''tax_revenue_mean = 10_000_000_000
tax_revenue_std = 2_000_000_000'''

admin_mean = 50_000_000
admin_std = 20_000_000

landlord_prob = 0.05
landlord_mean = 1_500_000_000
landlord_std = 500_000_000

budget_threshold = 2_000_000_000

#Run Monte Carlo Trials
N = 1000000
grocery = np.random.normal(grocery_mean, grocery_std, N)
bus = np.random.normal(free_bus_mean, free_bus_std, N)
rent = np.random.normal(rent_freeze_mean, rent_freeze_std, N)
admin = np.random.normal(admin_mean, admin_std, N)

landlord = (np.random.rand(N) < landlord_prob).astype(float) * (np.random.normal(landlord_mean, landlord_std, N))
gross_city_cost = grocery + admin + landlord + rent + bus
mean_net = np.mean(gross_city_cost)
median_net = np.median(gross_city_cost)
p5 = np.percentile(gross_city_cost, 5)
p95 = np.percentile(gross_city_cost, 95)
prob_feasible = np.mean(gross_city_cost <= budget_threshold)
prob_self_funded = np.mean(gross_city_cost <= 0)

# Print out Scores
print(f"Mean Net Annual Cost: ${mean_net:,.0f}")
print(f"Median Net Annual Cost: ${median_net:,.0f}")
print(f"5th Percentile: ${p5:,.0f}")
print(f"95th Percentile: ${p95:,.0f}")
print(f"Probability Affordable (≤ ${budget_threshold:,.0f}): {prob_feasible:.2%}")
print(f"Probability Self-Funded (≤ $0): {prob_self_funded:.2%}")
#%%
# Graphed Results
plt.figure(figsize=(8,5))
plt.hist(gross_city_cost, bins=50, color='green')
plt.xlabel("Gross Annual City Cost ($)")
plt.ylabel("Frequency")
plt.title("Monte Carlo Distribution of Gross Annual Cost")
plt.axvline(x=2_000_000_000, color='red')
plt.tight_layout()
plt.savefig("gross_annual_city_cost_distribution.png")
plt.show()
# %%