from dnasim import mutate
from dnasim.generator import generate_sequence, generate_gene_like
from dnasim.export import export_fasta, export_mutations
from dnasim.analysis import plot_mutation_patterns

# Generate test sequences
random_seq = generate_sequence(100)
gene_seq = generate_gene_like(300)

# Generate mutations
variants_random = mutate(random_seq, rate=0.1, n_variants=5)
variants_gene = mutate(gene_seq, rate=0.05, n_variants=3)

# Export results
export_fasta(variants_random, 'random_mutations.fasta')
export_mutations(random_seq, variants_random, 'random_analysis.csv')
export_fasta(variants_gene, 'gene_mutations.fasta')
export_mutations(gene_seq, variants_gene, 'gene_analysis.json')

# Generate visualizations
plot_mutation_patterns(random_seq, variants_random, 'random_patterns.png')
plot_mutation_patterns(gene_seq, variants_gene, 'gene_patterns.png')

print("Advanced features demonstration complete!")
print("Check the following files:")
print("- random_mutations.fasta")
print("- random_analysis.csv")
print("- gene_mutations.fasta")
print("- gene_analysis.json")
print("- random_patterns.png")
print("- gene_patterns.png")