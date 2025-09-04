"""Generate comprehensive DNA sequence quality reports."""
import matplotlib.pyplot as plt
from typing import List, Dict
from .validator import check_sequence_quality

def plot_gc_distribution(sequence: str, window_size: int = 50) -> None:
    """Plot GC content distribution along sequence."""
    gc_contents = []
    for i in range(0, len(sequence) - window_size + 1):
        window = sequence[i:i+window_size]
        gc = sum(1 for base in window.upper() if base in 'GC')
        gc_contents.append((gc / window_size) * 100)
    
    plt.figure(figsize=(10, 5))
    plt.plot(gc_contents)
    plt.title('GC Content Distribution')
    plt.xlabel('Sequence Position (Window Size: {})'.format(window_size))
    plt.ylabel('GC Content (%)')
    plt.grid(True)
    plt.savefig('gc_distribution.png')
    plt.close()

def generate_quality_report(sequence: str, output_file: str = 'quality_report.txt') -> None:
    """Generate comprehensive sequence quality report."""
    quality = check_sequence_quality(sequence)
    
    report = [
        "DNA Sequence Quality Report",
        "=" * 30,
        f"Sequence Length: {quality['length']} bp",
        f"GC Content: {quality['gc_content']:.1f}%",
        f"Valid Reading Frame: {quality['valid_reading_frame']}",
        "\nDetected Motifs:"
    ]
    
    for motif, positions in quality['motifs'].items():
        report.append(f"- {motif}: {len(positions)} occurrences at positions {positions}")
    
    report.append("\nRepetitive Regions:")
    for repeat, pos in quality['repetitive_regions']:
        report.append(f"- '{repeat}' at position {pos}")
    
    with open(output_file, 'w') as f:
        f.write('\n'.join(report))
    
    # Generate GC distribution plot
    plot_gc_distribution(sequence)

def batch_quality_analysis(sequences: Dict[str, str]) -> Dict[str, Dict]:
    """Analyze multiple sequences and compare their quality metrics."""
    results = {}
    for name, seq in sequences.items():
        results[name] = check_sequence_quality(seq)
    return results