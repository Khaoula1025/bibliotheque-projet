import data as d 

def utilisateursMajeurs():
   return list(filter(lambda x:x[3]>=18,d.utilisateurs))

def nomCompletMaj():
   return list(map(lambda x:x[2].upper(),d.utilisateurs))

def assosiationUtilisateursLivre():
   utilisateur_livre={}
   for i in list(zip(d.utilisateurs,d.livres)) :
      utilisateur_livre[i[0][1]]=i[1]['titre']
   print(utilisateur_livre)
   