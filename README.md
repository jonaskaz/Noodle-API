# Noodle-API
Cup Noodle Vending Machine Ordering Queue

## Install dependencies in virtual environment

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
## Running tests
```
pytest tests/
```
## Running the API
```
cd noodle
uvicorn main:app --reload
```
Navigate to http://127.0.0.1:8000/docs#/ to view routes