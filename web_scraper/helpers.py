def read_file_into_list(file_location):
    """Return list of elements from file

    :param str file_location: location of the file containing the proxies
    :return: list of elements from file
    :rtype: list
    """
    return_list = []

    with open(file_location, 'r') as File:
        for line in File:
            line = line.strip()
            proxies.append(line)

    return return_list
