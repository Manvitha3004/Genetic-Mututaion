from dnasim import mutate

# Example DNA sequence
sequence = "ATGCGATCGATCGATCG"

print("Original sequence:", sequence)

# Generate 3 variants with 5% mutation rate
variants = mutate(sequence, rate=0.05, n_variants=3)

print("\nMutated variants (5% mutation rate):")
for i, variant in enumerate(variants, 1):
    print(f"Variant {i}: {variant}")