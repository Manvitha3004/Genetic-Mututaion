from dnasim import mutate

# Test different sequence lengths
sequences = {
    "Short": "ATGC",
    "Medium": "ATGCTAGCTAGCT",
    "Long": "ATGCTAGCTAGCTGATCGATCGATCG",
    "Very Long": "ATGCTAGCTAGCTGATCGATCGATCGATCGATCGATCGATCGATCG"
}

# Test different mutation rates
rates = [0.01, 0.05, 0.1, 0.25, 0.5, 0.75]

for name, seq in sequences.items():
    print(f"\n=== Testing {name} Sequence ({len(seq)} bases) ===")
    print(f"Original: {seq}")
    
    for rate in rates:
        variants = mutate(seq, rate=rate, n_variants=3)
        print(f"\nRate {rate*100:.0f}%:")
        for i, var in enumerate(variants, 1):
            # Count differences from original
            mutations = sum(1 for a, b in zip(seq, var) if a != b)
            print(f"Variant {i}: {var} ({mutations} mutations)")

print("\nDone exploring mutations!")