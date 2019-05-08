# IBM Gate Circuit to DWave Annealer Embedding Translator

This project is described in detail in the paper "Automatically Translating Quantum Programs from a Subset of Common Gates to An Adiabatic Representation"

-----------------------------------------------------------------------------

## Running Qiskit scripts with the converter:

1) To run examples, add base directory of repository to ```PYTHONPATH```, i.e. go to repository directory and type

      ```export PYTHONPATH=`pwd` ```

2) Set token variable at the top of the ```execute``` function in ```converter/qiskit/tools/_compiler.py``` to your Dwave token as a string, i.e.

      ```token = 'DEV-########################################'```

      If this variable is not set you will be prompted to enter it when the script is run.

3) In qiskit scripts to be translated, change the line ```import qiskit``` to ```import converter.qiskit```


4) Command line flags:

      ```sim``` flag - Run ExactSolver simulation of embedding
        
        python example_script.py sim
     
      NOTE: ExactSolver simulations of embeddings comprised of more than 19 qubits is not recommended. It can take a very long time or cause your computer to crash. If simulation of an embedding with more than 19 qubits is attempted a warning is issued.
     
      ```run``` flag - Run generated embedding on DWave (this is default - no flag required) 
        
        python example_script.py run
        
      ```source``` flag -  Generate DWave Ocean script.
        
        python example_script.py source
       
      Running a script with the ```source``` flag will generate a Dwave ocean file, ```example_script_Dwave.py``` that can be used to debug or otherwise improve the generated embedding.
        
      Any combination of these flags will work 
        
        python example_script.py run sim source
