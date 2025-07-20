import pandas as pd
from scipy.stats import pearsonr

# Manually extracted relevant columns from the SQL INSERT statements
data = {
    "Promo_Spend": [2141, 1500, 2622, 1638, 1128, 1915, 2543, 843, 579, 806, 971],
    "Avg_Basket": [67, 78, 47, 67, 66, 50, 21, 21, 80, 61, 48],
    "Returns": [9, 3, 0, 7, 4, 2, 5, 10, 4, 0, 1]
}

df = pd.DataFrame(data)

# Calculate Pearson correlation coefficients
corr_1 = pearsonr(df["Promo_Spend"], df["Avg_Basket"])[0]
corr_2 = pearsonr(df["Promo_Spend"], df["Returns"])[0]
corr_3 = pearsonr(df["Avg_Basket"], df["Returns"])[0]

# Store results
correlations = {
    "Promo_Spend-Avg_Basket": corr_1,
    "Promo_Spend-Returns": corr_2,
    "Avg_Basket-Returns": corr_3
}

# Determine the strongest correlation (by absolute value)
strongest_pair = max(correlations.items(), key=lambda x: abs(x[1]))

# Format as required JSON
result_json = {
    "pair": strongest_pair[0],
    "correlation": round(strongest_pair[1], 2)
}

result_json
