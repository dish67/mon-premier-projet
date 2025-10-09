# mon-premier-projet

Projet de test DevOps avec Ubuntu et Codex.

## Explication du script `main.py`

Le script contient deux fonctions simples ainsi qu'une constante :

- `DEFAULT_NAME` stocke le prénom utilisé par défaut. Il est possible de passer un prénom différent à la fonction `bonjour` pour personnaliser le message.
- `bonjour(nom: str = DEFAULT_NAME) -> str` prépare une chaîne de caractères de bienvenue pour `nom`. La fonction renvoie la chaîne au lieu de l'afficher, ce qui la rend facile à réutiliser dans d'autres contextes (tests, interface graphique, etc.).
- `main() -> None` est le point d'entrée du programme. Lorsque le script est exécuté directement (c'est-à-dire que `__name__ == "__main__"`), cette fonction appelle `bonjour()` sans argument et affiche le message grâce à `print`.

L'expression `if __name__ == "__main__":` permet de n'exécuter `main()` que si le fichier est lancé comme script, et non lorsqu'il est importé dans un autre module Python.
