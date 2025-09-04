from dnasim import mutate
from dnasim.analysis import plot_mutation_patterns

# Generate a long DNA sequence for testing
sequence = "ATGC" * 25  # 100 base pairs

print("Processing long sequence in batches:")
print(f"Original ({len(sequence)} bp): {sequence}")

# Generate mutations
variants = mutate(sequence, rate=0.05, n_variants=3)

print("\nMutated variants:")
for i, var in enumerate(variants, 1):
    mutations = sum(1 for a, b in zip(sequence, var) if a != b)
    print(f"Variant {i} ({mutations} mutations): {var}")

# Analyze mutation patterns
print("\nGenerating mutation pattern visualization...")
plot_mutation_patterns(sequence, variants, "mutation_patterns.png")
print("Visualization saved to mutation_patterns.png")