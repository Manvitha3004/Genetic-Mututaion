import argparse
import sys
from typing import List
from . import mutate
from .analysis import plot_mutation_patterns

def parse_args(args: List[str] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='DNA Mutation Simulator')
    parser.add_argument('sequence', help='Input DNA sequence')
    parser.add_argument('-r', '--rate', type=float, default=0.01,
                      help='Mutation rate (default: 0.01)')
    parser.add_argument('-n', '--variants', type=int, default=1,
                      help='Number of variants to generate (default: 1)')
    parser.add_argument('-v', '--visualize', action='store_true',
                      help='Generate mutation pattern visualization')
    parser.add_argument('-o', '--output', help='Output file for visualization')
    parser.add_argument('-b', '--batch', action='store_true',
                      help='Process sequence in batches of 100 bases')
    
    return parser.parse_args(args)

def process_batch(sequence: str, rate: float, n_variants: int) -> List[str]:
    """Process long sequences in batches."""
    batch_size = 100
    results = []
    
    for i in range(0, len(sequence), batch_size):
        batch = sequence[i:i + batch_size]
        variants = mutate(batch, rate, n_variants)
        results.extend(variants)
    
    return results

def main(args: List[str] = None):
    args = parse_args(args)
    
    # Validate sequence
    if not set(args.sequence.upper()).issubset({'A', 'T', 'G', 'C'}):
        print("Error: Sequence must only contain A, T, G, C nucleotides", file=sys.stderr)
        sys.exit(1)
        
    # Generate mutations
    if args.batch and len(args.sequence) > 100:
        variants = process_batch(args.sequence, args.rate, args.variants)
    else:
        variants = mutate(args.sequence, args.rate, args.variants)
    
    # Print results
    print(f"\nOriginal: {args.sequence}")
    for i, var in enumerate(variants, 1):
        print(f"Variant {i}: {var}")
    
    # Generate visualization if requested
    if args.visualize:
        plot_mutation_patterns(args.sequence, variants, args.output)
        if args.output:
            print(f"\nVisualization saved to {args.output}")

if __name__ == '__main__':
    main()