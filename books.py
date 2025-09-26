import data

livres = data.livres

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

new_dict ={ "1984": 2, "Le Petit Prince": 1, "Harry Potter": 1 } 

def addNewBook(livres):
    livres.append(new_dict)
    return livres


def show_2_by_2(livres):
    choix = '>'
    debut = 0
    fin = 2
    while True:
            print(f'livre de {debut} a {fin}\n')
            for i in range(debut , fin):
                
                print((triage_livre(livres))[i])
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
            
