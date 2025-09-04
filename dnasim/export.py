import json
from typing import List, Dict
import csv
from datetime import datetime

def export_fasta(sequences: List[str], filename: str):
    """Export sequences in FASTA format."""
    with open(filename, 'w') as f:
        for i, seq in enumerate(sequences):
            f.write(f'>sequence_{i+1}\n{seq}\n')

def export_mutations(original: str, variants: List[str], filename: str):
    """Export mutation analysis in CSV format."""
    mutations = []
    for i, variant in enumerate(variants, 1):
        for pos, (orig, mut) in enumerate(zip(original, variant)):
            if orig != mut:
                mutations.append({
                    'variant': i,
                    'position': pos,
                    'original': orig,
                    'mutated': mut
                })
    
    if filename.endswith('.json'):
        with open(filename, 'w') as f:
            json.dump(mutations, f, indent=2)
    else:
        with open(filename, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['variant', 'position', 'original', 'mutated'])
            writer.writeheader()
            writer.writerows(mutations)