import pytest
from dnasim import mutate

def test_mutate_return_type():
    seq = "ATGC"
    result = mutate(seq)
    assert isinstance(result, list)
    assert all(isinstance(x, str) for x in result)
    assert len(result) == 1

def test_mutate_zero_rate():
    seq = "ATGCATGC"
    result = mutate(seq, rate=0, n_variants=5)
    assert len(result) == 5
    assert all(x == seq for x in result)

def test_mutate_full_rate():
    seq = "ATGC"
    result = mutate(seq, rate=1.0)[0]
    assert result != seq
    assert len(result) == len(seq)
    assert all(base in 'ATGC' for base in result)

def test_invalid_sequence():
    with pytest.raises(ValueError):
        mutate("ATGX")

def test_invalid_rate():
    with pytest.raises(ValueError):
        mutate("ATGC", rate=1.5)
        
def test_invalid_variants():
    with pytest.raises(ValueError):
        mutate("ATGC", n_variants=0)
        
def test_multiple_variants():
    seq = "ATGC"
    n_variants = 3
    result = mutate(seq, n_variants=n_variants)
    assert len(result) == n_variants
    assert len(set(result)) == n_variants  # All variants should be different
    
def test_empty_sequence():
    assert mutate("") == []
    
def test_case_insensitive():
    seq = "atgc"
    result = mutate(seq)
    assert len(result) == 1
    assert all(base in 'ATGC' for base in result[0])