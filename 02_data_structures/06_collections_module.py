from collections import Counter, defaultdict

words = ["apple", "grapes", "apple", "orange", "grapes", "apple"]
word_counts = Counter(words)

print("Apple count:", word_counts["apple"])
print("Word counts:", word_counts)

scores = defaultdict(int)
scores["Alice"] += 10
print("Alice's score:", scores["Alice"])