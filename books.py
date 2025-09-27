import data

livres = data.livres
aime_livres = data.aime_livres
users = data.utilisateurs

#q1
def sort_func(x):
    myList = list(x.items())
    return myList[1]
   
    
def triage_livre(livres):
    livres.sort(key=sort_func)
    return livres

#q2
def plus_ancien(livres):
    return (triage_livre(livres))[0]

def plus_recent(livres):
    return (triage_livre(livres))[-1]

#q3

def count_likes(aime_livres):
    dict_result = {}
    for i in aime_livres:
        count = 0
        for j in aime_livres:
            if i[1] == j[1]:
                count +=1
        dict_result[i[1]] = count
    return dict_result


def show_2_by_2(users):
    choix = '>'
    debut = 0
    fin = 2
    while True:
            print(f'livre de {debut} a {fin}\n')
            
            for i in range(debut , fin):
                print(users[i])
                
            print('\ntaper \'>\' pour passer au deux livre suivant ')
            print('taper autre chose pour quitter ')
            
            choix = input('votre choix : ')
            
            if choix.strip() == '>':
                debut +=2
                fin +=1
                if fin > len(triage_livre(livres)):
                    print('--------- la fin du liste -----------')
                    break
                elif fin < len(triage_livre(livres)):
                    fin +=1
                else:
                    pass
            else:
                break
            

# bonus 

def recherche_par_livre(livres):
    livre = input('donner le nom du livre souhaite : ')
    for i in livres:
        if livre in list(i.items())[0]:
            return i
        else:
            return '\nce livre n\'existe pas !!!\n'

def pair_name_age(users):
    nom_age = []
    for u in users:
        nom_age.append(tuple([u[1],u[-1]]))
    nom_age.sort(key=lambda x: x[1])
    return nom_age

