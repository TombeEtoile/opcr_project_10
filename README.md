# SoftDesk Support API

## Description du Projet

SoftDesk, une société d'édition de logiciels de collaboration, a développé une application permettant de remonter et suivre des problèmes techniques, appelée SoftDesk Support. Cette solution est destinée aux entreprises B2B (Business to Business). L'API RESTful que vous avez construite constitue le back-end de cette application, offrant un moyen standard, performant et sécurisé pour gérer les données, accessible depuis diverses plateformes front-end.

## Fonctionnalités
Gestion des Projets : Créez, lisez, mettez à jour et supprimez des projets.
Gestion des Issues : Suivi des problèmes techniques associés à un projet.
Gestion des Commentaires : Ajout de commentaires aux issues pour une communication efficace.
Authentification Utilisateur : Enregistrement et gestion des utilisateurs, avec la possibilité de supprimer son compte (droit à l'oubli).
Sécurité : Utilisation de JWT pour l'authentification, assurant que seules les requêtes authentifiées peuvent accéder aux données sensibles.

## Installation

### Clonez ce repository :
```bash
git clone <url-du-repository>
cd <nom-du-dossier>
```

### Créez un environnement virtuel :
```bash
python3 -m venv env
source env/bin/activate  # Pour Linux/Mac
env\Scripts\activate  # Pour Windows
```

### Installez les dépendances requises :
```bash
pip install -r requirements.txt
```

### Appliquez les migrations pour configurer la base de données :
```bash
python manage.py migrate
```

### Créez un superutilisateur pour accéder à l'interface d'administration :
```bash
python manage.py createsuperuser
```

### Lancez le serveur de développement :
```bash
python manage.py runserver
```

## Endpoints

### Sommaire des Endpoints

__/ :__ Sommaire des URLs disponibles.

__/project/ :__ Liste des projets.

__/project/<int:pk>/ :__ Détail d'un projet spécifique.

__/issue/ :__ Liste des issues.

__/issue/<int:pk>/ :__ Détail d'une issue spécifique.

__/comment/ :__ Liste des commentaires.

__/api/user/delete/ :__ Suppression de l'utilisateur connecté (droit à l'oubli).

__/register/ :__ Enregistrement d'un nouvel utilisateur.

### Endpoints d'Authentification

__/api/token/ :__ Obtenir un token JWT pour s'authentifier.

__/api/token/refresh/ :__ Rafraîchir le token JWT.


## Dépendances

### Le projet utilise les dépendances suivantes :

```bash
asgiref==3.8.1
dj-rest-auth==6.0.0
Django==5.0.7
django-cors-headers==4.4.0
django-filter==24.2
djangorestframework==3.15.2
sqlparse==0.5.0
```

## Utilisation

### Accès aux Endpoints

Pour accéder aux différentes ressources de l'API, vous pouvez utiliser un outil comme Postman. Voici quelques exemples de requêtes :

#### Obtenir la liste des projets :

```bash
GET http://127.0.0.1:8000/project/
```

#### Obtenir le détail d'un projet :

```bash
GET http://127.0.0.1:8000/project/1/
```

#### Enregistrement d'un nouvel utilisateur :
```bash
POST http://127.0.0.1:8000/register/
```

Body :
```json
{
    "username": "exemple",
    "password": "motdepasse",
    "email": "exemple@domaine.com"
}
```

#### Suppression de l'utilisateur connecté :
```bash
DELETE http://127.0.0.1:8000/api/user/delete/
```

## Sécurité et Permissions

L'API utilise JWT pour l'authentification.
Les utilisateurs doivent être authentifiés pour accéder aux données sensibles.
Le droit à l'oubli est implémenté pour permettre aux utilisateurs de supprimer définitivement leurs données personnelles.


