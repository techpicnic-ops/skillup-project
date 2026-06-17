

text = """
I love Kubernetes
I love Prometheus
I love Grafana
"""

words = text.split()

pairs = {}

for i in range(len(words)-1):
    current = words[i]
    next_word = words[i+1]

    if current not in pairs:
        pairs[current] = []

    pairs[current].append(next_word)

print(pairs)