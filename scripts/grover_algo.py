from qiskit import *
from qiskit.quantum_info import Statevector 
from qiskit.visualization import plot_bloch_multivector
from qiskit.providers.basic_provider import BasicSimulator

# qc = QuantumCircuit(1,1)
# qc.draw(output='mpl')
# qc.x(0)

# init_state = Statevector(qc)
# print(init_state)
# plot_bloch_multivector(init_state)

# qc.x(0)
# qc.h(0)
# qc.draw(output='mpl')

# h_state = Statevector(qc)
# print(h_state)

# plot_bloch_multivector(h_state)

# qc.measure(0,0)
# qc.draw(output='mpl')

# from qiskit.providers.basic_provider  import BasicSimulator
# from qiskit.visualization import plot_histogram

# backend = BasicSimulator()
# result = backend.run(qc, shots=2000).result()
# counts = result.get_counts(0)
# plot_histogram(counts)






# -------------------------------------------------------------------------------------
from qiskit.providers.basic_provider import BasicProvider
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram
import numpy as np

def grover_oracle(qc, qubits):
    qc.cz(qubits[0], qubits[1])

def grover_diffusion(qc, qubits):
    qc.h(qubits)
    qc.x(qubits)
    qc.h(qubits[1])
    qc.cz(qubits[0], qubits[1])
    qc.h(qubits[1])
    qc.x(qubits)
    qc.h(qubits)

def grover_algorithm():
    qc = QuantumCircuit(2)
    qc.h([0, 1])
    grover_oracle(qc, [0, 1])
    grover_diffusion(qc, [0, 1])
    qc.measure_all()
    return qc

qc = grover_algorithm()
backend = BasicSimulator()
new_circuit = transpile(qc, backend)
result = backend.run(qc, shots=2000).result()
counts = result.get_counts(0)
plot_histogram(counts)
