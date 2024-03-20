def update_dictionary(a_dictionary, key, value):
    # Check if the key/value exist already
    if key in a_dictionary:
        a_dictionary[key] = value
    else:
        a_dictionary.update({'key':value})
    retun a_dictionary
