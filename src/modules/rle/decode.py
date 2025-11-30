def rle_decode(encoded_text): # Decode the RLE encoded text back to its original form.
    decoded = ""
    number = ""
    i = 0

    while i < len(encoded_text):
        # Collect digits for the repeat count
        while i < len(encoded_text) and encoded_text[i].isdigit():
            number += encoded_text[i]
            i += 1

        # Skip colon
        if i < len(encoded_text) and encoded_text[i] == ":":
            i += 1

        # Repeat the character
        if i < len(encoded_text):
            char = encoded_text[i]
            decoded += char * int(number)
            number = ""  # reset
        i += 1

    return decoded
