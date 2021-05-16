# XMEME

 A Full Stack application for a Meme Stream Page where users can post memes by providing their name, a caption for the meme and the URL for the meme image as input

## **Technologies**

* Publicly Deployed on heroku: [Xmeme](https://xmeme1606.herokuapp.com/)
* [Django](https://www.djangoproject.com/): Django builds better web apps with less code
* [DRF](www.django-rest-framework.org/): A powerful and flexible toolkit for building Rest APIs with Django
* Database used: [SQLite](https://www.sqlite.org/index.html) (for local testing), [PostgreSQL](https://www.psycopg.org/) (for deployment)
* Architecture of the Full Stack application
![Drag Racing](https://drive.google.com/uc?export=view&id=1hgXmpF2QwAk6tfhDmjjSrK7AC2k7V57V)

## **API ENDpoints**

> ### To send a meme to the backend

* HTTP Method - **POST**

* Endpoint - **`/memes`**

* Json Body contains these inputs - name, url, caption

Example Request:

```js
curl --location --request POST 'http://localhost:8081/memes' \
--header 'Content-Type: application/json' \
--data-raw '{
"name": "xyz",
"url": "https://abc.com",
"caption": "This is a meme"
}'
```

Sample Response:

```json
{
    "id": 1
}
```

> ### To fetch the **latest 100 memes created** from the backend

* HTTP Method - **GET**

* Endpoint - **`/memes`**

* Json Body contains these inputs - name, url, caption

Example Request:

```js
curl --location --request GET 'http://<Server_URL>/memes'
```

Sample Response:

```json
 [
    {
        "id": "1",       
        "name": "MS Dhoni",
        "url": "https://images.pexels.com/photos/3573382/pexels-photo-3573382.jpeg","caption": "Meme for my place"
    },
    {
        "id": "2",
        "name": "Viral Kohli",
        "url": "https://images.pexels.com/photos/1078983/pexels-photo-1078983.jpeg",
        "caption": "Another home meme"
    }
 ]
```

> ### To specify a particular id (identifying the meme) to fetch a single Meme

* HTTP Method - **GET**

* Endpoint - **`/memes/<id>`**

* Error:  
  * If a meme with that Id doesn’t exist, a 404 HTTP response code would be returned.

Example Request:

```js
curl --location --request GET 'http://<Server_URL>/memes<id>'
```

Sample Response:

```json
    {
        "id": "1",       
        "name": "MS Dhoni",
        "url": "https://images.pexels.com/photos/3573382/pexels-photo-3573382.jpeg","caption": "Meme for my place"
    }
```

> ### To update the caption or url for an existing meme at the backend

* HTTP Method - **PATCH**

* Endpoint - **`/memes/<id>`**

* Json Body can contain these inputs - url, caption

* Error:  
  * If a meme with that Id doesn’t exist, a 404 HTTP response code would be returned.

Example Request:

```js
curl --location --request PATCH 'http://localhost:8081/memes<id>' \
--header 'Content-Type: application/json' \
--data-raw '{
"name": "xyz",
"url": "https://abc.com",
"caption": "This is a meme"
}'
```

> ### To get the documented existing APIs using Swagger

* HTTP Method - **GET**

* Endpoint - **`/swagger-ui/`**

## **Other API ENDpoints**

> ### For rendering the html page containing the 100 latest memes

* HTTP Method - **GET**

* Endpoint - **`/meme_list`**

> ### For getting a form for updating a meme with an existing id

* HTTP Method - **GET**

* Endpoint - **`/update_meme/<id>/`**

* Error:  
  * If a meme with that Id doesn’t exist, a 404 HTTP response code would be returned.

## **Local Setup**

* If you wish to run your own build, first ensure you have python3 globally installed in your computer. If not, you can get python [here](https://www.python.org/downloads/).

    First of all, clone the repository.

### For Windows

* Download [pip](https://pip.pypa.io/en/stable/installing/) and add it to the path
* Change your working directory to the the cloned folder

    ```bash
    cd path/to/xmeme
    ```

* Download all the dependencies

    ```bash
    pip3 install -r requirements.txt
    ```

* Migrate to the database

    ```bash
    python3 manage.py makemigrations
    python3 manage.py migrate
    ```

    After this, you would see a new file named *db.sqlite3* in your parent folder

* Run server

    ```bash
    python3 manage.py runserver
    ```

### For Linux

* Install all the dependencies

    ```bash
    $ chmod +x install.sh
    $ ./install.sh
    ```

* Run the server

    ```bash
    $ chmod +x server_run.sh
    $ ./server_run.sh &
    ```

### Some points to consider

* If the PORT has to be changed

    The app will run at port 8081 as default, if you want to change that to any other, change this section of the code in the `manage.py` file as:

    ```bash
    runserver.default_port = "8081"
    ```

* If a proper http404 html page has to be rendered for bad requests

    Change the *DEBUG* value to *False* and add the corresponding host, say localhost in `settings.py`:

    ```bash
    DEBUG = False
    ALLOWED_HOSTS = ['localhost', '127.0.0.1']
    ```
