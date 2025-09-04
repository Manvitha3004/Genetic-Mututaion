import random
from typing import List, Dict, Tuple
from dataclasses import dataclass
from .utils import validate_sequence, validate_rate

@dataclass
class MutationResult:
    """Container for mutation results and statistics."""
    sequence: str
    mutations: List[Tuple[int, str, str]]  # [(position, from_base, to_base), ...]
    mutation_rate: float

    def __str__(self) -> str:
        return f"Sequence: {self.sequence}\nMutations: {len(self.mutations)}\nRate: {self.mutation_rate:.2%}"

def mutate(sequence: str, rate: float = 0.01, n_variants: int = 1) -> List[str]:
    """
    Generate mutated DNA sequences by random nucleotide substitutions.

    Args:
        sequence: Input DNA sequence (string of A, T, G, C)
        rate: Mutation rate per base (default: 0.01)
        n_variants: Number of variant sequences to generate (default: 1)

    Returns:
        List[str]: List of mutated DNA sequences

    Examples:
        >>> sequences = mutate("ATCG", rate=0.5, n_variants=3)
        >>> print(sequences)  # ['ATTG', 'AGCG', 'ATCC']
    """
    if not sequence:
        return []

    if not validate_sequence(sequence):
        raise ValueError("Sequence must only contain A, T, G, C nucleotides")

    if not validate_rate(rate):
        raise ValueError("Mutation rate must be between 0 and 1")
        
    # Define mutation models
    transitions = {'A': 'G', 'G': 'A', 'C': 'T', 'T': 'C'}
    transversions = {
        'A': ['C', 'T'], 'G': ['C', 'T'],
        'C': ['A', 'G'], 'T': ['A', 'G']
    }

    if n_variants < 1:
        raise ValueError("Number of variants must be positive")

    sequence = sequence.upper()
    
    # Biological mutation patterns
    transitions = {
        'A': 'G', 'G': 'A',  # Purine to purine
        'C': 'T', 'T': 'C'   # Pyrimidine to pyrimidine
    }
    
    transversions = {
        'A': ['C', 'T'], 'G': ['C', 'T'],  # Purine to pyrimidine
        'C': ['A', 'G'], 'T': ['A', 'G']   # Pyrimidine to purine
    }
    
    # Mutation probabilities based on real data
    transition_prob = 0.8  # Transitions are more common
    
    # Special case: zero mutation rate
    if rate == 0:
        return [sequence] * n_variants
        
    # Special case: 100% mutation rate
    if rate == 1.0:
        results = []
        for _ in range(n_variants):
            mutated = list(sequence)
            for i in range(len(mutated)):
                options = [n for n in nucleotides if n != mutated[i]]
                mutated[i] = random.choice(options)
            results.append(''.join(mutated))
        return results
        
    variants = set()

    max_attempts = n_variants * 100
    attempts = 0
    
    while len(variants) < n_variants and attempts < max_attempts:
        mutated = list(sequence)
        mutations_made = False
        
        # Ensure at least one mutation for uniqueness
        if len(variants) > 0:
            pos = random.randrange(len(sequence))
            base = mutated[pos]
            # Force at least one mutation
            if random.random() < transition_prob:
                mutated[pos] = transitions[base]
            else:
                mutated[pos] = random.choice(transversions[base])
            mutations_made = True
            
            # Apply biologically relevant mutations
        for i in range(len(mutated)):
            if random.random() < rate:
                base = mutated[i]
                # Determine mutation type (transition vs transversion)
                if random.random() < transition_prob:
                    mutated[i] = transitions[base]
                else:
                    mutated[i] = random.choice(transversions[base])
                mutations_made = True
                
        variant = ''.join(mutated)
        if mutations_made and variant not in variants:
            variants.add(variant)
            
        attempts += 1
        
    if len(variants) < n_variants:
        # If we can't generate enough variants, recursively try with higher rate
        return mutate(sequence, min(rate * 2, 1.0), n_variants)
        
    return list(variants)[:n_variants]