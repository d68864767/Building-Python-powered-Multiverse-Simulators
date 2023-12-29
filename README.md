# Python-powered Multiverse Simulators

This project is a Python-powered multiverse simulator. It allows you to create and manage multiple universes, each with its own set of properties, and simulate them.

## Project Structure

The project is structured as follows:

- `main.py`: The main entry point of the application.
- `universe.py`: Contains the `Universe` class, which represents a single universe.
- `multiverse.py`: Contains the `Multiverse` class, which manages multiple `Universe` instances.
- `simulator.py`: Contains the `Simulator` class, which uses a `Multiverse` instance to simulate multiple universes.
- `utils.py`: Contains utility functions for loading and saving properties from a JSON file, and validating properties.
- `config.py`: Contains configuration variables for the application.
- `tests/`: Contains unit tests for the `Universe`, `Multiverse`, and `Simulator` classes.

## Usage

To use the simulator, you need to create a `Simulator` instance, add universes to it, and then call the `simulate` method. Here is an example:

```python
from simulator import Simulator

# Create a new simulator
simulator = Simulator()

# Add a universe to the simulator
simulator.add_universe('1', {'mass': 1e50, 'size': 1e100})

# Simulate all universes in the simulator
simulator.simulate()
```

You can also get and set the properties of a universe:

```python
# Get the properties of a universe
properties = simulator.get_universe_properties('1')

# Set the properties of a universe
simulator.set_universe_properties('1', {'mass': 2e50, 'size': 2e100})
```

## Configuration

You can configure the properties for the universes and the path to the JSON file for loading and saving properties in the `config.py` file.

## Testing

To run the tests, use the following command:

```bash
python -m unittest discover tests
```

## Contributing

Contributions are welcome. Please submit a pull request.

## License

This project is licensed under the MIT License.
