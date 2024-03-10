## Clone

```$ git clone https://github.com/thimyxuan/streamlit-dashboard-car-rental-delay.git```

## Stack technique

- Python
- Numpy
- Pandas
- Plotly
- Streamlit

## Objet

Ce tableau de bord Streamlit résume les informations de l'analyse réalisée en Partie 1 du projet Getaround.

Il est déployé à l'adresse suvante : 
[`https://streamlit-getaround-e6d6a2216793.herokuapp.com/`](https://streamlit-getaround-e6d6a2216793.herokuapp.com/)

Vous pouvez retrouver l'ensemble du projet Getaround dans [ce repository](https://github.com/thimyxuan/car-rental-delay-analysis).

## Déploiement en local

Créer l'image Docker :

```$ docker build . -t streamlit_env```

Créer le container Docker : 

```$ docker run -it -v "$(pwd):/app" -p 4000:4000 streamlit_env```

## Déploiement avec Heroku

Assurez-vous d'être connecté à vos comptes Docker et Heroku : 

```$ heroku login```

```$ docker login --username=<your username> --password=$(heroku auth:token) registry.heroku.com```

```$ heroku create YOUR_APP_NAME```

```$ heroku container:push web -a YOUR_APP_NAME```

```$ heroku container:release web -a YOUR_APP_NAME```

```$ heroku open -a YOUR_APP_NAME```