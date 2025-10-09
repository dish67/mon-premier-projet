#!/usr/bin/env python3
"""Script d'accueil minimaliste utilisé pour vérifier l'environnement Python."""

DEFAULT_NAME: str = "Michel"


def bonjour(nom: str = DEFAULT_NAME) -> str:
    """Construit le message d'accueil destiné à ``nom``."""

    return (
        f"👋 Bonjour {nom} ! Ceci est ton premier script Python depuis Ubuntu WSL2 et GitHub."
    )


def main() -> None:
    """Point d'entrée du script qui affiche le message d'accueil."""

    print(bonjour())


if __name__ == "__main__":
    main()
