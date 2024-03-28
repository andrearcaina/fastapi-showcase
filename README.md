# FastAPI Tutorial

FastAPI Tutorial for PACSxMOSS API Dev Workshop

# Steps

These are the following steps to create an API.

1. Create a virtual environment (if you want)

```bash
> py -m venv .venv # for windows
$ python -m venv .venv # for linux
```

2. Activate the virtual environment (if you did step 1)

```bash
> .venv\Scripts\activate # for windows
$ source .venv/bin/activate # for linux
```

3. Install FastAPI and Uvicorn

```bash
> pip install fastapi uvicorn
```

4. Create `main.py` just like in the repository, and run `uvicorn main:app --reload` in root directory.
For an in-depth understanding of an API, take a look at the slides [here](https://docs.google.com/presentation/d/1My6xQ1N1SMr7_Jarb1AqsfqdDeZAGn6ZJDVrmIj_urU/edit?usp=sharing)

# Shortcut
If you want to shortcut everything, clone this repository (assuming you have [git](https://git-scm.com/) installed).
1. Clone command -> `git clone https://github.com/andrearcaina/fastapi-tutorial.git`
   - run `pip install -r requirements.txt` to install all dependencies required for this tutorial!
3. Then, run `uvicorn main:app --reload` to run the API.

You're good to go!

# Swagger UI
Swagger UI: allows ease of access to testing API endpoints

Swagger UI allows anyone — be it your development team or your end consumers — to visualize and interact with the API's resources without having any of the implementation logic in place.

go to `localhost:8000/docs` or `127:0.0.1:8000/docs` to check out Swagger UI.
