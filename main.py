import random
import string

def generate_random_chars(length=3):
    """Generate random characters of specified length"""
    return ''.join(random.choices(string.ascii_letters, k=length))

def encode_word(word):
    """Encode a single word according to the rules"""
    if len(word) >= 3:
        # Remove first letter and append at the end
        modified = word[1:] + word[0]
        # Add 3 random characters at start and end
        encoded = generate_random_chars() + modified + generate_random_chars()
        return encoded
    else:
        # Simply reverse the string
        return word[::-1]

def decode_word(word):
    """Decode a single word according to the rules"""
    if len(word) < 3:
        # Reverse the string
        return word[::-1]
    else:
        # Remove 3 characters from start and end
        if len(word) >= 6:  # Ensure word has at least 6 chars (3 start + 3 end)
            stripped = word[3:-3]
            if stripped:  # Ensure there's something left after stripping
                # Remove last letter and append to beginning
                decoded = stripped[-1] + stripped[:-1]
                return decoded
        return word  # Return as is if can't decode properly

def encode_message(message):
    """Encode an entire message"""
    words = message.split()
    encoded_words = [encode_word(word) for word in words]
    return ' '.join(encoded_words)

def decode_message(message):
    """Decode an entire message"""
    words = message.split()
    decoded_words = [decode_word(word) for word in words]
    return ' '.join(decoded_words)

def main():
    """Main program loop"""
    print("=" * 50)
    print("SECRET CODE LANGUAGE TRANSLATOR")
    print("=" * 50)

    while True:
        print("\nOptions:")
        print("1. Encode a message")
        print("2. Decode a message")
        print("3. Exit")

        choice = input("\nEnter your choice (1/2/3): ").strip()

        if choice == '1':
            message = input("\nEnter the message to encode: ")
            if message:
                encoded = encode_message(message)
                print(f"\nOriginal message: {message}")
                print(f"Encoded message: {encoded}")
            else:
                print("Please enter a valid message.")

        elif choice == '2':
            message = input("\nEnter the message to decode: ")
            if message:
                decoded = decode_message(message)
                print(f"\nEncoded message: {message}")
                print(f"Decoded message: {decoded}")
            else:
                print("Please enter a valid message.")

        elif choice == '3':
            print("\nThank you for using the Secret Code Language Translator!")
            break

        else:
            print("\nInvalid choice! Please enter 1, 2, or 3.")

        # Ask if user wants to continue
        if choice in ['1', '2']:
            continue_choice = input("\nDo you want to perform another operation? (yes/no): ").strip().lower()
            if continue_choice not in ['yes', 'y']:
                print("\nThank you for using the Secret Code Language Translator!")
                break

if __name__ == "__main__":
    main()
