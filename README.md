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

#### GET: /images

Returns the complete list of images in random order.

_Response example_:

```
{
    "images": [
        "https://cdn.sanity.io/images/o9upvhes/production/395887b9ffe5328a4984d4d9cdd9825542bf04d6-1024x1024.png",
        "https://cdn.sanity.io/images/o9upvhes/production/5bdba26e9d0c7aa97b582d34400aa5979ade28a3-1024x1024.png",
        ...
    ]
}
```

---

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
