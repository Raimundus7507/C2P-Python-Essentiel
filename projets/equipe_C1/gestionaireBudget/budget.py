def main():
    print("=== GESTIONNAIRE DE BUDGET PERSONNEL ===\n")
    print("Bonjour ! Je vais t'aider à gérer ton budget mensuel.\n")
    input("\nSi tu est pret appuie sur continuer...")
    continuer = True
    while continuer:
        revenu = demander_montant("💰 Quel est ton revenu mensuel ? ")
        depenses, logement, nourriture, transport, loisirs = saisir_depenses()
        reste = calculer_reste(revenu, depenses)
        conseil = donner_conseil(revenu, reste)
        afficher_recap(revenu, depenses, reste, logement, nourriture, transport, loisirs, conseil)
        refaire = input("Veux-tu refaire un calcul ? (oui/non) ").strip().lower()
        if refaire != "oui":
            continuer = False
    print("\nMerci d'avoir utilisé le gestionnaire de budget ! 👋")

def demander_montant(message):
    montant = -1
    while montant < 0:
        entree = input(message)
        if entree.replace('.', '', 1).isdigit():
            montant = float(entree)
            if montant < 0:
                print("Veuillez entrer un montant positif.")
        else:
            print("Entrée invalide. Veuillez saisir un nombre.")
    return montant

def saisir_depenses():
    logement = demander_montant("🏠 Combien dépenses-tu pour le logement ? ")
    nourriture = demander_montant("🍕 Budget nourriture mensuel ? ")
    transport = demander_montant("🚗 Ton Transport  ? ")
    loisirs = demander_montant("🎬 Budget  loisirs ? ")
    total_depenses = logement + nourriture + transport + loisirs
    return total_depenses, logement, nourriture, transport, loisirs

def calculer_reste(revenu, depenses):
    return revenu - depenses

def donner_conseil(revenu, reste):
    if revenu == 0:
        return "Attention, tu n'as pas de revenu ce mois-ci."
    pourcentage = (reste / revenu) * 100
    if reste < 0:
        return "Tu dépenses plus que tes revenus ! Attention au découvert."
    elif pourcentage < 10:
        return "Situation critique : essaie de réduire tes dépenses."
    elif pourcentage < 30:
        return "Tu économises peu, essaie d'optimiser ton budget."
    elif pourcentage < 60:
        return "Bonne gestion ! Tu peux envisager d'épargner davantage."
    else:
        return "Excellent ! Tu économises {:.0f}% de tes revenus. Continue comme ça, tu peux te faire plaisir ou épargner !".format(pourcentage)

def afficher_recap(revenu, depenses, reste, logement, nourriture, transport, loisirs, conseil):
    """Affiche un résumé clair et lisible du budget."""
    print("\n📊 === RÉCAPITULATIF DE TON BUDGET ===\n")
    print("Revenus : {:.0f} Fcfa".format(revenu))
    print("Dépenses totales : {:.0f} Fcfa".format(depenses))
    print("  - Logement : {:.0f} Fcfa".format(logement))
    print("  - Nourriture : {:.0f} Fcfa".format(nourriture))
    print("  - Transport : {:.0f} Fcfa".format(transport))
    print("  - Loisirs : {:.0f} Fcfa".format(loisirs))
    print("Reste disponible : {:.0f} Fcfa".format(reste))
    print("\nConseil : " + conseil + "\n")


main()