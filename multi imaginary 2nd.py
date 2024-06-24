import numpy as np

def initialize_quantum_state(num_qubits):
# 2^num_qubits個の複素数要素を持つランダムな状態を生成
    state = np.random.rand(2**num_qubits) + 1j * np.random.rand(2**num_qubits)
    # 正規化
    state = state / np.linalg.norm(state)
    return state

def calculate_conjugate(state):
    return np.conjugate(state)

def main():
    num_qubits = 20

    # 量子状態の初期化
    quantum_state = initialize_quantum_state(num_qubits)
    print(f"Initial quantum state (first 10 elements): {quantum_state[:10]}")

    # 複素共役の計算
    conjugate_state = calculate_conjugate(quantum_state)
    print(f"Conjugate quantum state (first 10 elements): {conjugate_state[:10]}")

if __name__ == "__main__":
    main()