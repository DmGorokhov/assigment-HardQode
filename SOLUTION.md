
### Solution:
Develop 3 api endpoints:
* /api/v1/products/
* /api/v1/products/lessons/{user_id}
* /api/v1/products/product/{user_id}


### Source code is available on GitHub:

```shell
$ git clone git@github.com:DmGorokhov/assigment-HardQode.git
```

You can run the application using both Poetry and Docker.

**Poetry** is setup by the commands:

**Linux, macOS, Windows (WSL):**

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Details on installing and using the **Poetry** package are available in [official documentation](https://python-poetry.org/docs/).

To install **Poetry** you need **Python 3.7+** use the information from the official website [python.org](https://www.python.org/downloads/)

To install **Docker**, use the information from the official website [docs.docker.com](https://docs.docker.com/engine/install/)
### Basic shortcut commands:
When cloning app repository, you may need to install Make for run short console-commands described below.

#### *Docker*


```bash
make docker-build # build app-image
```

```bash
make docker-start # start container
```
#### *Poetry*

```
make install   # install poetry for dependency management
```
Set environment variables using file .env.example as example.
For development DEBUG variable must be set as True

```
make build   # run migrations
```

```
make start-dev   # starts the app on the local server in the development environment
```

Try get api endpoints:
* localhost:8000/api/v1/products/
* localhost:8000/api/v1/products/lessons/{user_id}
* localhost:8000/api/v1/products/{product_title}/{user_id}

Check SQL queries in django-debug sidebar