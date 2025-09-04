"""
Demo script showing dna-sim package functionality
"""
from dnasim import mutate

def demo_mutations():
    # Example 1: Basic mutation
    sequence = "ATCGATCG"
    print("\n1. Basic mutation (1% rate, 1 variant)")
    print("Original:", sequence)
    print("Mutated:", mutate(sequence)[0])

    # Example 2: Multiple variants
    print("\n2. Multiple variants (5% rate, 3 variants)")
    variants = mutate(sequence, rate=0.05, n_variants=3)
    print("Original:", sequence)
    for i, var in enumerate(variants, 1):
        print(f"Variant {i}:", var)

    # Example 3: High mutation rate
    print("\n3. High mutation rate (50% rate)")
    print("Original:", sequence)
    print("Mutated:", mutate(sequence, rate=0.5)[0])

    # Example 4: Case insensitive
    print("\n4. Case insensitive input")
    lower_seq = "atcgatcg"
    print("Original:", lower_seq)
    print("Mutated:", mutate(lower_seq)[0])

if __name__ == "__main__":
    print("DNA Mutation Simulator Demo")
    print("==========================")
    demo_mutations()