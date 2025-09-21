# Calculateur de notes

# Demande de l'information de l'etudiant

No_preno=input("Entrez votre Nom et Prénom:")
Cla=input("Entrez votre niveau (3ème,2nde,1ère,Tle):")
Etabl=input("Entrez l'établissement de provenance:")

print("--"*55)

    #Saisie des notes du trimestre
print("SAISIE DES NOTES DU TRIMESTRE(sur 20)")

Math=float(input("Entrez la note en Mathématique:"))
Scien_phy=float(input("Entrez la note de Sciences Physique:"))
Svt=float(input("Entrez la note de SVT:"))

Hist_Geo=float(input("Entrez la note de Histoire et Géographie:"))

Fran=float(input("Entrez la note de Français:"))
Ang=float(input("Entrez la note d'Anglais:"))

# CALCULS DES DONNEES
    # CALCUL de la moyenne général sur les 6 matière

Moy_Gen=((Math+Scien_phy+Svt+Hist_Geo+Fran+Ang)/6)
    # TOTAL DES POINTS

Tot_pts=(Math+Scien_phy+Svt+Hist_Geo+Fran+Ang)

    # ECART DE CHAQUE NOTE PAR RAPPORT A 10

Ec_Math=float(Math-10)
Ec_Scien_Phy=float(Scien_phy-10)
Ec_Svt=float(Svt-10)
Ec_Hist_Geo=float(Hist_Geo-10)
Ec_Fran=float(Fran-10)
Ec_Ang=float(Ang-10)

    # PROGRESSION DANS CHAQUE MATIERE
pro_Math=float(20-Math)
pro_Scien_phy=float(20-Scien_phy)
pro_Svt=float(20-Svt)
pro_Hist_Geo=float(20-Hist_Geo)
pro_Fran=float(20-Fran)
pro_Ang=float(20-Ang)
    # points nécessaires pour atteindre 10,12,14,16
pt_manq_10=(10-Moy_Gen)
pt_manq_12=(12-Moy_Gen)
pt_manq_14=(14-Moy_Gen)
pt_manq_16=(16-Moy_Gen)

# ETAPE 4: Expression de comparaison
    # Vérification des matières validées
V_Math= Math>=10
V_Scien_phy=Scien_phy>=10
V_Svt=Svt>=10
V_Hist_Geo=Hist_Geo>=10
V_Fran=Fran>=10
V_Ang=Ang>=10

    # Verification de la moyenne

V_moy_16= Moy_Gen>=16
V_moy_14= Moy_Gen>=14
V_moy_12= Moy_Gen>=12
V_moy_10= Moy_Gen>=10
V_moy_in10=Moy_Gen<=10

    # La meilleur matière

meill_Math=(Math>Scien_phy) and (Math>Svt) and (Math>Hist_Geo) and (Math>Fran) and (Math>Ang)
meill_Scien_phy=(Scien_phy>Math) and (Scien_phy>Svt) and (Scien_phy>Hist_Geo) and (Scien_phy>Fran) and (Scien_phy>Ang)
meill_Svt=(Svt>Math) and (Svt>Scien_phy) and (Svt>Hist_Geo) and (Svt>Fran) and (Svt>Ang)
meill_Hist_Geo=(Hist_Geo>Math) and (Hist_Geo>Scien_phy) and (Hist_Geo>Svt) and (Hist_Geo>Fran) and (Hist_Geo>Ang)
meill_Fran=(Fran>Math) and (Fran>Scien_phy) and (Fran>Svt) and (Fran>Hist_Geo) and (Fran>Ang)
meill_Ang=(Ang>Math) and (Ang>Scien_phy) and (Ang>Svt) and (Ang>Hist_Geo) and (Ang>Fran)

    # Note parfaite=20

note= Math or Scien_phy or Svt or Hist_Geo or Fran or Ang
note_parf= note==20
    # Note critique <5

note_critq= note <=5

# EATPE 5: EXPRESSIONS LOGIQUES

    #Matières fondamentales validées
Mat_fonda=((Math>=10) and (Fran>=10))

    # Toutes matières validées

Mats=(Math and Scien_phy and Svt and Hist_Geo and Fran and Ang )
V_Mats=Mats>=10

    # Profil scientifique fort

Pro_Scien=((Math and Scien_phy and Svt)>=10)

    # Profil littéraire
Pro_lit=((Fran and Hist_Geo)>=10)

Pro_equili= Pro_Scien and Pro_lit

    # Logique OU
Mats_1=((Math or Scien_phy or Svt or Hist_Geo or Fran or Ang)>=10) # Au moins validé une matière

Mats_2=((Math or Scien_phy or Svt or Hist_Geo or Fran or Ang)>=18) # Au mois 18 dans une matière

Mats_3=((Math or Scien_phy or Svt or Hist_Geo or Fran or Ang)<=5) # Difficulté majeur rencontré

    # Logique Not

Ne_Pass_Sup= (not(Moy_Gen>=10))
N_Mention= (not(Moy_Gen>=10))
N_Mats= not((Math and Scien_phy and Svt and Hist_Geo and Fran and Ang)>=10)

    # EXPRESSIONS COMPLEXE

promoteur=(Moy_Gen>=12 and not(Math<8 or Fran<8))
b_sout=(Moy_Gen<10)
C_Ex=14<Moy_Gen<16

# ETAPE 6:AFFICHAGE DU BULLETIN
print(f"\tCalculateur de Notes -Systèmes Educatif Togolais\n")
print("=="*55)

print(f"\t🎓INFORMATIONS DE L'ETUDIANT\n")
print(f"Nom et Prénom de l'étudiant:{No_preno}")
print(f"Niveau d'étude:{Cla}")
print(f"Etablissement:{Etabl}")

print("--"*55)

print("SAISIE DES NOTES DU TRIMESTRE(sur 20)\n")

print(f"📐Mathématique:{Math:.2f}\n")
print(f"📗Français: {round(Fran, 2)}\n")
print(f"📕Anglais: {round(Ang, 2)}\n")
print(f"🔍Sciences physiques: {round(Scien_phy, 2)}\n")
print(f"🧬SVT (Sciences de la Vie et de la Terre): {round(Svt, 2)}\n")
print(f"📚Histoire et Géographie: {round(Hist_Geo,2)}\n")

print("--"*55)
print(f"📊BULLETIN SCOLAIRE-{No_preno}")
print(f"Lycée {Etabl}-{Cla}")
print("--"*55)

print(f"\tNOTE DU TRIMESTRE:\n")

print(f"📐Mathématique: {round(Math, 2)}/20 (écart: {round(Ec_Math, 2)})\n")
print(f"📗Français: {round(Fran, 2)}/20 (écart: {round(Ec_Fran, 2)})\n")
print(f"📕Anglais: {round(Ang, 2)}/20 (écart: {round(Ec_Ang, 2)})\n")
print(f"🔍Sciences physiques: {round(Scien_phy, 2)}/20 (écart: {round(Ec_Scien_Phy, 2)})\n")
print(f"🧬SVT: {round(Svt, 2)}/20 (écart: {round(Ec_Svt, 2)})\n")
print(f"📚Histoire et Géographie: {round(Hist_Geo, 2)}/20 (écart: {round(Ec_Hist_Geo,2)})\n")

print("--"*55)

print("--\tRESULTATS GENERAUX:--\n")
print(f"Moyenne générale:{Moy_Gen:.2f}/20\n")
print(f"Total des points:{Tot_pts:.2f}/120\n")

print("--"*55)

print(f"\t--VALIDATION DES MATIERES(>=10)--\n")

print("📐Mathématique:",V_Math)
print("📗Français:",V_Fran)
print("📕Anglais:",V_Ang)
print("🔍Sciences physiques:",V_Scien_phy)
print("🧬SVT:",V_Svt)
print(f"📚Histoire et Géographie:{V_Hist_Geo}\n")

print("--"*55)

print("\t--ANALYSE PEDAGOGIQUE--\n")
print("Matière fondamentale validé(MATH et FRANCAIS):",Mat_fonda)
print("🏆Toutes les matières validées:",V_Mats)
print("✨Au moins une matière validée:",Mats_1)
print("🔬Profil Scientifique:",Pro_Scien)
print("📖Profil littéraire:",Pro_lit)
print(f"⚖️Profil équilibré:{Pro_equili}\n")

print("--"*55)

print("--\tMENTIONS ET DECISIONS:--\n")

print("🏅Mention Très Bien:",V_moy_16)
print("🏅Mention Bien:",V_moy_14)
print("🥉Mention Assez Bien:",V_moy_12)
print("🥈Mention  Passable:",V_moy_10)
AD=Moy_Gen>=10
print("✅ADMIS en Classe supérieure (>=10):",AD)
print(f"❌ECHEC(<10):{Ne_Pass_Sup}\n")

print("--"*55)

print(f"\t--MATIERE DOMINANTE:--\n")

print("📐Mathématique en tête:",meill_Math)
print("📗Français en tête:",meill_Fran)
print("📕Anglais en tête:",meill_Ang)
print("🧬SVT en tête:",meill_Svt)
print("🔍Sciences physique en tête:",meill_Scien_phy)
print(f"📚Histoire et Géographie en tête:{meill_Hist_Geo}\n")

print("--"*55)

print(f"\t--🔍ANALYSE APPROFONDI:--\n")
print("Etudiant prometteur:",promoteur)
print("Orientation scientifique recommandé:",Pro_Scien)
print("Orientation littéraire:",Pro_lit)
print("Besoin d'un soutien scolaire:",b_sout)
print(f"Candidat à l'excellence:{C_Ex}\n")

print("--"*55)
print("\t--OBJECTIFS A ATTEINDRE--\n")
print(f"📊Point pour avoir la moyenne (10/20): {round(pt_manq_10, 2)}")
print(f"✨Point pour avoir Assez Bien (12/20): {round(pt_manq_12, 2)}")
print(f"Point pour avoir Bien (14/20): {round(pt_manq_14, 2)}")
print(f"Point pour avoir Très Bien (16/20): {round(pt_manq_16,2)}\n")

print("--"*55)

print(f"\t--POTENTIEL D'AMELIORATION:--\n")

print(f"📐Mathématique: {pro_Math:.2f} points possibles")
print(f"📗Français: {pro_Fran:.2f} points possibles")
print(f"📕Anglais: {pro_Ang:.2f} points possibles")
print(f"🔍Sciences physique: {pro_Scien_phy:.2f} points possibles")
print(f"🧬SVT: {pro_Svt:.2f} points possibles")
print(f"📚Histoire et Géographie: {pro_Hist_Geo:.2f} points possibles\n")

print("--"*55)

print(f"\t--Bulletin établi selon le système éducatif togolais--\n")
print(f"🔨Bon courage {No_preno} pour la suite de tes etudes ! ")
print("💪Travaille dur pour réussir ton parcours scolaire !")