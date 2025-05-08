from time import sleep


def countdown(n):
    while (n >= 0):
        print(n)
        n-=1

def countdown_recursive(n):
    if n<=0:
        print("stop")
    else:
        print(n)
        sleep(0.5)
        counter= n-1
        countdown_recursive(counter)

if __name__ == '__main__':
    #countdown(10)
    countdown_recursive(10)