import tiktoken

enc = tiktoken.get_encoding("cl100k_base")

while True:
    text = input("Enter text: ")

    ids = enc.encode(text)

    print("\nToken IDs:")
    print(ids)

    print("\nTokens:")
    for token in ids:
        print(f"{token} -> {repr(enc.decode([token]))}")