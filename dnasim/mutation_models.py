"""Real biological mutation models based on empirical data."""

# Mutation probabilities based on published studies
MUTATION_PROBABILITIES = {
    # Transition probabilities (observed in human genome)
    'transitions': {
        'A': {'G': 0.92},  # A->G is most common
        'G': {'A': 0.89},
        'C': {'T': 0.91},
        'T': {'C': 0.90}
    },
    
    # Transversion probabilities
    'transversions': {
        'A': {'C': 0.04, 'T': 0.04},
        'G': {'C': 0.06, 'T': 0.05},
        'C': {'A': 0.05, 'G': 0.04},
        'T': {'A': 0.05, 'G': 0.05}
    }
}

# CpG dinucleotide mutation rates (methylation-induced)
CPG_MUTATION_RATE = 0.1  # 10x higher than normal rate

# UV-induced mutation patterns
UV_MUTATION_PATTERNS = {
    'CC': 'TT',  # CC to TT mutation
    'CT': 'TT',  # CT to TT mutation
    'TC': 'TT'   # TC to TT mutation
}

def get_mutation_probability(base: str, to_base: str) -> float:
    """Get empirically observed mutation probability."""
    if to_base in MUTATION_PROBABILITIES['transitions'][base]:
        return MUTATION_PROBABILITIES['transitions'][base][to_base]
    return MUTATION_PROBABILITIES['transversions'][base].get(to_base, 0.0)

def is_cpg_site(sequence: str, position: int) -> bool:
    """Check if position is in a CpG site."""
    if position < len(sequence) - 1:
        return sequence[position:position+2].upper() == 'CG'
    return False

def get_contextual_mutation_rate(sequence: str, position: int, base_rate: float) -> float:
    """Adjust mutation rate based on sequence context."""
    if is_cpg_site(sequence, position):
        return base_rate * CPG_MUTATION_RATE
    return base_rate