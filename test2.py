def write_to_file(file, sentences):

    """ (file open for writing, list of str) -> NoneType

    Write each sentence from sentences to file, one per line.

    Precondition: the sentences contain no newlines.

    >>> write_to_file(write_file, ['sentence one.', 'sentence two',
    'sentence three', 'sentence four', 'sentence five'])

    """

    for s in sentences:
        write_file.write(s)
        write_file.write('\n')

    
