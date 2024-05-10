import qiskit

import qiskit.visualization

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 

from qiskit_ibm_runtime import QiskitRuntimeService
 
def start_service(token_given : str = None):

    global service

    # Save an IBM Quantum account and set it as your default account.
    QiskitRuntimeService.save_account(channel="ibm_quantum", token= token_given, set_as_default=True, overwrite=True)
 
    # Load saved credentials
    service = QiskitRuntimeService()



def set_backend():

    global service

    global backend

    backend = service.backend("ibmq_qasm_simulator")



def bell_state_gate(q1, q2):
    if(q1 != 0 and q1 != 1):
        raise ValueError("q1 must be 0 or 1")
    if(q2 != 0 and q2 != 1):
        raise ValueError("q2 must be 0 or 1")
    qr = qiskit.QuantumRegister(2)
    cr = qiskit.ClassicalRegister(2)
    circuit = qiskit.QuantumCircuit(qr, cr)
    if(q1 == 1):
        circuit.x(0)
    if(q2 == 1):
        circuit.x(1)

    circuit.h(0)
    circuit.cx(0,1)
        
    circuit.measure(qr,cr) # Collapses qubit to either 1 or 0 w/ equal prob.
    return circuit