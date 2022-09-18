def mix(s1, s2):
    # use list to get a list of all chars
    letters_s1 = list(s1)
    letters_s2 = list(s2)
    
    # build dictionaries with strings for all chars (filter after)
    s1_dictionary = count_letters(letters_s1)
    s2_dictionary = count_letters(letters_s2)
    
    # list of all the strings that will be output (not sorted)
    chars_lst = []
    
    # check all elements that exist in dictionary that will be added for string 1 or =
    for letter in s1_dictionary:
        if letter.islower(): # confirm it is lower case
            if letter in s2_dictionary:
                if len(s1_dictionary[letter]) > len(s2_dictionary[letter]):
                    if len(s1_dictionary[letter]) > 1:
                        chars_lst.append("1:"+s1_dictionary[letter]+"/")
                elif len(s1_dictionary[letter]) < len(s2_dictionary[letter]):
                    chars_lst.append("2:"+s2_dictionary[letter]+"/")
                elif len(s1_dictionary[letter]) == len(s2_dictionary[letter]):
                    if len(s1_dictionary[letter]) > 1:
                        chars_lst.append("=:"+s2_dictionary[letter]+"/")
            elif len(s1_dictionary[letter]) > 1:
                chars_lst.append("1:"+s1_dictionary[letter]+"/")

    # check for any stragglers in dictionary for string 2
    for letter in s2_dictionary:
        if letter.islower(): # confirm it is lower case
            if len(s2_dictionary[letter]) > 1:
                if letter not in s1_dictionary:
                    chars_lst.append("2:"+s2_dictionary[letter]+"/")

    output_string = formatOutputString(chars_lst)
    
    
    
    # remove last / in string 
    return output_string



# def count_letters(letters):
# build a dictionary with each letter and string of total
# maintains order for python 3.6 and above 
def count_letters(letters):
    letters_counts = {}
    for letter in letters:
        if letter.islower():
            # if it has not been added, add it, otherwise add one more copy of the letter on it
            if letter in letters_counts:
                letters_counts[letter] += letter
            else:
                letters_counts[letter] = letter
    return letters_counts

# builds            
def buildLettersString(symbol,letters):
    # build the string start and end
    return symbol+":"+ letters + "/"

# def formatOutputString(chars_lst:list[str])
# Takes in list of strings with largest letters
# sorts them alphabeticaly and then by length
# joins them and outputs as string
def formatOutputString(chars_lst:list[str]):
    # sort the output alphabetically (part of the required ordering)
    chars_lst.sort()
    
    # sorts based on length
    chars_lst.sort(key=len,reverse=True)
    # sort(key=lambda s: len(s))
    
    # build the string
    output_string = ''.join(chars_lst)
    
    #remove the last character (extra /)
    return output_string[:-1]