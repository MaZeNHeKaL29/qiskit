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



def oracleBalance1(qr):
    qr.cx(0,1)
    qr.barrier()
    
    return qr


def oracleBalance2(qr):
    qr.x(1)
    qr.cx(0,1)
    qr.barrier()
    
    return qr



def oracleConstant1(qr):
    
    qr.x(1)
    qr.barrier()
    
    return qr 


def oracleConstant2(qr):
    
    qr.barrier()
    
    return qr 



def deutsch_algorithm(oracle):

    qr = qiskit.QuantumRegister(2)
    cr = qiskit.ClassicalRegister(1)
    circuit = qiskit.QuantumCircuit(qr, cr)

    
    circuit.x(1)

    circuit.h(0)

    circuit.h(1)

    circuit.barrier()

    circuit = oracle(circuit)

    circuit.h(0)

    circuit.barrier()

    circuit.measure(qr[0],cr)

    return circuit

