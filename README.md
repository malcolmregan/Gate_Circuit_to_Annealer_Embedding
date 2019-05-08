# Gate_Circuit_to_Annealer_Embedding

To run examples, add base directory of repository to PYTHONPATH, i.e.

```export PYTHONPATH=`pwd` ```

Set token variable at the top of the ```execute``` function in ```converter/qiskit/tools/_compiler.py``` to your Dwave token asa string, i.e.

  ```token = 'DEV-######## numbers_and_letters ###########'```

If this variable is not set you will be prompted to enter it when the script is run.

Command line flags:
  1) Run ExactSolver simulation of embedding
        ```python example_script.py sim```
     
     ExactSolver simulations of embeddings comprised of more than 19 qubits is not recommended. It can take a very long time or cause your computer to crash. If simulation of an embedding with more than 19 qubits is
     
  3) Run generated embedding on DWave (this is default - no flag required) 
        ```python example_script.py run'''
  3) Generate DWave Ocean script for debugging.
        ```python example_script.py source```
        
Any combination of these flags will work 
        ```python example_script.py run sim source```
