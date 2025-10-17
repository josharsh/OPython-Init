"""
Unit tests for LinkedList data structure implementation.
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Examples')))

import pytest
from io import StringIO


def test_node_creation():
    """Test Node class initialization"""
    from LinkedList import Node
    
    node = Node(5)
    assert node.data == 5
    assert node.next is None


def test_linkedlist_creation():
    """Test LinkedList class initialization"""
    from LinkedList import LinkedList
    
    llist = LinkedList()
    assert llist.head is None


def test_linkedlist_with_nodes():
    """Test LinkedList with multiple nodes"""
    from LinkedList import LinkedList, Node
    
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    
    llist.head.next = second
    second.next = third
    
    # Verify structure
    assert llist.head.data == 1
    assert llist.head.next.data == 2
    assert llist.head.next.next.data == 3
    assert llist.head.next.next.next is None


def test_linkedlist_print(capsys):
    """Test LinkedList print functionality"""
    from LinkedList import LinkedList, Node
    
    llist = LinkedList()
    llist.head = Node(10)
    second = Node(20)
    third = Node(30)
    
    llist.head.next = second
    second.next = third
    
    llist.printList()
    captured = capsys.readouterr()
    assert "10" in captured.out
    assert "20" in captured.out
    assert "30" in captured.out


def test_single_node_linkedlist():
    """Test LinkedList with single node"""
    from LinkedList import LinkedList, Node
    
    llist = LinkedList()
    llist.head = Node(100)
    
    assert llist.head.data == 100
    assert llist.head.next is None


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
