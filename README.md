### Solution

1. Clone repository locally from:

    cd  # to cloned repo

2. Create virtualenv locally and install requirements:

    pip install -r requirements.txt

3. Generate your omdb api key from: http://www.omdbapi.com/apikey.aspx and export it in your console:

    export OMDB_API_KEY=[your_api_key]

4. Set up db:

    ./manage.py makemigrations
    ./manage.py migrate

5. Run your application locally:

    ./manage.py runserver

6. Check your application on `127.0.0.1:8000`

7. Run tests:

    OMDB_API_KEY=[your_api_key] ./manage.py test apps


### Using API
Application is hosted publicly on http://djangomovies.brak.me.

You can use it via your console using `curl`, `http` or other of your choice or via browser.
If you want check it locally, just change http://djangomovies.brak.me to 127.0.0.1:8000 
after setting it up on your computer.

- POST /movies/
Add movies to db requires only movie title. Description will be automatically fetched from OMDB.
`http POST http://djangomovies.brak.me/movies/ title=[your_movie_title]`

- GET /movies/
Will show all movies in db ordered by data added descending.
`http http://djangomovies.brak.me/movies/`

- GET /comments/
Will show all comments in db ordered by data added descending.
`http http://djangomovies.brak.me/comments/`

- GET /comments/?movie_id=[your_movie_id]
Will show all comments associated movie with passed id.
`http http://djangomovies.brak.me/comments/?movie_id=1`

- POST /comments/
Add comment to a movie by passing comment text and movie id to which you want to add a comment.
`http POST http://djangomovies.brak.me/comments/ movie=[your_movie_id] comment_text=[your_comment_text]`
