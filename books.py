import data

livres = data.livres

def sort_func(x):
    myList = list(x.items())
    return myList[1]
   
    
def traige_livre(livres):
    livres.sort(key=sort_func)
    return livres

def plus_ancien(livres):
    return (traige_livre(livres))[0]

def plus_recent(livres):
    return (traige_livre(livres))[-1]

new_dict ={ "1984": 2, "Le Petit Prince": 1, "Harry Potter": 1 } 

def addNewBook(livres):
    livres.append(new_dict)
    return livres

# print( addNewBook(livres))

def show_2_by_2(livres):
    choix = '>'
    debut = 0
    fin = 2
    while True:
            print(f'livre de {debut} a {fin}\n')
            for i in range(debut , fin):
                
                print((traige_livre(livres))[i])
            print('\ntaper \'>\' pour passer au deux livre suivant ')
            print('taper autre chose pour quitter ')
            choix = input('votre choix : ')
            if choix.strip() == '>':
                debut +=2
                fin +=2 
                if fin > len(traige_livre(livres)):
                    print('--------- la fin du liste -----------')
                    break
            else:
                break
            
show_2_by_2(livres)