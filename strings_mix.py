def mix(s1, s2):
    # use list to get all chars
    letters_s1 = list(s1)
    letters_s2 = list(s2)
    
    # build dictionaries with counts
    s1_dictionary = count_letters(letters_s1)
    s2_dictionary = count_letters(letters_s2)
    
    print(s1_dictionary)
    print(s2_dictionary)
    
    output_string = []

    # TODO - remove 1 count items
    # TODO - sort by length
    for letter in s1_dictionary:
        if letter in s2_dictionary:
            if s1_dictionary[letter] > s2_dictionary[letter]:
                output_string.append(buildLettersString("1",letter, s1_dictionary[letter]))
            elif s1_dictionary[letter] == s2_dictionary[letter]:
                output_string.append(buildLettersString("=",letter,s2_dictionary[letter]))
            else:
                output_string.append(buildLettersString("=",letter,s1_dictionary[letter]))
        else:
             output_string.append(buildLettersString("1",letter, s1_dictionary[letter]))
    
   # for letter in s2_dictionary:
    #    if letter not in s2_dictionary:
     #       output_string.append(buildLettersString("1",letter, s1_dictionary[letter]))
    

    output_string= sorted(output_string, key=len)
    
    return output_string
    
# build a count dictionary
def count_letters(letters):
    letters_counts = {}
    for letter in letters:
        if letter.islower():
            if letter in letters_counts:
                letters_counts[letter] += 1
            else:
                letters_counts[letter] = 1
    return letters_counts

# builds            
def buildLettersString(symbol,letter,count):
    # build the string using a while loop
    letters_string = symbol+":"
    while count > 0:
        letters_string += letter
        count -=1
    letters_string +="/"
    
    # output the string
    return letters_string
        
        