# Bank Note Authentication Using FastAPI

This project Bank Note Authentication system using FastAPI and a machine learning model to classify banknotes as genuine or counterfeit based on their characteristics.

### Dataset
The dataset used for training the machine learning model consists of various characteristics of banknotes such as:

1. Variance of the wavelet-transformed image.
2. Skewness of the wavelet-transformed image.
3. Curtosis of the wavelet-transformed image.
4. Entropy of the image.

These features are fed into a classification model to predict whether the banknote is real or fake.

## API Endpoints
### 1. /predict
**Method: POST**
  This endpoint accepts banknote features and returns whether the banknote is genuine or counterfeit.

### 2. /
**Method: GET**
  A simple root endpoint that returns a welcome message.

## Getting Started
**1. Clone the repository**
 ```
 git clone https://github.com/hetshah13/Fastapi.git
 cd Fastapi
```
 
**2. Install dependencies**
  ```
  pip install -r requirements.txt
```
  


[Checkout Website](https://fastapi-niedaqrjy-het-shahs-projects-42ee3146.vercel.app)
