import tiktoken

enc = tiktoken.get_encoding("cl100k_base")

text = "Kubernetes is great"

tokens = enc.encode(text)

print(tokens)

for token in tokens:
    print(token, enc.decode([token]))