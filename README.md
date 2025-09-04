# dna-sim: Realistic DNA Mutation Simulator


A Python package for simulating DNA mutations using real gene sequences and empirical mutation models. Designed for bioinformatics, genomics, and educational use.


## 🚀 Features
- Real human gene sequences (TP53, Insulin, Hemoglobin)
- Biologically accurate mutation models (transitions, transversions, CpG context)
- Mutation pattern analysis and visualization
- Sequence quality reporting
- Command-line interface and batch processing
- No random/synthetic data—only real biological logic


## 🛠️ Installation

Clone the repository and install dependencies:
```bash
(https://github.com/Manvitha3004/DNA.git)
cd dna-sim
pip install -r requirements.txt
```


## 🧬 Step-by-Step Usage

### 1. Generate a Real Gene Sequence
```python
from dnasim.generator import generate_gene
# Get TP53 gene with regulatory elements
gene = generate_gene(gene_name='P53', with_regulatory=True)
print(gene)
```

### 2. Simulate Mutations
```python
from dnasim import mutate
# Generate 3 variants with 1% mutation rate
variants = mutate(gene, rate=0.01, n_variants=3)
for v in variants:
    print(v)
```

### 3. Analyze and Visualize Mutations
```python
from dnasim.analysis import plot_mutation_patterns
plot_mutation_patterns(gene, variants, "mutations.png")
```

### 4. Sequence Quality Report
```python
from dnasim.reports import generate_quality_report
# Generates a text report and GC content plot
generate_quality_report(gene, "quality_report.txt")


## 🖥️ Command-Line Interface

```bash
python -m dnasim.cli ATGCGT... --rate 0.01 --variants 3 --visualize --output mutations.png
```


## 🏁 Final Setup & Usage Checklist

1. **Install Python 3.8+**
   ```bash
   python --version
   ```
2. **Install All Requirements**
   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt  # For development/publishing
   ```
3. **Run Example Scripts**
   ```bash
   python examples/real_sequences.py
   python examples/quality_analysis.py
   python examples/batch_processing.py
   ```
4. **View Outputs**
   - Mutation visualizations: `mutations.png`, `gene_mutations.png`
   - Quality reports: `quality_report.txt`, `gc_distribution.png`
   - Mutated sequences: printed in terminal and saved as needed
5. **Use the CLI**
   ```bash
   python -m dnasim.cli ATGCGT... --rate 0.01 --variants 3 --visualize --output mutations.png
   ```
6. **Explore and Customize**
   - Add your own gene sequences to `dnasim/sequences.py`
   - Tweak mutation rates and batch sizes in scripts


## 💡 Pro Tips
- For large datasets, use batch processing and export features.
- All mutation logic is based on real biological models—no random/synthetic data.
- The package is modular: you can use only the parts you need (mutation, analysis, reporting).


## 🆘 Need Help?
- If you encounter errors, check your Python version and dependencies.
- For issues, open a GitHub issue or contact the maintainer.


## 🧪 Example Output

- Mutated gene sequences
- Mutation pattern visualizations
- Sequence quality reports
- GC content distribution plots


## 🤝 Contributing
1. Fork the repo
2. Create your feature branch
3. Commit your changes
4. Push and open a Pull Request


## 📄 License
MIT License
