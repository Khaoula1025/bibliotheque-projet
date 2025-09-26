import data as d 

def utilisateursMajeurs():
   return list(filter(lambda x:x[3]>=18,d.utilisateurs))

def nomCompletMaj():
   return list(map(lambda x:x[2].upper(),d.utilisateurs))

def assosiationUtilisateursLivre():
   utilisateur_livre={}
   for i in d.utilisateurs:
     for j in d.aime_livres:
       if i[0]==j[0]:
             if i[1] not in utilisateur_livre:
              utilisateur_livre[i[1]]=[]
             utilisateur_livre[i[1]].append(j[1])
          
   return utilisateur_livre
def associateNamesWithFbooks(x):
       for i in d.utilisateurs:
        if i[1]==x[0]:
           return f'{i[1]} {i[2]} ({i[3]}ans ) aime {x[1]}'
def user_livre():
 
           
    #user_livre=list(map(lambda x:f'{i[1]} {i[2]} ({i[3]}ans ) aime {x[1]}'if x[0]==i[1] else '',assosiationUtilisateursLivre().items()))
      return list(map(associateNamesWithFbooks,assosiationUtilisateursLivre().items()))
        
print(user_livre())
#print(assosiationUtilisateursLivre().items())
