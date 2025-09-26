import data as d 

def utilisateursMajeurs():
   return list(filter(lambda x:x[3]>=18,d.utilisateurs))
