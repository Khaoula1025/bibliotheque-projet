import users 
from data import utilisateurs
from data import aime_livres
print('les utilisateurs majeurs sont : ',users.utilisateursMajeurs(utilisateurs))
print('les utilisateurs des utilisateurs en majuscule: ',users.nomCompletMaj(utilisateurs))
print(users.assosiationUtilisateursLivre(utilisateurs,aime_livres))
print(users.user_livre(utilisateurs,aime_livres))
