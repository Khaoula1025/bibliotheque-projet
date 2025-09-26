import data as d 

def utilisateursMajeurs():
   return list(filter(lambda x:x[3]>=18,d.utilisateurs))

def nomCompletMaj():
   return list(map(lambda x:x[2].upper(),d.utilisateurs))

