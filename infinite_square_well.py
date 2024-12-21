import numpy as np
import matplotlib.pyplot as plt

# Constants
L = 1.0  # Well length
hbar = 1.0545718e-34  # Reduced Planck's constant (J·s)
m = 9.10938356e-31  # Mass of an electron (kg)
def wavefunction(n, x, L):
    """Wavefunction for the nth energy level in an infinite square well."""
    return np.sqrt(2 / L) * np.sin(n * np.pi * x / L)

def energy(n, L):
    """Energy for the nth energy level in an infinite square well."""
    return (n**2 * np.pi**2 * hbar**2) / (2 * m * L**2)
x = np.linspace(0, L, 1000)  # High-resolution spatial grid
n_values = [1, 2, 3]  # Quantum numbers to visualize
plt.figure(figsize=(10, 6))

for n in n_values:
    psi = wavefunction(n, x, L)
    plt.plot(x, psi, label=f"n={n}")

plt.title("Wavefunctions for a 1D Infinite Square Well")
plt.xlabel("Position x (m)")
plt.ylabel("Wavefunction ψ(x)")
plt.legend()
plt.grid()
plt.show()
plt.figure(figsize=(10, 6))

for n in n_values:
    psi = wavefunction(n, x, L)
    prob_density = psi**2
    plt.plot(x, prob_density, label=f"n={n}")

plt.title("Probability Densities for a 1D Infinite Square Well")
plt.xlabel("Position x (m)")
plt.ylabel("Probability Density |ψ(x)|²")
plt.legend()
plt.grid()
plt.show()

for n in n_values:
    psi = wavefunction(n, x, L)
    normalization = np.trapz(psi**2, x)
    print(f"Normalization for n={n}: {normalization}")

    plt.savefig(f"wavefunctions_{L}m.png")


