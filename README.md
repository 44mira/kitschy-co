# Important Links
- [Gantt](https://docs.google.com/spreadsheets/d/1-lv8CXxgeZPNvAxTtf1nMcPT3pGazXfCGU_z7rlab0M/edit?usp=drive_link)
- [Initial Features](https://docs.google.com/document/d/109JQ6lliifx3QkWt0vYSABfwqRs8qPxSq9vJw79hja8/edit)
- [ERD/Control Flow/Feature Tree](https://app.eraser.io/workspace/m7WbFfCAi3rne9vxpSZm?origin=share)
- [Mockups](https://www.figma.com/design/80Lbq0UWnjqPiZ0veNTV3z/Kitschy?node-id=0-1&t=LDXGwHHHuA6ldEWf-1)
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
cd backend

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
