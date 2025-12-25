from src.modules.rle.encode import rle_encode
from src.modules.rle.decode import rle_decode
from src.modules.rle.percent import compression_percent
from src.config.config import APP_NAME, VERSION, AUTHOR, STUDENT_ID, NUMBERS_ALLOWED, LOG_FILE


print(f"\n{APP_NAME} - v{VERSION} \n    by {AUTHOR} (ID: {STUDENT_ID}) \n")  # Display application name, version, author, and student ID

def save_log(original, encoded, decoded, percent):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write("--- RLE Compression Log ---\n")
        f.write(f"Original:        {original}\n")
        f.write(f"Compressed:      {encoded}\n")
        f.write(f"Decompressed:    {decoded}\n")
        f.write(f"Compression rate: {percent}%\n\n")
# Main interaction loop
while True:
    print("Choose an option:")
    print("[1] Enter text for compression")
    print("[2] View log history")
    print("[3] Exit program")
    choice = input("Your choice: ").strip()

    match choice:
        case "3": # Exit the program
            print("\nProgram is closing... 👋")
            break

        case "1": # Text compression option
            text = input("Enter text (e.g., AAAABBBBCCCDDAA): ").strip()

            if text.upper() == "EXIT":
                print("\nProgram is closing... 👋")
                break

            # Simple digit check
            if not NUMBERS_ALLOWED and any(c.isdigit() for c in text):
                print("Error: Input contains digits, but numbers are not allowed. Process cancelled.\n")
                continue

            # Lowercase check
            if any(c.islower() for c in text):
                print("Error: Input contains lowercase letters. Process cancelled.\n")
                continue

            if not text:
                print("Please enter a non-empty text.\n")
                continue

            # Encode with number support check
            try:
                encoded = rle_encode(text, allow_numbers=NUMBERS_ALLOWED)
            except ValueError as e:
                print(f"Error: {e}\n")
                continue

            # Decode and calculate compression
            decoded = rle_decode(encoded)
            percent = compression_percent(text, encoded)

            # Display results
            print("\n--- Results ---")
            print("Original:        ", text)
            print("Compressed:      ", encoded)
            print("Decompressed:    ", decoded)
            print("Compression rate:", percent, "%\n")

            # Ask to save log
            save_option = input("Do you want to save this result to log? (y/n): ").strip().lower()
            if save_option == "y":
                save_log(text, encoded, decoded, percent)
                print(f"Result saved to {LOG_FILE}\n")

        case "2": # View log history
            try:
                with open(LOG_FILE, "r", encoding="utf-8") as f:
                    print("\n--- Log History ---")
                    print(f.read())
            except FileNotFoundError:
                print("No log file found.\n")

        case _: # Invalid option handling
            print("Invalid option. Please choose 1, 2, or 3.\n")