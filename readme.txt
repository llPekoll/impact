# Impact +


## install the packages
`pip install -r requirements.txt`  

## run the server
`uvicorn main:app --reload`  
then go to http://127.0.0.1:8000 using POST Request Method  

## Run the test
Just write `pytest` in the console  


## sample request
{
    "mock_for_test": [{
        "id": "c8e3-ace6-4852-a32f",
        "event": "video_25",
        "timestamp": 1617393003
    }, {
        "id": "af77-79b6-4fe6-8645",
        "event": "video_25",
        "timestamp": 1617400203
    }, {
        "id": "75c3-2a09-4ac6-a38a",
        "event": "video_25",
        "timestamp": 1617385803
    }, {
        "id": "a6dc-030b-4fb5-891d",
        "event": "video_50",
        "timestamp": 1617400203
    }, {
        "id": "9919-b79c-4897-b3e4",
        "event": "video_completed",
        "timestamp": 1617400203
    }, {
        "id": "d008-a738-45f3-a3fb",
        "event": "video_start",
        "timestamp": 1617385803
    }],
}


# Tips
- Vous pouvez utiliser n'importe quel module python externe pour faciliter l'exercice, mais pensez à inclure un fichier requirements.txt ou une doc pour installer l'environnement de travail.
- Préparez un repo gitlab/github que vous me partagerez pour cet exercice.
- On considère que les données en entrée de fonction ont la bonne forme, pas besoin de les valider.

# Python

## Manipulation de données
1- Ecrivez une fonction qui prend en entrée une liste de dict sous la forme :
[{"id": "xxxx-xxxx-xxxx-xxxx", "event": "impressions", "timestamp": 00000000000}, ...]
où :
- id est un identifiant d'évènement sous forme de string
- event peut prendre les valeurs "impressions", "video_start", "video_25", "video_50", "video_75", "video_completed"
- timestamp est un timestamp unix en secondes
Et qui va ressortir un tableau contenant le nombre d'évènements par heure (on considère que l'on est dans le fuseau GMT+1) et par type d'évènement, avec la date/heure en ligne et les évènements en colonne.

2- Ecrivez une fonction qui prend le tableau résultat de la fonction précédente, qui multiplie la colonne impressions par une constante c = 0.1, et qui rajoute le résultat sous la forme d'une nouvelle colonne.

3- Ecrivez une fonction qui prend le tableau résultat de la fonction précédente, et qui l'écrit dans un fichier .csv

4- Ecrivez une fonction qui prend les mêmes données que la fonction 1 en entrée, et qui retourne la liste des identifiants "id" uniques du tableau d'entrée.

## Tests
Ecrivez un test pertinent pour les fonctions 1, 2 et 4 avec le framework de test de votre choix

# API
Ecrivez une API basique avec le framework de votre choix.
Cette api contient un seul point d'entrée qui accepte les requêtes POST et qui prend les données dans le corps de la requête, qui appelle les fonctions 1, 2 et 3 et qui retourne le fichier CSV correspondant.