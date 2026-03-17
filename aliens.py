import random

prefixe_comp=["zgl-","zb-","zd-","b-","z","g-","gl-","bl-","gz-","bz-"]
suffixe_comp=["b-","g-","l-"]
radical_comp=["b-x","g-x","l-x","gl-b","bl-b","gl-x","bl-x"]

voyelle=["a","ou","i","o","u"]

prefixe_tab=[]
suffixe_tab=[]
radical_tab=[]

for pcomp in prefixe_comp:
    for v in voyelle:
        prefixe_tab.append(pcomp.replace("-",v,1))
for scomp in suffixe_comp:
    for v in voyelle:
        suffixe_tab.append(scomp.replace("-",v,1))
for rcomp in radical_comp:
    for v in voyelle:
        radical_tab.append(rcomp.replace("-",v,1))

# print(prefixe_tab)
# print(suffixe_tab)
# print(radical_tab)

def new_alien_name(min_s, max_s):
    if (min_s != max_s):
        # print("min_x dif max_s", end =" ")
        snumber=random.randrange(min_s, max_s+1)-2
    else:
        # print("les memes donc ez", end =" ")
        snumber=min_s
    # print("snumber choisi ",snumber, end =" ")

    prefixe=prefixe_tab[random.randrange(0,len(prefixe_tab))]
    radical=radical_tab[random.randrange(0,len(radical_tab))]

    if(snumber<0):
        raise("problème avec la taille du nom au niveau du nombre de suffixes")
    elif(snumber==0):
        thing = ""+prefixe+radical
    else:
        name=""+prefixe
        for i in range(snumber):
            name+=suffixe_tab[random.randrange(0,len(suffixe_tab))]
        thing = name+radical

    print(thing, end =" ")
    return thing

def aliens(n,min_s,max_s): # size should be 2 or more
    if ((min_s < 2) or (max_s < 2)):
        raise("min_s ou max_s en dessous de 2")
    tab = n*[""]
    for j in range(len(tab)): # generation des noms
        tab[j] = new_alien_name(min_s, max_s)

aliens(100,2,3)

# while new_alien_name(4) != "baboubaglob":
#     print("pas de baboubaglob")