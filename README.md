# Logic-formula-evaluator

Ce projet implémente une série de fonctions pour évaluer des formules logiques en utilisant une valuation donnée. Il fournit également une fonctionnalité pour vérifier si un ensemble de formules (KB) satisfait une autre formule (alpha) dans la logique propositionnelle.

## Fonctionnalités principales
1. `Évaluation de formules logiques` : La fonction evaluer_formule(formule, valuation) évalue une formule logique donnée en utilisant une valuation spécifique.

2. `Génération de valuations possibles` : La fonction generer_valuations(variables) génère toutes les valuations possibles pour un ensemble de variables données.

3. `Vérification de la satisfiabilité` : La fonction verifie_satisfiabilite(KB, alpha) vérifie si un ensemble de formules (KB) satisfait une autre formule (alpha) dans la logique propositionnelle.

## Installation de Python

Pour exécuter ce programme, vous aurez besoin d'installer Python sur votre système. Voici comment installer Python sur différents systèmes d'exploitation :

### Windows

1. Téléchargez le programme d'installation Python à partir du [site officiel de Python](https://www.python.org/downloads/).
2. Exécutez le programme d'installation téléchargé.
3. Cochez la case "Add Python X.X to PATH" pendant le processus d'installation (où X.X représente la version de Python).
4. Cliquez sur "Install Now" pour lancer l'installation.
5. Une fois l'installation terminée, Python sera disponible dans l'invite de commande.

### macOS

1. macOS est livré avec une version de Python préinstallée. Vous pouvez vérifier la version en ouvrant le Terminal et en tapant `python --version`.
2. Pour installer une version plus récente, vous pouvez utiliser [Homebrew](https://brew.sh/). Ouvrez le Terminal et exécutez la commande suivante :

```
brew install python
```

3. Une fois l'installation terminée, la nouvelle version de Python sera disponible.

### Linux

1. De nombreuses distributions Linux sont livrées avec Python préinstallé. Vous pouvez vérifier la version en ouvrant un terminal et en tapant `python --version`.
2. Pour installer Python sur les distributions basées sur Debian (comme Ubuntu), vous pouvez utiliser apt. Ouvrez un terminal et exécutez la commande suivante :

```
sudo apt update
sudo apt install python3
```

Remplacez `python3` par `python` si vous voulez installer la version 2.
3. Pour d'autres distributions Linux, vous pouvez utiliser le gestionnaire de packages spécifique à la distribution pour installer Python.

Une fois Python installé, vous pouvez exécuter le programme en suivant les instructions fournies dans la section "Utilisation" ci-dessus.


4. (Optionnel) Si vous préférez travailler dans un environnement virtuel, vous pouvez le créer en utilisant les étapes suivantes :
    ```
    python -m venv venv
    source venv/bin/activate  # Pour Linux/macOS
    .\venv\Scripts\activate   # Pour Windows
    ```

## Utilisation

1. Exécutez le script Python dans un terminal en tapant cet commande dans un terminal :

  ```
  python eval_logic.py #Python
  python3 eval_logic.py #Python3
  ```

2. **Tableau de correspondance des connecteurs logiques :** Au démarrage du programme, une table de correspondance des connecteurs logiques est affichée pour référence.

3. **Entrée de formules logiques :** L'utilisateur est invité à entrer le nombre de formules pour KB, les formules pour KB et la formule pour alpha.

4. **Exemple :**
   - Pour une formule KB |= α, l'utilisateur peut entrer les formules de la forme "KB1 = A, KB2 = A | B, alpha = A | B | C".
   - Pour une formule KB /|= α, l'utilisateur peut entrer les formules de la forme "KB1 = A & B, KB2 = ~C, alpha = A | C".

5. **Affichage du résultat :** Le programme affiche si KB satisfait ou ne satisfait pas α.



## Exemple d'utilisation

```
-----Taper votre formule-----

Exemple KB |= α: KB1 = A, KB2 = A | B, alpha = A | B | C

Exemple KB /|= α: KB1 = A & B, KB2 = ~C, alpha = A | C

Entrer le nombre de formules pour KB: 2
Entrez la formule 1 de KB : A
Entrez la formule 2 de KB : A | B
Entrez la formule de Alpha : A | B | C

KB |= alpha

```

## Structure du Projet

- `AnalyseurSyntaxique.py` : Code du projet `verificateur-syntaxique`. Utilisé pour la saisie des formules de KB et alpha
- `Grammaire.py` : Contient le lexer et le parser PLY pour analyser les formules logiques
- `Inference.py` : Le script principal qui gère l'interaction avec l'utilisateur et le système d'inférence de propositions.

## Bibliothèque
Vous n'avez pas besoin de bibliothèques pour utiliser ce sript.



