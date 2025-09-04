# dna-sim

A lightweight Python package for simulating DNA mutations through random nucleotide substitutions.

## Features

- Simple API for generating mutated DNA sequences
- Configurable mutation rate and number of variants
- Pure Python implementation
- No external dependencies

## Installation

```bash
pip install dna-sim
```

## Usage

```python
from dnasim import mutate

# Generate 3 mutated variants with 5% mutation rate
sequence = "ATGCGATCG"
variants = mutate(sequence, rate=0.05, n_variants=3)

print("Original:", sequence)
for i, var in enumerate(variants, 1):
    print(f"Variant {i}:", var)
```

## API Reference

### `mutate(sequence: str, rate: float = 0.01, n_variants: int = 1) -> List[str]`

Generate mutated DNA sequences by random nucleotide substitutions.

**Parameters:**
- `sequence`: Input DNA sequence (string of A, T, G, C)
- `rate`: Mutation rate per base (default: 0.01)
- `n_variants`: Number of variant sequences to generate (default: 1)

**Returns:**
List of mutated sequences

## License

MIT License