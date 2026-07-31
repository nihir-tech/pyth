from collections import Counter
filename = input("Enter file name: ")
with open(filename, "r") as file:
    text = file.read().lower()
words = text.split()
frequency = Counter(words)
sorted_words = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
print("\nTop 10 Most Frequently Appearing Words:\n")
for word, count in sorted_words[:10]:
    print(f"{word} : {count}")
