def cleaner(a):  # returns a set of all unique arg string alpha characters in lower case.
    b = set([x.lower() for x in list(a) if x.isalpha()])
    return b


def get_center():
    a = input('Center Letter - ')
    b = cleaner(a)
    
    if len(b) == 1:
        return list(b)[0]
    else:
        print('You fucked it')
        return get_center()


def get_ring():
    a = input('Outer Letters - ')
    b = cleaner(a)
    
    if len(b) == 6:
        return b
    else:
        print('You fucked it')
        return get_ring()


def main():
    f = open('scrabble-words.txt', 'r')
    word_list = [x[:-1] for x in f]
    f.close()
    wl = [w.lower() for w in word_list if len(w) > 3]
    running = True
    
    while running:
        center = get_center()
        ring = get_ring()
        ring.add(center)
        out = []

        for x in wl:
            if center in x and ring.issuperset(x):
                out.append(x.title()+',')

        out.sort()
        for x in range(0, len(out), 7):
            print(*out[x:x+7])


        if input('Any: Continue\n  1: Quit\n') == '1':
            running = False


if __name__ == '__main__':
    main()
