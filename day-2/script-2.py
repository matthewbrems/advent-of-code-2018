# Open the file for reading.
file = open('./day_2_input.txt', 'r')

# List comprehension iterating over each item in the file
list_of_words = [i for i in file]

# Create a function to calculate Hamming distance.
def hamming(string_1, string_2):
    count = 0
    for i in range(len(string_1)):
        if string_1[i] != string_2[i]:
            count += 1
    return count

# Iterate through list of words.
for i in range(len(list_of_words)):
    for j in list_of_words[i+1:]:

        # Check Hamming distance.
        if hamming(list_of_words[i], j) == 1:
            
        # If Hamming = 1, then create new string.
            for letter in range(len(j)):
                if list_of_words[i][letter] != j[letter]:
                    
                    # Print the result.
                    print(j[0:letter] + j[letter+1:])
