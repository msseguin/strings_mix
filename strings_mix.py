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
        if letter.islower(): # confirm it is lower case
            if letter in s2_dictionary:
                if len(s1_dictionary[letter]) > len(s2_dictionary[letter]):
                    if len(s1_dictionary[letter]) > 1:
                        output_string.append("1:"+s1_dictionary[letter]+"/")
                elif len(s1_dictionary[letter]) < len(s2_dictionary[letter]):
                    output_string.append("2:"+s2_dictionary[letter]+"/")
                elif len(s1_dictionary[letter]) == len(s2_dictionary[letter]):
                    if len(s1_dictionary[letter]) > 1:
                        output_string.append("=:"+s2_dictionary[letter]+"/")
            elif len(s1_dictionary[letter]) > 1:
                output_string.append("1:"+s1_dictionary[letter]+"/")

    # check for any stragglers
    for letter in s2_dictionary:
        if letter.islower(): # confirm it is lower case
            if len(s2_dictionary[letter]) > 1:
                if letter not in s1_dictionary:
                    output_string.append("2:"+s2_dictionary[letter]+"/")


    output_string.sort(key=len)
    
    print(output_string.reverse())
    
    output_string = ''.join(output_string)
    
    return output_string[:-1]
    
# build a dictionary with each letter and string of total
def count_letters(letters):
    letters_counts = {}
    for letter in letters:
        if letter.islower():
            if letter in letters_counts:
                letters_counts[letter] += letter
            else:
                letters_counts[letter] = letter
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
        
        