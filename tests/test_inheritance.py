"""
Unit tests for basic OOP concepts - inheritance examples.
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Examples')))

import pytest
from io import StringIO


def test_animal_class_creation():
    """Test Animal class initialization"""
    from inheritance import Animal
    
    animal = Animal()
    assert hasattr(animal, 'defineMe')
    assert hasattr(animal, 'eat')


def test_lion_class_creation():
    """Test Lion class initialization"""
    from inheritance import Lion
    
    lion = Lion()
    assert hasattr(lion, 'defineMe')
    assert hasattr(lion, 'eat')
    assert hasattr(lion, 'prey')


def test_lion_inherits_from_animal():
    """Test that Lion properly inherits from Animal"""
    from inheritance import Lion, Animal
    
    lion = Lion()
    assert isinstance(lion, Lion)
    assert isinstance(lion, Animal)


def test_animal_methods(capsys):
    """Test Animal class methods"""
    from inheritance import Animal
    
    animal = Animal()
    
    animal.defineMe()
    captured = capsys.readouterr()
    assert "parent class Animal" in captured.out
    
    animal.eat()
    captured = capsys.readouterr()
    assert "eating" in captured.out.lower()


def test_lion_methods(capsys):
    """Test Lion class methods"""
    from inheritance import Lion
    
    lion = Lion()
    
    lion.defineMe()
    captured = capsys.readouterr()
    assert "child class Lion" in captured.out
    
    lion.eat()
    captured = capsys.readouterr()
    assert "eating" in captured.out.lower()
    
    lion.prey()
    captured = capsys.readouterr()
    assert "hunt" in captured.out.lower() or "prey" in captured.out.lower()


def test_method_overriding():
    """Test that Lion overrides Animal's defineMe method"""
    from inheritance import Lion, Animal
    
    animal = Animal()
    lion = Lion()
    
    # Both have the method but with different implementations
    assert hasattr(animal, 'defineMe')
    assert hasattr(lion, 'defineMe')
    # The method behavior should be different (verified by output tests)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
