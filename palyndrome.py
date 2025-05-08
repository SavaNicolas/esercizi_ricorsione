def palyndrome(word):
    if len(word) <= 1:
        return True
    else:
        return ((word[0] == word[-1]) and #word[-1] sarebbe l'ultima lettera,
                palyndrome(word[1:-1])) #word[1:-1] taglia primo e ultimo carattere


def palyndrome_banale(word):
    return word ==word[::-1] #word[1:-1] taglia primo e ultimo carattere

if __name__ == '__main__':
    print(palyndrome('casa'))
    print(palyndrome('civic'))

    # print(palyndrome_banale('casa'))
    # print(palyndrome_banale('civic'))
