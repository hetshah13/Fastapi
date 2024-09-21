""" 
we have create virtual environment: myenv
1. python -m venv myenv
2. myenv\Scripts\activate
3. then install libraries and dependances
4. deactivate (to deactivate virtual environment)
"""

# Libraries
import uvicorn # for ASGI
from fastapi import FastAPI

# Creating Object
app = FastAPI()

# Index route, opens automatically on http://127.0.0.1:8000/
@app.get('/')
def index():
    return{'Message':'Hello Het'}

@app.get('/welcome')
def get_name(name: str, degree: str):
    return {'Welcome To This Repo ' f'{name}'
            ' Your Highest Qualification ' f'{degree}'}


# Run the API with uvicorn
# It will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8000)

#uvicorn main:app --reload