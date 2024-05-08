# Fonction pour évaluer une formule logique avec une valuation donnée
def evaluer_formule(formule, valuation):
    # Fonction pour évaluer un opérateur logique
    def evaluer_operateur(op, a, b):
        if op == '&':
            return a and b
        elif op == '|':
            return a or b
        elif op == '~':
            return not a
        elif op == '>>':
            return (not a) or b
        elif op == '=':
            return a == b

    # Fonction pour évaluer une expression logique récursivement
    def evaluer(expression, valuation):
        if len(expression) == 1:  # Cas de base : la formule est une variable
            return valuation[expression[0]]  # Utiliser une liste pour indexer
        else:
            op = expression[0]
            a = evaluer(expression[1], valuation)
            b = evaluer(expression[2], valuation) if len(expression) == 3 else None
            return evaluer_operateur(op, a, b)

    # Diviser la formule en ses parties (opérateurs et variables)
    parts = []
    part = ''
    for char in formule:
        if char in ['&', '|', '~', '>', '=']:
            parts.append(part)
            parts.append(char)
            part = ''
        else:
            part += char
    parts.append(part)

    # Évaluer l'expression logique
    return evaluer(parts, valuation)


# Fonction pour générer toutes les valuations possibles pour un ensemble de variables
def generer_valuations(variables):
    valuations = []
    n = len(variables)
    for i in range(2 ** n):
        valuation = {variables[j]: bool((i >> j) & 1) for j in range(n)}
        valuations.append(valuation)
    return valuations

# Fonction pour vérifier si KB |= alpha
def verifie_satisfiabilite(KB, alpha):
    variables = list(set("".join(KB) + alpha))
    valuations = generer_valuations(variables)
    satisfiable = True

    for valuation in valuations:
        kb_eval = all(evaluer_formule(formule, valuation) for formule in KB)
        alpha_eval = evaluer_formule(alpha, valuation)

        # Vérifier si KB est vrai et alpha est faux dans la valuation actuelle
        if kb_eval and not alpha_eval:
            satisfiable = False
            break

    return satisfiable

# Fonction principale
def main():

    # Affichage de la table de correspondance des connecteurs logiques
    print("Tableau de correspondance des connecteurs logiques")
    print("+-----------------+---------+")
    print("| Connecteur      | Symbole |")
    print("+-----------------+---------+")
    print("| Négation (¬)    | ~       |")
    print("| Conjonction (∧) | &       |")
    print("| Disjonction (∨) | |       |")
    print("| Implication (→) | >>      |")
    print("| Équivalence (↔) | =       |")
    print("+-----------------+---------+\n")

    print("-----Taper votre formule-----")
    print("Exemple KB |= α: KB1 = A, KB2 = A | B, alpha = A | B | C\n")
    print("Exemple KB /|= α: KB1 = A & B, KB2 = ~C, alpha = A | C\n")

    # Demander le nombre de formules pour KB
    while True:
        try:
            nb_formules_KB = int(input("Entrer le nombre de formules pour KB: "))
            break
        except ValueError:
            print("Veuillez entrer un nombre.")

    KB = []
    # Demander les formules pour KB
    for i in range(nb_formules_KB):
        formule = input(f"Entrez la formule {i+1} de KB : ").strip()
        KB.append(formule)

    # Demander la formule pour alpha
    alpha = input("Entrez la formule de Alpha : ").strip()

    # Vérifier si KB |= alpha
    satisfiable = verifie_satisfiabilite(KB, alpha)

    if satisfiable:
        print("KB |= alpha")
    else:
        print("KB /|= alpha")

if __name__ == "__main__":
    main()
