# progamme de calculateur de note d'un étudiant
print("🎓 Calculateur de Notes - Système Éducatif Togolais 🇹🇬")
print("="*30)

# l'étudiant saisi ces informations
print("\n👤 INFORMATIONS ÉTUDIANT")
print("_"*30)
nom_prenom = input("Nom et prénom de l'élève : ")
classe = input(f"Classe (ex: 3ème, 2nde, 1ère, Tle) : ")
etablissement = input("Etablissement : ")

# l'étudiant saisi ces notes du trimestre
print("\n📚 SAISIE DES NOTES DU TRIMESTRES (sur 20)")
print("_"*30)
mathem = float(input("📐 Mathématiques : "))
français = float(input("📝 Français : "))
Anglais = float(input("🇬🇧 Anglais : "))
PCT = float(input("⚗️ Scientifique Physique : "))
SVT = float(input("🧬 SVT (Science de la Vie) : "))
Histoire = float(input("🌍 Histoire-Géographie : "))

print("="*30)

print(f"📊 BULLETIN SCOLAIRE - {nom_prenom}")
print(f"{etablissement} - {classe} ")
print("="*30)

# affichage des notes du trimestre
print("\n📚 NOTES DU TRIMESTRE :")
print("_"*30)
print(f"📐 Mathématiques      : {mathem}/20 (écart: +{mathem - 10}) ")
print(f"📝 Français      : {français}/20 (écart: +{français - 10}) ")
print(f"🇬🇧 Anglais      : {Anglais}/20 (écart: +{Anglais - 10}) ")
print(f"⚗️ Sciences Physiques      : {PCT}/20 (écart: +{PCT - 10}) ")
print(f"🧬 SVT      : {SVT}/20 (écart: +{SVT - 10}) ")
print(f"🌍 Histoire-Géo      : {Histoire}/20 (écart: +{Histoire - 10}) ")

moyenne = (mathem + français + Anglais + PCT + SVT + Histoire) / 6
total_des_points = mathem + français + Anglais + PCT + SVT + Histoire
# affichage des resultats généraux
print("\n📊 RÉSULTATS GÉNÉRAUX :")
print("_"*30)
print(f"📈 Moyenne générale : {moyenne :.2f}/20")
print(f"📋 Total des points : {total_des_points}/120")

# Affichage des matières validées et non validées
print("\n✅ VALIDATION DES MATIÈRES (≥ 10/20) :")
print("_"*30)
print(f"📐 Mathématiques : {mathem >= 10} ")
print(f"📝 Français      : {français >= 10} ")
print(f"🇬🇧 Anglais      : {Anglais >= 10} ")
print(f"⚗️ Sc. Physiques : {PCT >= 10} ")
print(f"🧬 SVT           : {SVT >= 10} ")
print(f"🌍 Histoire-Géo  : {Histoire >= 10} ")

# Afichage de l'analyse pédagogique
profil_scientifique = mathem >= 14 and PCT >= 14 and SVT >= 14
profil_litteraire = français >= 14 and Anglais >= 14 and Histoire >= 14
print("\nANALYSES PÉDAGOGIQUES :")
print("_"*30)
print(f"📚 Matières fondamentales validées (Math ET Français) : {mathem >= 10 and français >= 10}")
print(f"🏆 Toutes matières validées : {mathem >= 10 and français >= 10 and Anglais >= 10 and PCT >= 10 and SVT >= 10 and Histoire >= 10}")
print(f"⭐ Au moins une matière validée : {mathem >= 10 or français >= 10 or Anglais >= 10 or PCT >= 10 or SVT >= 10 or Histoire >= 10}")
print(f"🔬 Profil scientifique : {profil_scientifique}")
print(f"📖 Profil littéraire : {profil_litteraire}")

# Affichage de la mention et décision
print("\n🏅 MENTIONS ET DÉCISIONS :")
print("_"*30)
print(f"🌟 Mention TRÈS BIEN (≥ 16) : {moyenne >= 16}")
print(f"⭐ Mention BIEN (≥ 14) : {moyenne >= 14}")
print(f"✨ Mention ASSEZ BIEN (≥ 12) : {moyenne >= 12}")
print(f"✅ ADMIS en classe supérieure (≥ 10) : {moyenne >= 10}")
print(f"❌ ÉCHEC (< 10) : {moyenne < 10}")
H
# Trouver et Affichage des matières dominante
print(f"Mathématiques en tête : {(mathem > PCT) and (mathem > français) and (mathem > Anglais) and (mathem > SVT) and (mathem > Histoire)}")
print(f"Français en tête : {(français > PCT) and (français > mathem) and (français > Anglais) and (français > SVT) and (français > Histoire)}")
print(f"Anglais en tête : {(Anglais > PCT) and (Anglais > français) and (Anglais > mathem) and (Anglais > SVT) and (Anglais > Histoire)}")
print(f"Scinces Physiques en tête : {(PCT > mathem) and (PCT > français) and (PCT > Anglais) and (PCT > SVT) and (PCT > Histoire)}")
print(f"Histoire-Géo en tête : {(Histoire > PCT) and (Histoire > français) and (Histoire > Anglais) and (Histoire > SVT) and (Histoire > mathem)}")
print(f"SVT en tête : {(SVT > PCT) and (SVT > français) and (SVT > Anglais) and (SVT > mathem) and (SVT > Histoire)}")


# Analyse approfondie
print("\n🔍 ANALYSES APPROFONDIES : ")
print("_"*30)
prometteur = moyenne >= 12 and not (mathem < 8 or français < 8)
echec = not (moyenne >= 10)
excellence = mathem >= 18 or français >= 18 or Anglais >= 18
print("🌟 Étudiant prometteur :", prometteur)
print(f"🔬 Orientation scientifique recommandée : {profil_scientifique}")
print(f"📚 Orientation littéraire recommandée : {profil_litteraire}")
print("🆘 Besoin de soutien scolaire : ", echec)
print("🏆 Candidat à l'excellence : ", excellence)

note_validee = mathem >= 10
math_meilleure = mathem > français and mathem > Anglais
note_parfaite = (mathem == 20 or français == 20 or Anglais == 20 or SVT == 20 or PCT == 20 or Histoire == 20)

# Les objectifs à atteindre
print("\n🎯 OBJECTIFS À ATTEINDRE :")
print("_"*30)
print(f"📊 Points pour la moyenne (10/20) : {10 - moyenne :.2f}")
print(f"✨ Points pour Assez Bien (12/20) : {12 - moyenne :.2f}")
print(f"⭐ Points pour Bien (14/20) : {14 - moyenne :.2f}")
print(f"🌟 Points pour Très Bien (16/20) : {16 - moyenne :.2f}")
print(f"Ne passe pas en classe supérieure : {moyenne < 10}")

#potentiel d'amelioration
print("\nPOTENTIEL D'AMELIORATION :")
print("_"*30)
print(f"📐Maths : {20 - mathem} points sont possibles")
print(f"📝Français : {20 - français} points sont possibles")
print(f"🇬🇧 Anglais : {20 - Anglais} points sont possibles")
print(f"⚗️Sciences Physiques : {20 - PCT} points sont possibles")
print(f"🧬SVT : {20 - SVT} points sont possibles")
print(f"🌍Géographie : {20 - Histoire} points sont possibles")

# Messsage de fin
print("\n🇹🇬 Bulletin établi selon le système éducatif togolais")
print(f"🎓 Bon courage {nom_prenom} pour la suite de tes études !")
print("💪 Travaille dur pour réussir ton parcours scolaire !")