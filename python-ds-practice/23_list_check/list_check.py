def list_check(lst):
    """Are all items in lst a list?

        >>> 

        True

        >>> list_check([[1], "nope"])
        False
    """
    # return [el for el in lst if type(el)== list]

    for el in lst:
        if not isinstance(el, list):
            return False
        
    return True    
