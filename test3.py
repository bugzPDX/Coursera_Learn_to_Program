def do_twice(f,g):
    f(g)
    f(g)

def do_four(f,g):
    do_twice(f,g)
    do_twice(f,g)

def print_twice(s):
    print(s)

    
do_four(print_twice, 'spam')




def print_spam():
    print('spam')



def print_grid():
    horiz = ('+ - - - - '*2 + '+')
    vert = ('|         '*2 + '|')
    print(horiz)
    do_four(print_twice,vert)
    print(horiz)
    do_four(print_twice,vert)
    print(horiz)



def print_big_grid():
    horiz = ('+ - - - - '*4 + '+')
    vert = ('|         '*4 + '|')
    print(horiz)
    do_four(print_twice,vert)
    print(horiz)
    do_four(print_twice,vert)
    print(horiz)
    do_four(print_twice,vert)
    print(horiz)
    do_four(print_twice,vert)
    print(horiz)
