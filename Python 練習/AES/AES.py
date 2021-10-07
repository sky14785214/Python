import numpy as np


# def multiplication(a,b):
def key_expansion(key,Nr,Nk):
    IF = np.array([(14,11,13,9), (9,14,11,9),(13,9,14,11),(11,13,9,14)])

    print(IF)
    print(key)
    # keyt = np.zeros(shape=(4,Nk))
    # keyt = np.array()
    

    np.reshape(key, (4, Nk))
    print(key)
    



a =  np.arange(20)
# key_expansion(a,1,2)
a = np.reshape(a, (4,5))
print(a)
