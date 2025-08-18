import numpy as np
from scipy.optimize import minimize

# Parameters from thesis
G = 6.674e-11  # Gravitational constant (m^3 kg^-1 s^-2)
c = 3e8  # Speed of light (m/s)
m_sun = 1.989e30  # Sun mass (kg)

# Sample data from orbital_data.csv (Mercury as example)
a_mercury = 0.387 * 1.496e11  # Semi-major axis (m)
v_observed = 47.87e3  # Observed velocity (m/s)

# Objective function: Minimize error in force prediction
def objective(params):
    eta, k_s, b_star = params
    # Simplified force model: F = k_s * m * omega_i^2 / r^2, omega_i = eta / m_i
    m_i = 4.7e-26  # Silicon mass (kg)
    omega_i = eta / m_i
    F_pred = k_s * m_sun * omega_i**2 / a_mercury**2
    F_obs = G * m_sun * 3.3e23 / a_mercury**2  # Newtonian force for Mercury
    return (F_pred - F_obs)**2

# Initial guess
initial_params = [1.1e-30, 9.4e30, 1e-2]  # eta, k_s, b_star

# Optimize
result = minimize(objective, initial_params, method='Nelder-Mead')
eta_opt, k_s_opt, b_star_opt = result.x

print(f"Optimized parameters: eta = {eta_opt:.2e}, k_s = {k_s_opt:.2e}, b_star = {b_star_opt:.2e}")