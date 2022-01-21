# Kunstig (API)

This repository holds Kunstig backend, a webapp that allows you to fetch images live from an AI model trained to create paintings in different art styles.

This API is based on the repo [glup-ml-deployment-tutorial](https://github.com/glup-ai/glup-ml-deployment-tutorial/tree/master/Tutorial).

## Prerequisites

- Python v 3.8

## Setup

#### Create a new virtual environment

```
python -m venv .venv
```

#### Activate the environment

Windows <br/>

```
.venv/Scripts/activate
```

Mac / Linux <br/>

```
source .venv/bin/activate
```

#### Install requirements

```
pip install -r requirements.txt
```

<a name="run-app"></a>

#### Run app locally

```
flask run
```

## Usage

#### GET: /models

Returns the complete list of models.

_Response example_:

```
{
    "models": [
        {
            "displayName": "Munch",
            "name": "munch"
        },
        {
            "displayName": "Portrait",
            "name": "portrait"
        }
    ]
}
```

---

#### POST: /model

Returns extended information about a model.

_Request body_:

```
{
    "model": string (required)
}
```

_Response example_:

```
{
    "displayName": "Munch",
    "images": [
        "test/test_image1.jpg",
        "test/test_image2.jpg"
    ]
}
```

---

#### POST: /generate

Returns a generated image. Use the optional parameter 'inputString' to seed the image generation.

_Request body_:

```
{
    "model": string (required),
    "inputString": string (optional)
}
```
