# DNA Mutation Simulator (dna-sim)

A Python package for simulating DNA mutations using real biological sequences and mutation patterns.

## Features

- Real gene sequences (P53, Insulin, Hemoglobin)
- Biologically accurate mutation patterns (transitions/transversions)
- Complete gene structure simulation (promoters, coding sequences, regulatory elements)
- Mutation analysis and visualization
- Command-line interface
- Batch processing support

## Installation

```bash
pip install dna-sim
```

## Quick Start

```python
from dnasim import mutate
from dnasim.generator import generate_gene

# Get a real gene sequence (P53, Insulin, or Hemoglobin)
sequence = generate_gene(gene_name='P53')

# Generate mutations
variants = mutate(sequence, rate=0.01, n_variants=3)
```

## Step-by-Step Usage

1. **Generate a Gene Sequence**
   ```python
   from dnasim.generator import generate_gene
   
   # Get P53 gene with regulatory elements
   gene = generate_gene(gene_name='P53', with_regulatory=True)
   ```

2. **Create Mutations**
   ```python
   from dnasim import mutate
   
   # Generate 3 variants with 1% mutation rate
   variants = mutate(gene, rate=0.01, n_variants=3)
   ```

3. **Analyze Mutations**
   ```python
   from dnasim.analysis import plot_mutation_patterns
   
   # Visualize mutation patterns
   plot_mutation_patterns(gene, variants, "mutations.png")
   ```

## Command Line Usage

```bash
python -m dnasim.cli ATGC --rate 0.01 --variants 3 --visualize
```

## Available Genes

- P53 (Tumor suppressor)
- Insulin (Metabolic regulation)
- Hemoglobin (Oxygen transport)

## Advanced Features

### Batch Processing
```python
from dnasim.cli import process_batch

variants = process_batch(sequence, rate=0.01, n_variants=3)
```

### Export Results
```python
from dnasim.export import export_mutations

export_mutations(sequence, variants, "mutations.csv")
```

## API Reference

### `mutate(sequence: str, rate: float = 0.01, n_variants: int = 1)`
Generate mutations in DNA sequence.
- `sequence`: Input DNA sequence
- `rate`: Mutation rate (default: 0.01)
- `n_variants`: Number of variants (default: 1)

### `generate_gene(gene_name: str = 'P53', with_regulatory: bool = True)`
Generate complete gene sequence.
- `gene_name`: 'P53', 'Insulin', or 'Hemoglobin'
- `with_regulatory`: Include regulatory elements

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

MIT License