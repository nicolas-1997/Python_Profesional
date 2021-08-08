import time


def fibo_gen(numeberMax: int):
    n1 = 0
    n2 = 1
    counter = 0
    
    while True:
        if counter == numeberMax:
            print("Maximum iterations reached")
            break
    
        if counter == 0:
            counter +=1
            yield n1
        elif counter == 1:
            counter +=1
            yield n2
        else:
            aux = n1 + n2 
            n1, n2 = n2, aux
            counter +=1
            yield aux   

def fibo_compact(stop: int):
    n1, n2 = 0, 1
    counter = 0

    while True:
        if counter == stop:
            print("Maximum iterations reached")
            break
        else:
            counter +=1
            yield n1
            n1, n2 = n2, n1+n2

if __name__ == "__main__":

    numeberMax = int(input("Enter a maximum number of iterations: "))

    fibo = fibo_gen(numeberMax)
    fibo2 = fibo_compact(numeberMax)
    for element in fibo2:
        print(element)
        time.sleep(1)