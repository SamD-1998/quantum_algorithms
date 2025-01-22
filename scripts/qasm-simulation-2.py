from decomposition import *

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit import Aer, execute

from qiskit.tools.visualization import plot_histogram, plot_state_city
import csv                      #file format management
import time   
import pdb 
import scipy.linalg as la       #linear algebra
import numpy as np             
# you can define you own untary matrix

start_time = time.time()

ga = 1.52e9
p1 = 0.5
p2 = 0.5

rho0 = []
rho1 = []

q = QuantumRegister(2)
c = ClassicalRegister(2)

for t in range(1,1001,10):

	a = np.exp(-ga*t*1e-12)
	
	UM0 = np.eye(4)
	UM0[1,1] = np.sqrt(a)
	UM0[1,3] = np.sqrt(1-a)
	UM0[2,2] = -1.0
	UM0[3,1] = np.sqrt(1-a)
	UM0[3,3] = -np.sqrt(a)
	
	UM1 = np.zeros((4,4),"complex")
	UM1[0,1] = np.sqrt(1-a)
	UM1[0,2] = np.sqrt(a)
	UM1[1,3] = 1.0
	UM1[2,0] = 1.0
	UM1[3,1] = np.sqrt(a)
	UM1[3,2] = -np.sqrt(1-a)
	#pdb.set_trace()

	circ1 = QuantumCircuit(q,c)
	circ1.h(0)
	circ10 = general_implement(UM0,circ1,q)
	circ10.measure(q,c)
	
	circ1 = QuantumCircuit(q,c)
	circ1.h(0)
	circ11 = general_implement(UM1,circ1,q)
	circ11.measure(q,c)
	
	circ2 = QuantumCircuit(q,c)
	circ2.x(0)
	circ20 = general_implement(UM0,circ2,q)
	circ20.measure(q,c)
	
	circ2 = QuantumCircuit(q,c)
	circ2.x(0)
	circ21 = general_implement(UM1,circ2,q)
	circ21.measure(q,c)
#pdb.set_trace()
# elementary gates output
	
	simulator = Aer.get_backend('qasm_simulator')
	# Execute and get counts
	result10 = execute(circ10,simulator).result()
	counts10 = result10.get_counts(circ10)
	
	result11 = execute(circ11,simulator).result()
	counts11 = result11.get_counts(circ11)
	
	result20 = execute(circ20,simulator).result()
	counts20 = result20.get_counts(circ20)
	
	result21 = execute(circ21,simulator).result()
	counts21 = result21.get_counts(circ21)
	
	sq0 = p1*counts10.get('00',0)/1024 + p1*counts11.get('00',0)/1024 + p2*counts20.get('00',0)/1024 + p2*counts21.get('00',0)/1024
	sq1 = p1*counts10.get('01',0)/1024 + p1*counts11.get('01',0)/1024 + p2*counts20.get('01',0)/1024 + p2*counts21.get('01',0)/1024
	
	rho0.append(np.real(sq0))
	rho1.append(np.real(sq1))
	#pdb.set_trace()
with open("C:\\Users\\zixua\\Documents\\Research 2017\\Project 2\\joint project with yale july 2021\\IBM simulator and device discussions\\data.csv", "w", newline='') as f:
    wr = csv.writer(f)
    for i in range(len(rho0)):
        wr.writerow([i, rho0[i], rho1[i]])

print("--- %s seconds ---" % (time.time() - start_time))
