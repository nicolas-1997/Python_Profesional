if __name__ == "__main__":

    adc = {"Jinx", "Miss Fortune", "Sivir", "Lucian", "Ezreal"}
    jg = {"Shaco", "Tryndamere", "Warwik", "Vi","Teemo","Maokai", "Amumu","Phanteon"}
    top =  {"Tryndamere", "Dr Mundo", "Daruis", "Teemo", "Aatrox", "Maokai","Phanteon"}
    mid = {"Annie", "lux", "Phanteon", "Teemo", "Ezreal"}   
    supp = {"Nami", "Annie", "Blitz", "Rakan", "Lux"}

    champAp = {"Miss Fortune", "Ezreal", "Shaco", "Teemo", "Maokai", "Amumu", "Annie", "Lux", "Nami", "Blitz"}
    champAd = {"Jinx", "Miss Fortune","Sivir", "Lucian", "Ezreal","Shaco", "Tryndamere", "Warwik", "Vi","Dr Mundo", "Daruis","Aatrox","Phanteon","Rakan"}

    join_sets = adc | jg | supp  #The union of two sets A and B is the set A ∪ B that contains all the elements of A and B.
    inner_join = champAd & champAp #The intersection of two sets A and B is the set A ∩ B that contains all the common elements of A and B
    left_join = top - jg #The difference between two sets A and B is the set A \ B that contains all the elements of A that do not belong to B.
    full_outer_join = supp ^ mid #The symmetric difference between two sets A and B is the set that contains the elements of A and B that are not common.
