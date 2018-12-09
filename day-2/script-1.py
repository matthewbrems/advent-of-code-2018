# Open the file for reading.
file = open('./day_2_input.txt', 'r')

# List comprehension iterating over each item in the file
list_of_words = [i for i in file]

# Instantiate counters.
two_count = 0
three_count = 0

# Iterate over each word.
for i in list_of_words:
    
    # Instantiate empty dictionary.
    word_dict = {}
    
    # Check each unique letter in the word, then count the values
    # and append it into the dictionary.
    for j in set(i):
        word_dict[j] = i.count(j)
        
    # Check to see if there are any letters with 2 or 3 occurrences.
    if 2 in word_dict.values():
        two_count += 1
    if 3 in word_dict.values():
        three_count += 1

# Print checksum.
print(two_count * three_count)
