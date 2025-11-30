from src.config.config import NUMBERS_ALLOWED  # Import the config variable

def rle_encode(text, allow_numbers=None):

    # Use config default if allow_numbers is not explicitly provided
    if allow_numbers is None:
        allow_numbers = NUMBERS_ALLOWED

    if not text:
        return ""

    # Check for digits if numbers are not allowed
    if not allow_numbers and any(char.isdigit() for char in text):
        raise ValueError("Numbers in text are not allowed. Set NUMBERS_ALLOWED=True to enable.")

    result = []
    count = 1

    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            result.append(f"{count}:{text[i - 1]}")
            count = 1

    result.append(f"{count}:{text[-1]}")  # Append last character
    return "".join(result)
