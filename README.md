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

5. If you want to shortcut everything, make sure you have at least step 3 done, and then clone this repository (assuming you have [git](https://git-scm.com/) installed)
Then, run `uvicorn main:app --reload` to run the API.

You're good to go!
