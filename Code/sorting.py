pangram = "The quick brown fox jumps over the lazy dog"

letters= sorted(pangram)
print(letters)

numbers = [2.3,4.5,8.7,3.1,1.6]
sorted= sorted(numbers)
print(sorted)
print(numbers)
# another_sorted_numbers = numbers.sort()
numbers.sort()
print(numbers)
# print(another_sorted_numbers)

missing_letter = sorted("The quick brown fox jumped over the lazy dog")
print(missing_letter)