import numpy as np

def initialize_quantum_state(num_qubits, seed=None):
    # シード値を設定することでランダムな状態の再現性を確保
    if seed is not None:
        np.random.seed(seed)
    state = np.random.rand(2**num_qubits) + 1j * np.random.rand(2**num_qubits)
    state = state / np.linalg.norm(state)
    return state

def calculate_conjugate(state):
    return np.conjugate(state)

def main():
    num_qubits = 20
    seed = 42  # 再現性のためのシード値

    quantum_state = initialize_quantum_state(num_qubits, seed)
    print(f"Initial quantum state (first 10 elements): {quantum_state[:10]}")

    conjugate_state = calculate_conjugate(quantum_state)
    print(f"Conjugate quantum state (first 10 elements): {conjugate_state[:10]}")

if __name__ == "__main__":
    main()