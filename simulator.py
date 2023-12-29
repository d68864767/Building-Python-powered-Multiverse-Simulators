```python
from multiverse import Multiverse

class Simulator:
    def __init__(self):
        """
        Initialize a new Simulator instance.
        """
        self.multiverse = Multiverse()

    def add_universe(self, id, properties):
        """
        Add a new universe to the multiverse.

        :param id: The unique identifier for the new universe.
        :param properties: A dictionary containing the properties of the new universe.
        """
        self.multiverse.add_universe(id, properties)

    def remove_universe(self, id):
        """
        Remove a universe from the multiverse.

        :param id: The unique identifier for the universe to remove.
        """
        self.multiverse.remove_universe(id)

    def simulate(self):
        """
        Simulate all universes in the multiverse.
        """
        self.multiverse.simulate()

    def get_universe_properties(self, id):
        """
        Get the properties of a universe in the multiverse.

        :param id: The unique identifier for the universe whose properties to get.
        :return: A dictionary containing the properties of the universe, or None if no such universe exists.
        """
        return self.multiverse.get_properties(id)

    def set_universe_properties(self, id, properties):
        """
        Set the properties of a universe in the multiverse.

        :param id: The unique identifier for the universe whose properties to set.
        :param properties: A dictionary containing the new properties for the universe.
        """
        self.multiverse.set_properties(id, properties)
```
