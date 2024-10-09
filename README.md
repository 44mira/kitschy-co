
# Kitschy Co.

Clone the repo.

```bash
git clone https://github.com/44mira/kitschy-co.git
cd kitschy-co
```

> NOTE: Remember to cd back into the root folder before making `git`-related actions.

```bash
cd frontend
# ...
cd ..

git add .
git commit -m "feat: example"
git push
```

## Frontend

The frontend is written in Sveltekit.

```bash
cd frontend

# load dependencies
npm install

# run the development server
npm run dev
```

## Backend

The backend is written in Django ReST Framework.

These instructions assume you have `pyenv` installed.

```bash
# set local version to python 3.11
pyenv install 3.11
pyenv local 3.11

# instantiate virtual environment
python -m venv .venv
# or
virtualenv -p python3 .venv     # requires virtualenv

# on unix
source .venv/bin/activate

# on windows
. .venv\Scripts\activate

# load dependencies
pip install -r requirements.txt
```
