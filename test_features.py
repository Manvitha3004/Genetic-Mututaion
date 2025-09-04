from dnasim import mutate
from dnasim.analysis import analyze_mutations, plot_mutation_patterns

def run_tests():
    # Test Case 1: Basic Mutation
    print("=== Test 1: Basic Mutation ===")
    dna = "ATCGATCG"
    print(f"Original: {dna}")
    variants = mutate(dna, rate=0.1, n_variants=1)
    print(f"Mutated: {variants[0]}\n")

    # Test Case 2: Multiple Variants with Analysis
    print("=== Test 2: Multiple Variants with Analysis ===")
    dna = "ATCGATCGATCG" * 2
    variants = mutate(dna, rate=0.2, n_variants=5)
    print(f"Original ({len(dna)} bp): {dna}")
    for i, var in enumerate(variants, 1):
        diffs = sum(a != b for a, b in zip(dna, var))
        print(f"Variant {i}: {var} ({diffs} mutations)")
    
    # Analyze patterns
    stats = analyze_mutations(dna, variants)
    print("\nMutation Statistics:")
    print(f"Total variants: {len(variants)}")
    print(f"Average mutations per variant: {sum(stats['mutation_counts'])/len(variants):.1f}")
    
    # Generate visualization
    print("\nGenerating visualization...")
    plot_mutation_patterns(dna, variants, "mutation_analysis.png")
    print("Visualization saved as 'mutation_analysis.png'")

if __name__ == "__main__":
    run_tests()