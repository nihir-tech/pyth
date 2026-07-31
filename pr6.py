num = input("Enter a multi-digit number: ")
freq = [0] * 10
for ch in num:
    if ch.isdigit():
        freq[int(ch)] += 1
print("\nFrequency of each digit:")
for i in range(10):
    if freq[i] > 0:
        print(f"Digit {i} occurs {freq[i]} time(s)")
