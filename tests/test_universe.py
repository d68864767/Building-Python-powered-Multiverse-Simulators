```python
import unittest
from universe import Universe

class TestUniverse(unittest.TestCase):
    def setUp(self):
        self.universe = Universe('1', {'mass': 1e50, 'size': 1e100})

    def test_init(self):
        self.assertEqual(self.universe.id, '1')
        self.assertEqual(self.universe.properties, {'mass': 1e50, 'size': 1e100})

    def test_simulate(self):
        with self.assertRaises(NotImplementedError):
            self.universe.simulate()

    def test_get_properties(self):
        properties = self.universe.get_properties()
        self.assertEqual(properties, {'mass': 1e50, 'size': 1e100})

    def test_set_properties(self):
        new_properties = {'mass': 2e50, 'size': 2e100}
        self.universe.set_properties(new_properties)
        self.assertEqual(self.universe.properties, new_properties)

if __name__ == '__main__':
    unittest.main()
```
