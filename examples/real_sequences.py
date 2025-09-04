from dnasim import mutate
from dnasim.generator import generate_gene
from dnasim.analysis import plot_mutation_patterns

# Test mutations on real genes
genes = ['P53', 'Insulin', 'Hemoglobin']

for gene_name in genes:
    print(f"\n=== Testing mutations on {gene_name} gene ===")
    
    # Get the complete gene sequence
    gene_seq = generate_gene(gene_name=gene_name, with_regulatory=True)
    print(f"Original sequence length: {len(gene_seq)} bp")
    
    # Generate mutations with different rates
    rates = [0.001, 0.01, 0.05]  # Realistic mutation rates
    
    for rate in rates:
        variants = mutate(gene_seq, rate=rate, n_variants=3)
        print(f"\nMutations with {rate*100:.1f}% rate:")
        for i, var in enumerate(variants, 1):
            mutations = sum(1 for a, b in zip(gene_seq, var) if a != b)
            print(f"Variant {i}: {mutations} mutations ({mutations/len(gene_seq)*100:.2f}% changed)")
        
        # Analyze mutation patterns
        plot_mutation_patterns(gene_seq, variants, f"{gene_name}_{rate}_mutations.png")
        print(f"Mutation pattern visualization saved as '{gene_name}_{rate}_mutations.png'")