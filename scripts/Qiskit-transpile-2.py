from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.quantum_info.operators import Operator
from qiskit.compiler import transpile
from qiskit import Aer, execute, IBMQ
import pdb 
import numpy as np 
# you can define you own untary matrix
a = 0.21871
U = np.eye(4)
U[1,1] = np.sqrt(a)
U[1,3] = np.sqrt(1-a)
U[2,2] = -1
U[3,1] = np.sqrt(1-a)
U[3,3] = -np.sqrt(a)

print("=================the original matrix=============")
print(U)

q = QuantumRegister(2)
circ = QuantumCircuit(q)

U_op = Operator(U)
circ.unitary(U_op,q)

print("================direct draw without decomposition==============")
print(circ.draw())


basis_gates = ['u1', 'u2', 'u3', 'cx']
simulator = Aer.get_backend('qasm_simulator')

# elementary gates output
print("================elementary gate decomposition==============")
circ_trans = transpile(circ,simulator, basis_gates=basis_gates)
print(circ_trans.draw())

circ_trans.draw(filename='C:\\users\\zixua\\documents\\research 2017\\project 2\\joint project with yale july 2021\\IBM simulator and device discussions\\circuit_simple',output='mpl')


