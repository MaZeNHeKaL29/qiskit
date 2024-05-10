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



def phase_flip_gate_zero_qubit():
    qr = qiskit.QuantumRegister(1)
    cr = qiskit.ClassicalRegister(1)
    circuit = qiskit.QuantumCircuit(qr, cr)
    circuit.z(qr)
    circuit.measure(qr,cr) # Collapses qubit to either 1 or 0 w/ equal prob.
    return circuit


def phase_flip_gate_one_qubit():
    qr = qiskit.QuantumRegister(1)
    cr = qiskit.ClassicalRegister(1)
    circuit = qiskit.QuantumCircuit(qr, cr)
    circuit.x(qr)
    circuit.z(qr)
    circuit.measure(qr,cr) # Collapses qubit to either 1 or 0 w/ equal prob.
    return circuit