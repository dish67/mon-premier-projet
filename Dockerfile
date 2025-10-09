# Étape 1 : Choisir une image de base avec Python
FROM python:3.11-slim

# Étape 2 : Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Étape 3 : Copier les fichiers du projet
COPY . .

# Étape 4 : Installer les dépendances
RUN pip install --upgrade pip && pip install -r requirements.txt

# Étape 5 : Lancer le script principal par défaut
CMD ["python", "src/main.py"]
