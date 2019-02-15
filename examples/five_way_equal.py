from converter.qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, execute
from sys import argv

def equal_nway(qx, qy, temp, qz, n, qc):

    if n == 1:
        #if n is 1, we directly do the comparison onto qz without any temporary bits
        qc.cx(temp[0],qz[0])
        qc.ccx(qx[0],temp[0],qz[0])
        qc.ccx(qy[0],temp[0],qz[0])

    else:
        #comparing the MSB
        t = QuantumRegister(1)
        qc.add(t)
        qc.cx(temp[0],t[0])
        qc.ccx(qx[n-1],temp[0],t[0])
        qc.ccx(qy[n-1],temp[0],t[0])
        equal_nway(qx,qy,t,qz,n-1,qc)

        #reversing t
        #qc.ccx(qy[n-1],temp[0],t[0])
        #qc.ccx(qx[n-1],temp[0],t[0])
        #qc.cx(temp[0],t[0])
    return qc

#5 inputs with  n-bits each : to be compared
n = 5

#output bit: function XORed onto this
qz = QuantumRegister(1)
cz = ClassicalRegister(1)

#output bit: function XORed onto this
tmp = QuantumRegister(1)
tmpc = ClassicalRegister(1)

qin1 = QuantumRegister(n)
cin1 = ClassicalRegister(n)
qin2 = QuantumRegister(n)
cin2 = ClassicalRegister(n)

#beginning of the circuit
circuit = QuantumCircuit(qin1,qin2,qz,tmp,cin1,cin2,cz,tmpc)

#initialize temp
circuit.x(tmp)

#actually compare
equal_nway(qin1, qin2, tmp, qz, n, circuit)

#reversing tmp
circuit.x(tmp)

#circuit.measure(qin1, cin1)
#circuit.measure(qin2, cin2)

circuit.measure(qz, cz)

execute(circuit)
