def remove_duplicates(lista):
    without_duplicate = []

    for element in lista:
        if element not in without_duplicate:
            without_duplicate.append(element)
        
    return without_duplicate

def remove_duplicates_with_set(lista: list):
    return list(set(lista)) 

def run():
    lista = [1,1,1,2,5 ,8,9,8,10, 15,11,12, 20,]
    print("remove_duplicates: ", remove_duplicates(lista))
    print("with sets: ", remove_duplicates_with_set(lista))

if __name__ == "__main__":
    run()