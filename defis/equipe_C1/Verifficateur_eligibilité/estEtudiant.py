print("=== Vérificateur d'éligibilité UL ===")
Age = int(input("Age :"))
Mention = input("Mention au BAC : ")
inscrit = input("Inscrit à l'UL (Oui/Non) :")
nation = input("Nationalité : ") 

critAge = Age <= 22
critMention = (Mention == "Tres Bien") or (Mention == "Assez Bien") or (Mention == "Bien")
critinscrit = (inscrit == "Oui")
critnation = (nation == "Togolaise")

eligible = critAge and critMention and critinscrit and critnation

print("\n=== Résultat ===")
print("Age <=22 : ", critAge)
print("Mention Bien ou Tres Bien : ", critMention)
print("Inscrit à l'UL : ", critinscrit)
print("Nationalité Togolaise : ", critnation)
print("\nÉligibilité générale (tous critères vrais) : ", eligible)