import numpy as np
import matplotlib.pyplot as plt

# Parameters from thesis
c = 3e8  # m/s
eta = 1.1e-30  # s^-1 * kg
a = 1.618  # golden ratio
L = 1  # screen distance, m
d = 0.001  # slit separation, m (adjusted to 1 mm for realistic 0.5 mm fringes)
x = np.linspace(-0.005, 0.005, 1000)  # screen positions, m

# Materials from Table \ref{tab:slit}
materials = {
    'Silicon': 4.7e-26,  # kg
    'Gold': 3.3e-25,
    'Graphene': 2.0e-26  # approx. carbon atom mass
}

for mat, m_i in materials.items():
    # Calculate n for lambda_eff ~500 nm (base for silicon)
    target_lambda = 5e-7  # m
    S_n = (c * m_i) / (eta * target_lambda)  # scales with m_i since omega_i = eta / m_i, lambda_eff ~ m_i
    n = np.log(S_n) / np.log(a)
    
    # Use n ~93 for silicon; scale lambda_eff proportionally for others
    lambda_eff = (c * m_i) / (eta * a**93)  # fixed n, lambda_eff ~ m_i
    
    # Fringe spacing
    delta_x = lambda_eff * L / d
    print(f"{mat}: lambda_eff = {lambda_eff:.2e} m, Delta x = {delta_x:.2e} m")
    
    # Intensity (standard double-slit approximation)
    phase = np.pi * d * x / (lambda_eff * L)
    intensity = np.cos(phase)**2  # simplified envelope=1 for illustration
    
    # Plot (in practice, save/show; here, describe)
    # plt.plot(x * 1e3, intensity, label=mat)

# Example output for silicon: lambda_eff = 4.71e-07 m, Delta x = 4.71e-04 m (~0.47 mm, close to 0.5 mm)

# To visualize fringes, peaks approx. every delta_x ~0.5 mm