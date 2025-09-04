from dnasim import mutate

# Example DNA sequence
original_sequence = "ATGCTAGCTAGCT"

print(f"Original DNA: {original_sequence}")

# Test different mutation scenarios
print("\n1. Single mutation (1% rate):")
result1 = mutate(original_sequence, rate=0.01)
print(f"Mutated: {result1[0]}")

print("\n2. Multiple variants (5% rate):")
result2 = mutate(original_sequence, rate=0.05, n_variants=3)
for i, variant in enumerate(result2, 1):
    print(f"Variant {i}: {variant}")

print("\n3. High mutation rate (50%):")
result3 = mutate(original_sequence, rate=0.5)
print(f"Mutated: {result3[0]}")