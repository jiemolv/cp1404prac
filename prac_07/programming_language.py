"""
programming_language
Estimate: 30 minutes
Actual:   32 minutes
"""
"""
CP1404/CP5632 Practical - Suggested Solution
Programming Language class with tests.
"""


class ProgrammingLanguage:
    """Represent information about a programming language."""

    def __init__(self, name, typing, reflection, year, pointer_arithmetic=None):
        """Construct a ProgrammingLanguage from the given values."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year
        self.pointer_arithmetic = PointerArithmetic(pointer_arithmetic)

    def __repr__(self):
        """Return string representation of a ProgrammingLanguage."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Determine if language is dynamically typed."""
        return self.typing == "Dynamic"

    def has_pointer_arithmetic(self):
        """Check if the language supports pointer arithmetic."""
        return self.pointer_arithmetic.supported

class PointerArithmetic:
    """Represents the availability of pointer arithmetic for a programming language."""

    def __init__(self, supported=False):
        """Initialize PointerArithmetic with availability status."""
        self.supported = supported

    def __str__(self):
        """Return string representation of PointerArithmetic."""
        return f"Pointer Arithmetic: {'Supported' if self.supported else 'Not Supported'}"



def run_tests():
    """Run simple tests/demos on ProgrammingLanguage class."""
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    languages = [ruby, python, visual_basic]
    print(python)

    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


if __name__ == "__main__":
    run_tests()