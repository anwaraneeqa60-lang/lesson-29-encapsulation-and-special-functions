class StringReverser:
    """A class to handle word-by-word string manipulation."""
    
    def reverse_words(self, text: str) -> str:
        """
        Reverses the order of words in a given string.
        Automatically handles multiple spaces, leading, and trailing whitespaces.
        """
        words = text.split()
        reversed_words = words[::-1]
        return " ".join(reversed_words)
if __name__ == "__main__":
    reverser = StringReverser()
    sample_text = "  Hello  world   from Python "
    result = reverser.reverse_words(sample_text)
    print(f"Original: '{sample_text}'")
    print(f"Reversed: '{result}'")