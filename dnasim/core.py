import random
from typing import List
from .utils import validate_sequence, validate_rate
from .mutation_models import get_mutation_probability, get_contextual_mutation_rate

def mutate(sequence: str, rate: float = 0.01, n_variants: int = 1) -> List[str]:
    """
    Generate mutated DNA sequences using real biological mutation models.

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
        
    if n_variants < 1:
        raise ValueError("Number of variants must be positive")

    sequence = sequence.upper()
    bases = 'ATGC'
    variants = set()
    max_attempts = n_variants * 100
    attempts = 0

    while len(variants) < n_variants and attempts < max_attempts:
        mutated = list(sequence)
        for i in range(len(mutated)):
            context_rate = get_contextual_mutation_rate(sequence, i, rate)
            if random.random() < context_rate:
                original = mutated[i]
                # Choose mutation based on empirical probabilities
                probs = [get_mutation_probability(original, b) for b in bases if b != original]
                total = sum(probs)
                if total > 0:
                    choices = [b for b in bases if b != original]
                    weights = [p/total for p in probs]
                    mutated[i] = random.choices(choices, weights=weights)[0]
        variant = ''.join(mutated)
        variants.add(variant)
        attempts += 1
        
    if len(variants) < n_variants:
        raise ValueError(f"Could not generate {n_variants} unique variants. Try increasing mutation rate.")
        
    return list(variants)[:n_variants]