
strings = ['Shikha', 'Muzam', 'Haua', '01971700130']


combined_string = ''.join(strings)


num_characters = len(combined_string)


num_vowels = sum(1 for char in combined_string if char.lower() in 'aeiou')

print("Sample Output\n")
print(strings)
print("\nNumber of Characters:", num_characters)
print("Number of Vowels:", num_vowels)
