def nb_repetitions(elt:any,tab:list[any],)->int:
    '''
    >>> nb_repetitions(5, [2, 5, 3, 5, 6, 9, 5])
    3
    >>> nb_repetitions('A', ['B', 'A', 'B', 'A', 'R'])
    2
    >>> nb_repetitions(12, [1, '!', 7, 21, 36, 44])
    0
    '''
    nb=0
    for element in tab:
        if elt == element:
            nb+=1
    return nb

def binaire(a):
    '''
    >>> binaire(0)
    '0'
    >>> binaire(77)
    '1001101'
    
    convertit un nombre entier a en sa representation 
    binaire sous forme de chaine de caractères.'''
    if a == 0:
        return '0'
    bin_a =""
    while a>0: 
        bin_a = str(a%2) + bin_a 
        a = a//2
    return bin_a

if __name__ =='__main__':
    import doctest
    doctest.testmod()

