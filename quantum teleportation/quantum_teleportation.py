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




def quantum_teleporte(theta):

    qr = qiskit.QuantumRegister(3)

    cr = qiskit.ClassicalRegister(3)

    circuit = qiskit.QuantumCircuit(qr,cr)

    circuit.h(0)

    circuit.rz(theta,0)

    circuit.barrier()

    circuit.h(1)

    circuit.cx(1,2)

    circuit.barrier()

    circuit.cx(0,1)

    circuit.h(0)

    circuit.barrier()

    circuit.measure(qr[0], cr[0])

    circuit.measure(qr[1], cr[1])

    circuit.barrier()

    circuit.cx(1,2)

    circuit.cz(0,2)

    circuit.measure(qr[2], cr[2])

    return circuit
    