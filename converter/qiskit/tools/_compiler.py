

from copy import deepcopy
import uuid
import logging
import sys

#from converter.qiskit import transpiler
#from converter.qiskit.transpiler._passmanager import PassManager
#from converter.qiskit.qobj import Qobj, QobjConfig, QobjExperiment, QobjItem, QobjHeader
#from converter.qiskit.unroll import DagUnroller, JsonBackend
#from converter.qiskit.transpiler._parallel import parallel_map
import dimod
from dwave.system.samplers import DWaveSampler
from dwave.cloud.exceptions import SolverOfflineError
from dwave.system.composites import EmbeddingComposite
import minorminer

def compile(circuits, backend,
            config=None, basis_gates=None, coupling_map=None, initial_layout=None,
            shots=1024, max_credits=10, seed=None, qobj_id=None, hpc=None,
            skip_transpiler=False, seed_mapper=None):
    pass










def dags_2_qobj(dags, backend_name, config=None, shots=None,
                max_credits=None, qobj_id=None, basis_gates=None, coupling_map=None,
                seed=None):
    pass










def _dags_2_qobj_parallel(dag, config=None, basis_gates=None, coupling_map=None):
    pass





def execute(circuit, backend = None,
            config=None, basis_gates=None, coupling_map=None, initial_layout=None,
            shots=1024, max_credits=10, seed=None, qobj_id=None, hpc=None,
            skip_transpiler=False, seed_mapper=None):

    #token = 'DEV-beb5d0babc40334f66b655704f1b5315917b4c41'
    token = ''

    outputs = list()
    inputs = list()
    
    qubit_biases = circuit.annealergraph.qubitbiases
    coupler_strengths = circuit.annealergraph.couplerstrengths

    print("\nDone building embedding.")
    print("\t# qubits: ", len(qubit_biases))
    print("\t# couplers: ", len(coupler_strengths))
    print("\t# non-gate couplers: {}\n".format(len(coupler_strengths)-circuit.annealergraph.numgatecouplers))

    for qubit in circuit.annealergraph.qubits.keys():
        if isinstance(circuit.annealergraph.qubits[qubit], dict):
            if circuit.annealergraph.qubits[qubit]['measured'] == True:
                outputs.append(circuit.annealergraph.qubits[qubit]['components'][-1])
                # can't omit output bit from being included as input, but is its put
                # first in the list, it will be zero the top portion of the readout
                ans = input("Constrain input of measured qubit {} to be 0 (y/n)? ".format(qubit))
                if ans == 'y':
                    change = circuit.annealergraph.qubits[qubit]['components'][0]
                    circuit.annealergraph.qubitbiases[change] = circuit.annealergraph.qubitbiases[change] + 5
                else:
                    inputs.append(circuit.annealergraph.qubits[qubit]['components'][0])

    for qubit in circuit.annealergraph.qubits.keys():
        if isinstance(circuit.annealergraph.qubits[qubit], dict):
            if circuit.annealergraph.qubits[qubit]['measured'] == False:
                ans = input("Constrain input of unmeasured qubit {} to be 0 (y/n)? ".format(qubit))
                if ans == 'y':
                    change = circuit.annealergraph.qubits[qubit]['components'][0]
                    circuit.annealergraph.qubitbiases[change] = circuit.annealergraph.qubitbiases[change] + 5
                else:
                    inputs.append(circuit.annealergraph.qubits[qubit]['components'][0])
            
    circuit.annealergraph.print_chimera_graph_to_file()
 
    if token == '':
        token = input('Please set token variable at the top of the "execute" function in /converter/qiskit/tools/_compiler.py to your DWave token as a string. Or, you can enter it here: ')

    samp = input("\nHow many samples? ")
    samp = int(samp)

    if 'source' in sys.argv:
        writedwavesource(circuit, token, samp)

    if ('run' in sys.argv) or (len(sys.argv)==1):
        sampler = circuit.annealergraph.sampler
        bqm = dimod.BinaryQuadraticModel(qubit_biases, coupler_strengths, 0, dimod.BINARY)
        print(qubit_biases)
        print(coupler_strengths)
        kwargs = {}
        if 'num_reads' in sampler.parameters:
            kwargs['num_reads'] = samp
        if 'answer_mode' in sampler.parameters:
            kwargs['answer_mode'] = 'histogram'
        #if 'annealing_time' in sampler.parameters:
        #    kwargs['annealing_time'] = 100
        print("\nRunning...")
    
        response = sampler.sample(bqm, **kwargs)

        sampler.client.close()
        print("Done.")
        print(response.data)

        groundstate = 1000000
        for sample, energy in response.data(['sample','energy']):
            if energy<groundstate:
                groundstate = round(energy,1)
        print("Ground State: ", groundstate)

        function = list()
        for sample, energy in response.data(['sample', 'energy']):
            if round(energy,1) == groundstate:
                print(sample, round(energy,1))
                row = []
                for inp in inputs:
                    row.append(sample[inp])
                for outp in outputs:
                    row.append(sample[outp])
                function.append(row)
        print('\n')
    
        function.sort()
        for i in range(len(function)):
            print(function[i])

    if 'sim' in sys.argv:
        ans = 'y'
        if len(circuit.annealergraph.qubitbiases) > 19:
            ans = input("WARNING: Embedding uses {} qubits - ExactSolver simulation could take way too long or cause your computer to crash. Type 'y' to continue: ".format(len(circuit.annealergraph.qubitbiases)))
        
        if ans == 'y' or ans == 'Y':
            print("Simulating problem with {} qubits".format(len(circuit.annealergraph.qubitbiases)))
            qubit_biases = circuit.annealergraph.qubitbiases
            coupler_strengths = circuit.annealergraph.couplerstrengths
        
            print("\nQubit Biases:")
            for key in qubit_biases.keys():
                print(key, "\t", qubit_biases[key])
            print("\nCoupler Strengths:")
            for key in coupler_strengths.keys():
                print(key, "\t", coupler_strengths[key])
            print("\n")

            bqm = dimod.BinaryQuadraticModel(qubit_biases, coupler_strengths, 0, dimod.BINARY)
            sampler = dimod.ExactSolver()
    
            response = sampler.sample(bqm)

            groundstate = 1000000
            for sample, energy in response.data(['sample','energy']):
                if energy<groundstate:
                    groundstate = round(energy,1)
        
            print("Ground State: ", groundstate)
            function = list()
            for sample, energy in response.data(['sample', 'energy']):
                if round(energy,1) == groundstate:
                    print(sample, round(energy,1))
                    row = []
                    for inp in inputs:
                        row.append(sample[inp])
                    for outp in outputs:
                        row.append(sample[outp])
                    function.append(row)
            print('\n')

            function.sort()
            for i in range(len(function)):
                print(function[i])
        else:
            print('Quitting.')
    
def writedwavesource(circ, token, samp):
    print('in write source')
