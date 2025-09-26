import data as d 

def utilisateursMajeurs(utilisateurs):
   return list(filter(lambda x:x[3]>=18,utilisateurs))

def nomCompletMaj(utilisateurs):
   return list(map(lambda x:x[2].upper(),utilisateurs))

def assosiationUtilisateursLivre(utilisateurs,aime_livres):
   utilisateur_livre={}
   for i in utilisateurs:
     for j in aime_livres:
       if i[0]==j[0]:
             if i[1] not in utilisateur_livre:
              utilisateur_livre[i[1]]=[]
             utilisateur_livre[i[1]].append(j[1])
          
   return utilisateur_livre
def associateNamesWithFbooks(x):
       for i in d.utilisateurs:
        if i[1]==x[0]:
           return f'{i[1]} {i[2]} ({i[3]}ans ) aime {x[1]}'
def user_livre(utilisateurs,aime_livres):
       return list(map(associateNamesWithFbooks,assosiationUtilisateursLivre(utilisateurs,aime_livres).items()))

