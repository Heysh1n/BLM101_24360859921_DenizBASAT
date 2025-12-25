def rle_decode(encoded_text):
    decoded_parts = []  # Used to collect decoded segments
    number = ""
    i = 0

    while i < len(encoded_text):
        # Collect digits representing the count of repetitions
        while i < len(encoded_text) and encoded_text[i].isdigit():
            number += encoded_text[i]
            i += 1

        # Skip a colon if present
        if i < len(encoded_text) and encoded_text[i] == ":":
            i += 1

        # Repeat the character the specified number of times
        if i < len(encoded_text):
            char = encoded_text[i]
            decoded_parts.append(char * int(number)) # Add to list
            number = "" 
        i += 1

    return "".join(decoded_parts) # Collect all in one string