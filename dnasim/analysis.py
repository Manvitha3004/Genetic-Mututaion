import matplotlib.pyplot as plt
from typing import List, Dict, Tuple
from collections import defaultdict

def analyze_mutations(original: str, variants: List[str]) -> Dict:
    """Analyze mutation patterns across variants."""
    stats = {
        'mutation_counts': [],
        'positions': defaultdict(int),
        'substitutions': defaultdict(int)
    }
    
    for variant in variants:
        mutations = 0
        for pos, (orig, mut) in enumerate(zip(original, variant)):
            if orig != mut:
                mutations += 1
                stats['positions'][pos] += 1
                stats['substitutions'][f'{orig}->{mut}'] += 1
        stats['mutation_counts'].append(mutations)
    
    return stats

def plot_mutation_patterns(original: str, variants: List[str], output_file: str = None):
    """Generate visualization of mutation patterns."""
    stats = analyze_mutations(original, variants)
    
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))
    
    # Plot 1: Mutation counts histogram
    ax1.hist(stats['mutation_counts'], bins='auto')
    ax1.set_title('Distribution of Mutations')
    ax1.set_xlabel('Number of Mutations')
    ax1.set_ylabel('Frequency')
    
    # Plot 2: Position-wise mutation frequency
    positions = list(stats['positions'].keys())
    frequencies = list(stats['positions'].values())
    ax2.bar(positions, frequencies)
    ax2.set_title('Mutation Positions')
    ax2.set_xlabel('Sequence Position')
    ax2.set_ylabel('Mutation Frequency')
    
    # Plot 3: Substitution types
    subs = list(stats['substitutions'].keys())
    counts = list(stats['substitutions'].values())
    ax3.bar(subs, counts)
    ax3.set_title('Substitution Types')
    ax3.set_xlabel('Substitution')
    ax3.set_ylabel('Count')
    plt.xticks(rotation=45)
    
    plt.tight_layout()
    if output_file:
        plt.savefig(output_file)
    else:
        plt.show()
    plt.close()