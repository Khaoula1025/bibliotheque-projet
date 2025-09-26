import data
import books

livres = data.livres
users = data.utilisateurs
aime_livres = data.aime_livres

# books

print(books.count_likes(aime_livres))
# books.show_2_by_2(livres)
# print(books.recherche_par_livre(livres))

# users

# print('les utilisateurs majeurs sont : ',users.utilisateursMajeurs(users))
# print('les utilisateurs des utilisateurs en majuscule: ',users.nomCompletMaj(users))
print(users.assosiationUtilisateursLivre(users,aime_livres))
#print(users.user_livre(users,aime_livres))