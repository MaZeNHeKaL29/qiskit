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


def get_random_int5():
    set_qubits(5)

    
    new_circuit = qiskit.transpile(circuit, backend)
    job = backend.run(new_circuit)

    result = job.result()

    str = ''

    for i in range(1):
        str += next(iter(result.get_counts()))

    decimal_value = int(str, 2)

    return str,decimal_value


def get_random_int8():
    set_qubits(8)

    
    new_circuit = qiskit.transpile(circuit, backend)
    job = backend.run(new_circuit)

    result = job.result()

    str = ''

    for i in range(1):
        str += next(iter(result.get_counts()))

    decimal_value = int(str, 2)

    return str,decimal_value



def get_random_int16():
    set_qubits(8)


    new_circuit = qiskit.transpile(circuit, backend)
    job = backend.run(new_circuit)

    result = job.result()

    str = ''

    for i in range(2):
        str += next(iter(result.get_counts()))

    decimal_value = int(str, 2)

    return str,decimal_value



def get_random_int32():
    set_qubits(8)


    new_circuit = qiskit.transpile(circuit, backend)
    job = backend.run(new_circuit)

    result = job.result()

    str = ''

    for i in range(4):
        str += next(iter(result.get_counts()))

    decimal_value = int(str, 2)

    return str, decimal_value



def get_random_int64():
    set_qubits(8)


    new_circuit = qiskit.transpile(circuit, backend)
    job = backend.run(new_circuit)

    result = job.result()

    str = ''

    for i in range(8):
        str += next(iter(result.get_counts()))

    decimal_value = int(str, 2)

    return str,decimal_value