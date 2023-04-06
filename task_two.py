class Reversor:
    @classmethod
    def lets_reverse(cls, word: str) -> str:
        return word[::-1]

print(f"Factorial: {Reversor.lets_reverse(word= 'Labas rytas')}")