import random

def alice_prepare_qubits(num_qubits):
	"""Alice prepares qubits in random bases."""
	bases = [random.choice(['+', 'x']) for _ in range(num_qubits)]
	bit_values = [random.randint(0, 1) for _ in range(num_qubits)]

	qubits = []
	for i in range(num_qubits):
		if bases[i] == '+':
			qubits.append(('H' if bit_values[i] == 0 else 'V'))
		else:
			qubits.append(('D' if bit_values[i] == 0 else 'A'))

	return bases, bit_values, qubits

def bob_measure_qubits(qubits):
	"""Bob measures qubits using random bases."""
	bases = [random.choice(['+', 'x']) for _ in qubits]
	bit_values = []

	for i in range(len(qubits)):
		if bases[i] == '+':
			bit_values.append(0 if qubits[i] in ['H', 'D'] else 1)
		else:
			bit_values.append(0 if qubits[i] in ['H', 'A'] else 1)

	return bases, bit_values

def sifting_phase(alice_bases, bob_bases, bit_values):
	"""Keep bits where Alice and Bob used the same basis."""
	sifted_key = []
	for i in range(len(alice_bases)):
		if alice_bases[i] == bob_bases[i]:
			sifted_key.append(bit_values[i])
	return sifted_key

# Simulate BB84 Protocol
num_qubits = 10

# Step 1: Alice prepares qubits
alice_bases, alice_bit_values, qubits = alice_prepare_qubits(num_qubits)

# Step 2: Bob measures qubits
bob_bases, bob_bit_values = bob_measure_qubits(qubits)

print("Alice's Bases: [", end="")
for a, b in zip(alice_bases, bob_bases):
	if a == b:
		print(f"\033[92m{a}\033[0m, ", end="")
	else:
		print(f"\033[91m{a}\033[0m, ", end="")
print("]")

print("Bob's Bases:   [", end="")
for a, b in zip(alice_bases, bob_bases):
	if a == b:
		print(f"\033[92m{b}\033[0m, ", end="")
	else:
		print(f"\033[91m{b}\033[0m, ", end="")
print("]")

print("Alice's Bits:  [", end="")
for a, b in zip(alice_bases, bob_bases):
	if a == b:
		print(f"\033[92m{alice_bit_values.pop(0)}\033[0m, ", end="")
	else:
		print(f"\033[91m{alice_bit_values.pop(0)}\033[0m, ", end="")
print("]")

print("Bob's Bits:    [", end="")
for a, b in zip(alice_bases, bob_bases):
	if a == b:
		print(f"\033[92m{bob_bit_values.pop(0)}\033[0m, ", end="")
	else:
		print(f"\033[91m{bob_bit_values.pop(0)}\033[0m, ", end="")
print("]")


# Step 3: Sifting phase
sifted_key = sifting_phase(alice_bases, bob_bases, bob_bit_values)

print(f"Length of original key bits: {num_qubits}")
print(f"Length of sifted key: {len(sifted_key)}")
print(f"Sifted Key: {sifted_key}")

'''
In this simulation:

Alice prepares qubits in random bases (+ or x), where:
+ corresponds to the standard basis with horizontal (H) and vertical (V) polarizations.
x corresponds to the diagonal basis with diagonal (D) and antidiagonal (A) polarizations.
Bob then measures these qubits in random bases.
After sending and measuring the qubits, Alice and Bob publicly announce the bases they used (without revealing the bit values). They then keep the bits where they used the same basis. This results in a "sifted" key.
Note: In a real-world scenario, there's more to the BB84 protocol (like error checking, privacy amplification, etc.). This simulation is simplified for the sake of brevity and clarity. Additionally, this simulation assumes an ideal, noise-free quantum channel. In practice, noise and eavesdropping would introduce errors that the protocol must handle.
'''