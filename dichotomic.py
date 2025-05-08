def dichotomic(input_list, val):
    if len(input_list) == 1: #quindi non la posso più dividere!! rimane 1 elemento
        if input_list[0] == val:
            return True
        else:
            return False
    else:
        index = len(input_list)//2
        mid_val = input_list[index]

        if val == mid_val:
            return True
        elif val < mid_val:
            return dichotomic(input_list[:index], val)
        else:
            return dichotomic(input_list[index + 1:], val)


if __name__ == '__main__':
    sequenza = [1,2,3,4,5,6,7,8,9,10]
    print(dichotomic(sequenza, 2)) #il valore 2 sta nella lista??
    print(dichotomic(sequenza, 11))