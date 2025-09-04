from dnasim import mutate
from dnasim.generator import (
    generate_promoter_region,
    generate_coding_sequence,
    generate_regulatory_sequence,
    generate_gene
)
from dnasim.analysis import plot_mutation_patterns

# Generate and mutate a promoter region
promoter = generate_promoter_region()
print("\n=== Promoter Region ===")
print(f"Original: {promoter}")
mutated_promoters = mutate(promoter, rate=0.05, n_variants=2)
print("Mutations:")
for i, var in enumerate(mutated_promoters, 1):
    print(f"Variant {i}: {var}")

# Generate and mutate a coding sequence
coding = generate_coding_sequence(150)  # 50 codons
print("\n=== Coding Sequence ===")
print(f"Original: {coding}")
print(f"Start codon: {coding[:3]}")
print(f"Stop codon: {coding[-3:]}")
mutated_coding = mutate(coding, rate=0.01, n_variants=2)
print("Mutations:")
for i, var in enumerate(mutated_coding, 1):
    print(f"Variant {i}: {var}")

# Generate and mutate a complete gene
gene = generate_gene(with_regulatory=True)
print("\n=== Complete Gene ===")
print(f"Length: {len(gene)} bp")
print("Original sequence:")
for i in range(0, len(gene), 60):
    print(gene[i:i+60])

mutated_genes = mutate(gene, rate=0.02, n_variants=3)
print("\nMutated variants:")
for i, var in enumerate(mutated_genes, 1):
    mutations = sum(1 for a, b in zip(gene, var) if a != b)
    print(f"\nVariant {i} ({mutations} mutations):")
    for j in range(0, len(var), 60):
        print(var[j:j+60])

# Visualize mutations in the gene
plot_mutation_patterns(gene, mutated_genes, "gene_mutations.png")
print("\nMutation pattern visualization saved as 'gene_mutations.png'")