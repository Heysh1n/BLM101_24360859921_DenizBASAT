def compression_percent(original, encoded): #Calculate the compression percentage between the original and encoded data.
    if len(original) == 0: # "IF" the original data length is zero
        return 0

    ratio = (1 - (len(encoded) / len(original))) * 100 # Calculate the compression percentage
    return round(ratio, 2) # Return the percentage rounded to two decimal places
