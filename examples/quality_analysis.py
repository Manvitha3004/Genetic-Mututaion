"""Example demonstrating DNA sequence quality analysis."""
from dnasim.generator import generate_gene
from dnasim.reports import generate_quality_report, batch_quality_analysis
from dnasim import mutate

# Analyze original genes
genes = {
    'P53': generate_gene('P53'),
    'Insulin': generate_gene('Insulin'),
    'Hemoglobin': generate_gene('Hemoglobin')
}

# Generate quality reports for each gene
print("Generating quality reports for original genes...")
for name, sequence in genes.items():
    generate_quality_report(sequence, f'{name}_quality.txt')
    print(f"Report generated for {name}")

# Generate mutations and analyze their impact
print("\nAnalyzing mutation impact...")
for name, sequence in genes.items():
    variants = mutate(sequence, rate=0.01, n_variants=3)
    
    # Compare original vs mutated sequences
    quality_comparison = batch_quality_analysis({
        'original': sequence,
        'variant1': variants[0],
        'variant2': variants[1],
        'variant3': variants[2]
    })
    
    print(f"\n{name} Mutation Analysis:")
    for seq_name, quality in quality_comparison.items():
        print(f"{seq_name}:")
        print(f"- GC Content: {quality['gc_content']:.1f}%")
        print(f"- Valid Reading Frame: {quality['valid_reading_frame']}")
        print(f"- Motifs found: {len(quality['motifs'])}")
        
print("\nAnalysis complete! Check the generated reports and plots.")