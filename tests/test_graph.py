"""
Unit tests for Graph data structure implementation.
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Examples')))

import pytest


def test_graph_initialization_empty():
    """Test Graph initialization with no data"""
    from graph import Graph
    
    g = Graph()
    assert g.vertices() == []
    assert g.edges() == []


def test_graph_initialization_with_dict():
    """Test Graph initialization with dictionary"""
    from graph import Graph
    
    graph_dict = {
        "a": ["b", "c"],
        "b": ["a", "d"],
        "c": ["a"],
        "d": ["b"]
    }
    
    g = Graph(graph_dict)
    vertices = g.vertices()
    assert "a" in vertices
    assert "b" in vertices
    assert "c" in vertices
    assert "d" in vertices
    assert len(vertices) == 4


def test_add_vertex():
    """Test adding vertices to graph"""
    from graph import Graph
    
    g = Graph()
    g.add_vertex("x")
    g.add_vertex("y")
    g.add_vertex("z")
    
    vertices = g.vertices()
    assert "x" in vertices
    assert "y" in vertices
    assert "z" in vertices
    assert len(vertices) == 3


def test_add_vertex_duplicate():
    """Test adding duplicate vertex (should not create duplicate)"""
    from graph import Graph
    
    g = Graph()
    g.add_vertex("a")
    g.add_vertex("a")  # Adding same vertex again
    
    vertices = g.vertices()
    assert vertices.count("a") == 1


def test_add_edge():
    """Test adding edges to graph"""
    from graph import Graph
    
    g = Graph()
    g.add_edge(["a", "b"])
    
    vertices = g.vertices()
    assert "a" in vertices
    # Note: Based on implementation, vertex "b" might not be added automatically


def test_graph_edges():
    """Test getting edges from graph"""
    from graph import Graph
    
    graph_dict = {
        "a": ["b", "c"],
        "b": ["a"],
        "c": ["a"]
    }
    
    g = Graph(graph_dict)
    edges = g.edges()
    assert len(edges) > 0


def test_complex_graph():
    """Test a more complex graph structure"""
    from graph import Graph
    
    # Create a graph representing a social network
    social_graph = {
        "Alice": ["Bob", "Charlie"],
        "Bob": ["Alice", "David"],
        "Charlie": ["Alice", "David"],
        "David": ["Bob", "Charlie"]
    }
    
    g = Graph(social_graph)
    vertices = g.vertices()
    
    assert len(vertices) == 4
    assert "Alice" in vertices
    assert "Bob" in vertices
    assert "Charlie" in vertices
    assert "David" in vertices


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
