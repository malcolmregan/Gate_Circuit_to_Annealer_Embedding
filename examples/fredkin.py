from converter.qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, execute

c = QuantumRegister(1) 
t1 = QuantumRegister(1)
t2 = QuantumRegister(1)
cc = ClassicalRegister(1)
t1c = ClassicalRegister(1)
t2c = ClassicalRegister(1)

circuit = QuantumCircuit(c,t1,t2,cc,t1c,t2c)

circuit.cswap(c[0],t1[0],t2[0])

circuit.measure(c,cc)
circuit.measure(t1, t1c)
circuit.measure(t2, t2c)

execute(circuit)
