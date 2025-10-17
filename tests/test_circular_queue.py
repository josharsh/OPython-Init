"""
Unit tests for Examples/circular_queue.py
Tests the Queue (circular queue) implementation.
"""
import unittest
import sys
from pathlib import Path

# Add Examples directory to path
examples_path = Path(__file__).parent.parent / "Examples"
sys.path.insert(0, str(examples_path))

from circular_queue import Queue


class TestCircularQueue(unittest.TestCase):
    """Test cases for the Queue class (circular queue)."""

    def setUp(self):
        """Set up test fixtures."""
        self.queue = Queue()

    def test_queue_creation(self):
        """Test that a Queue is created with correct size."""
        self.assertTrue(self.queue.isEmpty())
        self.assertFalse(self.queue.isFull())

    def test_enqueue_single_element(self):
        """Test enqueuing a single element."""
        self.queue.enQueue(1)
        self.assertFalse(self.queue.isEmpty())

    def test_enqueue_until_full(self):
        """Test enqueuing until queue is full."""
        for i in range(5):
            self.queue.enQueue(i)
        self.assertTrue(self.queue.isFull())

    def test_dequeue_element(self):
        """Test dequeuing an element."""
        self.queue.enQueue(1)
        self.queue.enQueue(2)
        dequeued = self.queue.deQueue()
        self.assertEqual(dequeued, 1)

    def test_dequeue_order(self):
        """Test that dequeue follows FIFO order."""
        self.queue.enQueue(1)
        self.queue.enQueue(2)
        self.queue.enQueue(3)
        self.assertEqual(self.queue.deQueue(), 1)
        self.assertEqual(self.queue.deQueue(), 2)
        self.assertEqual(self.queue.deQueue(), 3)

    def test_circular_behavior(self):
        """Test circular queue wrapping behavior."""
        # Fill the queue
        for i in range(5):
            self.queue.enQueue(i)
        
        # Remove some elements
        self.queue.deQueue()
        self.queue.deQueue()
        
        # Add more elements (should wrap around)
        self.queue.enQueue(5)
        self.queue.enQueue(6)
        
        self.assertTrue(self.queue.isFull())

    def test_isEmpty_on_empty_queue(self):
        """Test isEmpty on empty queue."""
        self.assertTrue(self.queue.isEmpty())

    def test_isEmpty_after_operations(self):
        """Test isEmpty after enqueue and dequeue."""
        self.queue.enQueue(1)
        self.assertFalse(self.queue.isEmpty())
        self.queue.deQueue()
        self.assertTrue(self.queue.isEmpty())
    
    def test_dequeue_on_empty_queue(self):
        """Test dequeue on empty queue returns -1."""
        result = self.queue.deQueue()
        self.assertEqual(result, -1)


if __name__ == '__main__':
    unittest.main()
