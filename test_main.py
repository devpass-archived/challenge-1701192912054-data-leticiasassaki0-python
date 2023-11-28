import unittest
from main import Stack

class TestStack(unittest.TestCase):
    def test_push(self):
        stack = Stack()
        stack.push(10)
        stack.push(20)
        self.assertEqual(stack.size(), 2)

    def test_pop(self):
        stack = Stack()
        stack.push(10)
        stack.push(20)
        self.assertEqual(stack.pop(), 20)
        self.assertEqual(stack.size(), 1)
        self.assertEqual(stack.pop(), 10)
        self.assertEqual(stack.size(), 0)

    def test_peek(self):
        stack = Stack()
        stack.push(10)
        stack.push(20)
        self.assertEqual(stack.peek(), 20)
        self.assertEqual(stack.size(), 2)

    def test_is_empty(self):
        stack = Stack()
        self.assertTrue(stack.is_empty())
        stack.push(10)
        self.assertFalse(stack.is_empty())

if __name__ == '__main__':
    unittest.main()
