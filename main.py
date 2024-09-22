""" 
we have create virtual environment: myenv
1. python -m venv myenv
2. myenv\Scripts\activate
3. then install libraries and dependances
# pip install uvicorn, fastapi, uvloop
4. deactivate (to deactivate virtual environment)
"""

# Libraries
import uvicorn # for ASGI
from fastapi import FastAPI
import pickle
import pandas as pd

# Creating Object
app = FastAPI()
pickle_open = open("classifier.pkl","rb")
classifier = pickle.load(pickle_open)

# Index route, opens automatically on http://127.0.0.1:8000/
@app.get('/')
def index():
    return{'Message':'Hello Het'}

@app.get('/welcome')
def get_name(name: str):
    return {'Welcome To This Web Page ' f'{name}'}

@app.post('/predict')
def predict_note(data:Banknote):
    data = data.dict()

# Run the API with uvicorn
# It will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8000)

#uvicorn main:app --reload