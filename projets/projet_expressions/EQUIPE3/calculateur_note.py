# 🎓 Calculateur de Notes - Système Éducatif Togolais 🇹🇬
print("🎓 CALCULATEUR DE NOTES - SYSTÈME ÉDUCATIF TOGOLAIS 🇹🇬")
print("="*55)

# 🔥 Étape 1 : Informations de l'élève nom, classe, etablissement
nom = input("Nom et prénom de l'élève : ")
classe = input("Classe (ex: 3ème, 2nde, Tle) : ")
etab = input("Établissement : ")

# Saisie des notes des matières
print("\n📚 SAISIE DES NOTES DU TRIMESTRE (sur 20)")
math = float(input("📐 Mathématiques : "))
francais = float(input("📝 Français : "))
anglais = float(input("🇬🇧 Anglais : "))
sciences = float(input("⚗️ Sciences Physiques : "))
svt = float(input("🧬 SVT : "))
histoire = float(input("🌍 Histoire-Géographie : "))

# 🧮 Étape 2 : Calculs arithmétiques
total = math + francais + anglais + sciences + svt + histoire
moyenne = total / 6

# Écarts par rapport à 10
ecart_math = math - 10
ecart_fr = francais - 10
ecart_ang = anglais - 10
ecart_sci = sciences - 10
ecart_svt = svt - 10
ecart_hist = histoire - 10

# Progression pour atteindre 20
prog_math = 20 - math
prog_fr = 20 - francais
prog_ang = 20 - anglais
prog_sci = 20 - sciences
prog_svt = 20 - svt
prog_hist = 20 - histoire

# ⚖️ Étape 3 : Comparaisons
valide_math = math >= 10
valide_fr = francais >= 10
valide_ang = anglais >= 10
valide_sci = sciences >= 10
valide_svt = svt >= 10
valide_hist = histoire >= 10

# Mentions
if moyenne >= 16:
    mention = "Très Bien"
elif moyenne >= 14:
    mention = "Bien"
elif moyenne >= 12:
    mention = "Assez Bien"
elif moyenne >= 10:
    mention = "Passable"
else:
    mention = "Échec"

# Matière dominante
if francais > math and francais > anglais and francais > sciences and francais > svt and francais > histoire:
    meilleure = "Français"
elif anglais > math and anglais > francais and anglais > sciences and anglais > svt and anglais > histoire:
    meilleure = "Anglais"
elif sciences > math and sciences > francais and sciences > anglais and sciences > svt and sciences > histoire:
    meilleure = "Sciences Physiques"
elif svt > math and svt > francais and svt > anglais and svt > sciences and svt > histoire:
    meilleure = "SVT"
elif histoire > math and histoire > francais and histoire > anglais and histoire > sciences and histoire > svt:
    meilleure = "Histoire-Géographie"
else:
    meilleure = "Mathématiques"

# 🔗 Étape 4 : Expressions logiques complexes
fondamentales = math >= 10 and francais >= 10
toutes_validees = valide_math and valide_fr and valide_ang and valide_sci and valide_svt and valide_hist
profil_sci = math >= 14 and sciences >= 14
profil_litt = francais >= 14 and histoire >= 14
profil_equilibre = profil_sci and profil_litt
excellence = math >= 18 or francais >= 18 or anglais >= 18 or sciences >= 18 or svt >= 18 or histoire >= 18
echec = not (moyenne >= 10)

# 📊 Étape 5 : Affichage du bulletin
print("\n" + "="*35)
print(f"📊 BULLETIN SCOLAIRE - {nom}")
print(f"🏫 {etab} - {classe}")
print("="*35)

print("\n📚 NOTES DU TRIMESTRE :")
print(f"📐 Mathématiques       : {math}/20 (écart: {ecart_math:+.1f}, progression possible: {prog_math:.1f})")
print(f"📝 Français            : {francais}/20 (écart: {ecart_fr:+.1f}, progression possible: {prog_fr:.1f})")
print(f"🇬🇧 Anglais              : {anglais}/20 (écart: {ecart_ang:+.1f}, progression possible: {prog_ang:.1f})")
print(f"⚗️ Sciences Physiques  : {sciences}/20 (écart: {ecart_sci:+.1f}, progression possible: {prog_sci:.1f})")
print(f"🧬 SVT                 : {svt}/20 (écart: {ecart_svt:+.1f}, progression possible: {prog_svt:.1f})")
print(f"🌍 Histoire-Géographie : {histoire}/20 (écart: {ecart_hist:+.1f}, progression possible: {prog_hist:.1f})")

print("\n📊 RÉSULTATS GÉNÉRAUX :")
print(f"📈 Moyenne générale : {moyenne:.2f}/20")
print(f"📋 Total des points : {total}/120")
print(f"🏅 Mention : {mention}")

print("\n✅ VALIDATION DES MATIÈRES (≥ 10/20) :")
print(f"Mathématiques : {valide_math}")
print(f"Français      : {valide_fr}")
print(f"Anglais       : {valide_ang}")
print(f"Sc. Physiques : {valide_sci}")
print(f"SVT           : {valide_svt}")
print(f"Histoire-Géo  : {valide_hist}")

print("\n🔍 ANALYSES PÉDAGOGIQUES :")
print(f"Matières fondamentales validées (Math ET Français) : {fondamentales}")
print(f"Toutes matières validées : {toutes_validees}")
print(f"Profil scientifique fort : {profil_sci}")
print(f"Profil littéraire fort   : {profil_litt}")
print(f"Profil équilibré         : {profil_equilibre}")
print(f"Excellence (≥18 dans au moins une matière) : {excellence}")
print(f"Échec (moyenne < 10) : {echec}")

print("\n🥇 Matière dominante :", meilleure)

print("\n🇹🇬 Bulletin établi selon le système éducatif togolais")
print(f"🎓 Bon courage {nom} pour la suite de tes études ! 💪")