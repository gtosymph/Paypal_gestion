# Utilise une image Python Alpine minimaliste
FROM python:3.9-alpine

# Installer les dépendances système requises pour requests et SSL
RUN apk add --no-cache \
    build-base \
    libffi-dev \
    openssl-dev \
    && rm -rf /var/cache/apk/*

# Définit le répertoire de travail
WORKDIR /app

# Copie et installe les dépendances Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie le script Python
COPY main.py .

# Point d’entrée : exécute le script
CMD ["python", "main.py"]
