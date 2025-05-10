class dayfive:

    my_list =  ['rushi',28,'jayesh',26,'amir',34,'baibahv',28]
    my_set = {'QA','Dev','Manager','DevOps','rushi'}
    my_set.update(my_list)
    print(my_set)

    a = set('abracadabra')
    b = set('alacazam')
    c = a ^ b
    print(c)

    A = {1, 3, 5}
    B = {2, 4, 6}
    C = {0}

    print('Original set ',A)

    A.update(B,C)
    print('updated set',A)

    a = [1, 2, 3, 4]
    b = [5, 6, 3, 8]

    common = set(a) & set(b)
    if common:
        print("Common", common)
    else:
        print("Not common.")

    setA = {'a', 'c', 'v','bn','ng'}
    setB = {'a', 'c', 'v', 'er', 'ty', 'ui'}
    setA.intersection_update(setB)
    print(setA)

    clas1 = {1, 2, 3, 4, 5}
    div = {1, 2, 4, 5, 7}
    clas1.update(div-clas1)
    print(clas1 )