#!/usr/bin/env python3

DEFAULT_NAME = "Michel"

def bonjour(name: str = DEFAULT_NAME) -> str:
    message = f"👋 Bonjour {name} ! Ceci est ton premier projet Python structuré."
    print(message)
    return message

if __name__ == "__main__":
    bonjour()

