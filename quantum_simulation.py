# Importation des modules nécessaires de Qiskit
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import os

# Crée un circuit quantique avec 2 qubits et 2 bits classiques
circuit = QuantumCircuit(2, 2)

# Applique une porte Hadamard sur le premier qubit (Q0)
circuit.h(0)

# Applique une porte CNOT (intrication) entre le qubit 0 et le qubit 1
circuit.cx(0, 1)

# Mesure les qubits et stocke les résultats dans les bits classiques
circuit.measure([0, 1], [0, 1])

# Affiche le circuit pour visualiser la séquence d'opérations
print(circuit.draw())

# Utilise le simulateur AerSimulator pour simuler le circuit
simulator = AerSimulator()

# Transpile le circuit pour l'adapter au simulateur
compiled_circuit = transpile(circuit, simulator)

# Exécute le circuit sur le simulateur
sim_result = simulator.run(compiled_circuit).result()

# Obtient les comptages des résultats des mesures
counts = sim_result.get_counts()

# Affiche les résultats dans la console
print("\nRésultats de la simulation : ", counts)

# Génère l'histogramme des résultats
histogram = plot_histogram(counts)

# Définir le chemin vers le dossier "Mes téléchargements"
downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")

# Définir le nom du fichier pour l'histogramme
file_path = os.path.join(downloads_folder, "quantum_histogram.png")

# Enregistrer l'histogramme dans le dossier "Mes téléchargements"
histogram.savefig(file_path)

# Afficher l'histogramme
histogram.show()

print(f"Histogramme enregistré dans {file_path}")
