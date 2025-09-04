"""Utility functions for DNA sequence manipulation."""
from typing import List, Dict, Optional

def validate_sequence(sequence: str) -> bool:
    """
    Validate if a string is a valid DNA sequence.
    
    Args:
        sequence: Input DNA sequence
        
    Returns:
        bool: True if sequence only contains valid nucleotides
        
    Raises:
        ValueError: If sequence contains invalid characters
    """
    invalid_chars = set(sequence.upper()) - set('ATGC')
    if invalid_chars:
        raise ValueError(f"Invalid nucleotides found: {invalid_chars}")
    return True

def validate_rate(rate: float) -> bool:
    """
    Validate mutation rate is between 0 and 1.
    
    Args:
        rate: Mutation rate
        
    Returns:
        bool: True if rate is valid
        
    Raises:
        ValueError: If rate is outside valid range
    """
    if not isinstance(rate, (int, float)):
        raise ValueError("Mutation rate must be a number")
    if not 0 <= rate <= 1:
        raise ValueError("Mutation rate must be between 0 and 1")
    return True

def analyze_mutations(original: str, mutated: str) -> List[Dict[str, str]]:
    """
    Analyze differences between original and mutated sequences.
    
    Args:
        original: Original DNA sequence
        mutated: Mutated DNA sequence
        
    Returns:
        List of mutation details
    """
    mutations = []
    for i, (orig, mut) in enumerate(zip(original, mutated)):
        if orig != mut:
            mutations.append({
                'position': i,
                'original': orig,
                'mutated': mut,
                'type': 'substitution'
            })
    return mutations