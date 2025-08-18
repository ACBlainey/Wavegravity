import numpy as np
from scipy.stats import ttest_rel
import pandas as pd

# Load orbital data
data = pd.read_csv('../data/orbital_data.csv')

# Compute MAPE
data['MAPE'] = np.abs((data['Observed_Value'] - data['Predicted_Value']) / data['Observed_Value']) * 100
mean_mape = data['MAPE'].mean()
std_mape = data['MAPE'].std()
print(f"Wave-Based MAPE: {mean_mape:.2f}% (SD {std_mape:.2f}%)")

# Simulated GR and MOND errors (from Table 4)
gr_errors = [2.3, 2.1, 3.6, 3.2, 2.3, 2.1, 3.6, 2.5, 2.5]  # Approximate for 9 systems
mond_errors = [1.6, 1.5, 2.0, 1.8, 1.6, 1.5, 2.0, 1.7, 1.7]
wave_errors = data['MAPE'].values

# Paired t-tests
t_stat_gr, p_value_gr = ttest_rel(wave_errors, gr_errors)
t_stat_mond, p_value_mond = ttest_rel(wave_errors, mond_errors)
print(f"t-test vs GR: t = {t_stat_gr:.2f}, p = {p_value_gr:.2e}")
print(f"t-test vs MOND: t = {t_stat_mond:.2f}, p = {p_value_mond:.2e}")