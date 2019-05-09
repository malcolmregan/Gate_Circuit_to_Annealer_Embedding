# IBM Gate Circuit to DWave Annealer Embedding Translator

This project is described in detail in the paper "Automatically Translating Quantum Programs from a Subset of Common Gates to an Adiabatic Representation" by Malcolm Regan, Brody Eastwood, Mahita Nagabhiru, and Frank Mueller.

-----------------------------------------------------------------------------

## Running Qiskit scripts with the converter

1) To run examples, add base directory of repository to ```PYTHONPATH```, i.e. go to repository directory and type

      ```export PYTHONPATH=`pwd` ```

2) Set token variable at the top of the ```execute``` function in ```converter/qiskit/tools/_compiler.py``` to your Dwave token as a string, i.e.

      ```token = 'DEV-########################################'```

      If this variable is not set you will be prompted to enter it when the script is run.

3) In Qiskit scripts to be translated, change the line ```import qiskit``` to ```import converter.qiskit```


4) Command line flags:

      ```sim``` flag - Run ExactSolver simulation of embedding
        
        python example_script.py sim
     
      NOTE: ExactSolver simulations of embeddings comprised of more than 19 qubits is not recommended. It can take a very long time or cause your computer to crash. If simulation of an embedding with more than 19 qubits is attempted a warning is issued.
     
      ```run``` flag - Run generated embedding on DWave (this is default - no flag required) 
        
        python example_script.py run
        
      ```source``` flag -  Generate DWave Ocean script.
        
        python example_script.py source
       
      Running a script with the ```source``` flag will generate a Dwave ocean file, ```example_script_Dwave.py```, that can be used to debug or otherwise improve the generated embedding.
        
      Any combination of these flags will work 
        
        python example_script.py run sim source


-----------------------------------------------------------------------------

## Example

The  sample  Qiskit  program  below  defines  a  1-qubit  adder  circuit.  Note  that  the  imports  have  been  modified  to  indicate  the  use of the gate-circuit-to-annealer embedding translator (i.e., ’converter.qiskit’ replaces ’qiskit’). This is the only modification that is required to run a Qiskit program with the translator code.


```
from converter.qiskit import QuantumRegister, ClassicalRegister
from converter.qiskit import QuantumCircuit, execute

# Input Registers: a = qi[0]; b = qi[1]; ci = qi[2]
qi = QuantumRegister(3)
ci = ClassicalRegister(3)

# Output Registers: s = qo[0]; co = qo[1]
qo = QuantumRegister(2)
co = ClassicalRegister(2)

circuit = QuantumCircuit(qi,qo,ci,co)

# Define adder circuit

for idx in range(3):
      circuit.ccx(qi[idx], qi[(idx+1)%3], qo[1])
for idx in range(3):
      circuit.cx(qi[idx], qo[0])

circuit.measure(qo, co)

# Run
execute(circuit)
```

The measure method is used as an indication that a given qubit register isconsidered a circuit output, which aids in organizing the results. When  the execute method  is called,  the  user  is  prompted  to  answer  whether  or  not  initial  values  of  qubits should be constrained to zero. Qubits are identified using Qiskit’s naming scheme in the program and by the order with which they appeared in the initialization of the Quantum Circuit. In the case of the 1-qubit adder above, the user would like for the initial state of the sum and carry-out qubits be constrained to zero, and so responds to the prompts from execute as follows:

```
Constrain input of measured qubit q1_0 to be 0 (y/n)? y
Constrain input of measured qubit q1_1 to be 0 (y/n)? y
Constrain input of unmeasured qubit q0_0 to be 0 (y/n)? n
Constrain input of unmeasured qubit q0_1 to be 0 (y/n)? n
Constrain input of unmeasured qubit q0_2 to be 0 (y/n)? n
```



-----------------------------------------------------------------------------

## Notes



-----------------------------------------------------------------------------

## To Do
