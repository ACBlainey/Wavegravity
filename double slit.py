import numpy as np
import matplotlib.pyplot as plt

# Parameters from thesis
c = 3e8  # m/s
eta = 1.1e-30  # s^-1 * kg
a = 1.618  # golden ratio
L = 1  # screen distance, m
d = 0.001  # slit separation, m (1 mm for ~0.5 mm fringes)
k = 1.06e-3  # empirical factor to match Table \ref{tab:slit}

# Materials from Table \ref{tab:slit}
materials = {
    'Silicon': 4.7e-26,  # kg
    'Gold': 3.3e-25,
    'Graphene': 2.0e-26
}

# Screen positions
x = np.linspace(-0.005, 0.005, 1000)  # m

plt.figure(figsize=(8, 5))
for mat, m_i in materials.items():
    # Spin rate: omega_i = eta / m_i
    omega_i = eta / m_i  # s^-1
    
    # Adjust n per material to target lambda_eff ~500 nm
    target_lambda = 5e-7  # m
    S_n = (c * m_i) / (eta * target_lambda)  # base S_n
    n = np.log(S_n) / np.log(a)  # e.g., n ~ 92.87 for silicon
    
    # Effective wavelength with correction: lambda_eff = k * (c * m_i) / (eta * a^n)
    lambda_eff = k * (c * m_i) / (eta * a**n)
    
    # Fringe spacing: delta_x = lambda_eff * L / d
    delta_x = lambda_eff * L / d
    
    # Intensity: I ~ cos^2(pi * d * x / (lambda_eff * L))
    phase = np.pi * d * x / (lambda_eff * L)
    intensity = np.cos(phase)**2
    
    print(f"{mat}: m_i={m_i:.2e} kg, omega_i={omega_i:.2e} s^-1, "
          f"lambda_eff={lambda_eff:.2e} m, delta_x={delta_x*1e3:.2f} mm")
    
    # Plot
    plt.plot(x * 1e3, intensity, label=f"{mat} (Δx={delta_x*1e3:.2f} mm)")

plt.xlabel('Screen Position (mm)')
plt.ylabel('Intensity')
plt.title('Double-Slit Interference Patterns by Material')
plt.legend()
plt.grid(True)
plt.show()