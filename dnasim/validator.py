"""DNA sequence validation and quality checks."""
from typing import Dict, List, Tuple

def check_gc_content(sequence: str) -> float:
    """Calculate GC content percentage."""
    gc_count = sum(1 for base in sequence.upper() if base in 'GC')
    return (gc_count / len(sequence)) * 100 if sequence else 0

def validate_reading_frame(sequence: str) -> bool:
    """Check if sequence length is multiple of 3 and has valid start/stop codons."""
    if len(sequence) < 3:
        return False
    
    sequence = sequence.upper()
    has_start = sequence.startswith('ATG')
    has_stop = any(sequence.endswith(codon) for codon in ['TAA', 'TAG', 'TGA'])
    correct_length = len(sequence) % 3 == 0
    
    return has_start and has_stop and correct_length

def find_motifs(sequence: str) -> Dict[str, List[int]]:
    """Find common DNA motifs and their positions."""
    motifs = {
        'TATA_box': 'TATAAA',
        'CpG': 'CG',
        'Kozak': 'GCCACC',
        'PolyA': 'AAAAAA'
    }
    
    results = {}
    for name, motif in motifs.items():
        positions = []
        for i in range(len(sequence) - len(motif) + 1):
            if sequence[i:i+len(motif)] == motif:
                positions.append(i)
        if positions:
            results[name] = positions
            
    return results

def check_sequence_quality(sequence: str) -> Dict[str, any]:
    """Comprehensive sequence quality check."""
    return {
        'length': len(sequence),
        'gc_content': check_gc_content(sequence),
        'valid_reading_frame': validate_reading_frame(sequence),
        'motifs': find_motifs(sequence),
        'is_palindromic': sequence == sequence[::-1],
        'repetitive_regions': find_repetitive_regions(sequence)
    }

def find_repetitive_regions(sequence: str, min_length: int = 4) -> List[Tuple[str, int]]:
    """Find repetitive regions in sequence."""
    repeats = []
    for i in range(len(sequence) - min_length + 1):
        for j in range(i + min_length, len(sequence) + 1):
            substr = sequence[i:j]
            if sequence.count(substr) > 1:
                repeats.append((substr, i))
    return repeats