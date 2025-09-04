"""Biological DNA sequence generator using real gene/motif data."""
from .sequences import (
    CODING_SEQUENCES,
    PROMOTER_SEQUENCES,
    REGULATORY_ELEMENTS,
    TF_BINDING_SITES,
    get_real_sequence,
    get_promoter
)

def generate_promoter_region(gene_name: str = 'P53') -> str:
    """Return real promoter sequence for a gene."""
    return get_promoter(gene_name)

def generate_coding_sequence(gene_name: str = 'P53') -> str:
    """Return real coding sequence for a gene."""
    return get_real_sequence(gene_name)

def generate_regulatory_sequence() -> str:
    """Return a concatenation of real regulatory motifs."""
    elements = [
        REGULATORY_ELEMENTS['TATA_box'],
        REGULATORY_ELEMENTS['Kozak_sequence'],
        TF_BINDING_SITES['NF_kB'],
        REGULATORY_ELEMENTS['Poly_A_signal']
    ]
    return ''.join(elements)

def generate_gene(gene_name: str = 'P53', with_regulatory: bool = True) -> str:
    """Return a complete gene structure using real sequences."""
    sequence = []
    if with_regulatory:
        sequence.append(generate_promoter_region(gene_name))
    sequence.append(generate_coding_sequence(gene_name))
    if with_regulatory:
        sequence.append(generate_regulatory_sequence())
    return ''.join(sequence)