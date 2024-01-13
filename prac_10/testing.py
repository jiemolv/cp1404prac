def repeat_string(s, n):
    """
    Repeat string s, n times, with spaces in between.
    """
    return " ".join([s] * n)


def test_repeat_string():
    """
    Test the repeat_string function.
    """
    assert repeat_string('hello', 3) == 'hello hello hello'
    assert repeat_string('world', 5) == 'world world world world world'


class Car:
    def __init__(self, fuel):
        self.fuel = fuel

    def add_fuel(self, amount):
        """
        Add fuel to the car.
        """
        self.fuel += amount

    def test_add_fuel(self):
        """
        Test the add_fuel method.
        """
        car = Car(50)
        car.add_fuel(20)
        assert car.fuel == 70

        car.add_fuel(30)
        assert car.fuel == 100


def is_long_word(word, length=5):
    """
    Check if a word is longer than a specified length.
    """
    return len(word) > length


def test_is_long_word():
    """
    Test the is_long_word function.
    """
    assert is_long_word("Python") is True
    assert is_long_word("Java") is False


def format_phrase_as_sentence(phrase):
    """
    Format a phrase as a sentence: starting with a capital and ending with a single full stop.
    """
    formatted_phrase = phrase.capitalize()
    if not formatted_phrase.endswith('.'):
        formatted_phrase += '.'
    return formatted_phrase


def test_format_phrase_as_sentence():
    """
    Test the format_phrase_as_sentence function.
    """
    assert format_phrase_as_sentence("hello") == "Hello."
    assert format_phrase_as_sentence("this is a sentence") == "This is a sentence."
    assert format_phrase_as_sentence("already formatted.") == "Already formatted."


if __name__ == "__main__":
    test_repeat_string()
    # Uncomment the line below to run the doctests
    # import doctest
    # doctest.testmod()

    car = Car(50)
    car.test_add_fuel()
    test_is_long_word()
    test_format_phrase_as_sentence()
