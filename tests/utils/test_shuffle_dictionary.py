import unittest
from ecosystem.utils.helpers import shuffle_dictionary


class TestShuffleDictionary(unittest.TestCase):
    """Unit tests for the shuffle_dictionary() function."""

    def test_shuffle_preserves_keys_and_values(self):
        """Shuffling should not change keys or associated values."""
        original = {"a": 1, "b": 2, "c": 3}
        shuffled = shuffle_dictionary(original, seed=42)

        # Same keys, same values
        self.assertEqual(set(shuffled.keys()), set(original.keys()))
        self.assertEqual(set(shuffled.values()), set(original.values()))

    def test_shuffle_changes_order(self):
        """Order should differ from original when possible."""
        original = {"a": 1, "b": 2, "c": 3}
        shuffled = shuffle_dictionary(original, seed=42)

        # If all keys are distinct, order should change for this seed
        self.assertNotEqual(list(shuffled.keys()), list(original.keys()))

    def test_shuffle_is_deterministic_with_seed(self):
        """Same seed → same output; different seeds → different output."""
        original = {"x": 10, "y": 20, "z": 30}

        shuffled1 = shuffle_dictionary(original, seed=123)
        shuffled2 = shuffle_dictionary(original, seed=123)
        shuffled3 = shuffle_dictionary(original, seed=999)

        self.assertEqual(list(shuffled1.keys()), list(shuffled2.keys()))
        self.assertNotEqual(list(shuffled1.keys()), list(shuffled3.keys()))

    def test_shuffle_empty_dict(self):
        """Empty dictionary should return an empty dictionary."""
        self.assertEqual(shuffle_dictionary({}, seed=5), {})

    def test_shuffle_singleton_dict(self):
        """A single-key dictionary should remain unchanged."""
        original = {"only": 42}
        shuffled = shuffle_dictionary(original, seed=999)
        self.assertEqual(shuffled, original)


if __name__ == "__main__":
    unittest.main()
