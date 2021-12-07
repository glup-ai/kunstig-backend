# Kunstig (API)
This Kunstig API produces beautiful images from Kunstig's trained models. 

This API is based on the repo [glup-ml-deployment-tutorial](https://github.com/glup-ai/glup-ml-deployment-tutorial/tree/master/Tutorial), and uses the deployment solution: Hosted app service using the Flask framework.

## Prerequisites
- Python v 3.8

## Setup
#### Create a new virtual environment
`$ python -m venv .venv`

#### Activate the environment
Windows <br/>
`$ .venv/Scripts/activate`

Mac / Linux <br/>
`$ source .venv/bin/activate`

#### Install requirements
`$ pip install -r requirements.txt`

<a name="run-app"></a>
#### Run app locally
`$ flask run`

#### Get images from Kunstig
Check out the beautiful art Kunstig produces by calling on of our GET methods you can find in [app.py](https://github.com/glup-ai/kunstig-backend/blob/master/app.py):
- `running-server/munch`
- `running-server/portrait`
_get the running server address from the previous step: [Run app locally](#run-app)_
