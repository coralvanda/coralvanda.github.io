# Pokemon API README

An API using Flask and the OpenAPI specification

## How to run (using terminal/command line)
From the root directory of the project, create a Python virtual environment with:

`virtualenv venv -p python3`

Then activate it. On Windows, use:

`.venv/Scripts/activate`

Once active, install the requirements with:

`pip install -r requirements.txt`

Finally, run the application with:

`python -m flask --app app/run run`

## How to run tests (with terminal/command line)
From the root directory of the project, run:

```
python -m pytest .\tests\unit\
```

## Routes available:
- /pokemon - Lists all pokemon in the data set
- /pokemon/{id} - Shows info on a single pokemon using the pokedex index number