def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    my_dict = {}

    for letter in phrase:
        my_dict[letter] = my_dict.get(letter,0) + 1
        
    return my_dict

# Every letter you get to, we check to see if it's in the "my_dict" already with get.
# Since get has a second argument, instead of throwing an error if it doesn't find it, 
# it will return the second argument.

# That's zero + 1, since this must be the first time we saw that letter.
# And then that value gets assigned to that key.
# If the letter IS there, it just adds one to the existing value.



