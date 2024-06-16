# Urine Strip Analysis

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Setup](#setup)
3. [Running the Application](#running-the-application)
4. [API Documentation](#api-documentation)
5. [Visual Representation](#visual-representation)

## Prerequisites

- [Python 3.8+](https://www.python.org/downloads/)
- [OpenCV](https://pypi.org/project/opencv-python/)
- [Django](https://pypi.org/project/Django/)

## Setup

1. Clone the repository
2. Create and activate a virtual environment:
    - Windows: 
    ```bash
    python -m venv env
    source env/bin/activate
    ```
    - Linux and MacOS:
    ```
    source myenv/bin/activate
    ```
3. Install required packages using the `requirements.txt` file.
```
pip install -r requirements.txt
```

4. Run migrations: Run the below line inside the root directory of this repository
```
python manage.py migrate
```

5. Running the Application

```
python manage.py runserver --settings=mysite.settings
```

## API Documentation

### Upload Image
* URL: stripColors/processImage
* Method: POST
* Body: Ensure that you pass the body in `form-data` mode:

```json
{
  "image": 'filename.png',
  "id": '1' 
}
```

* Response:
  - Image4: 
    ```json
    {
      "URO": [183.0, 168.0, 149.0], 
      "BIL": [178.0, 165.0, 153.0], 
      "KET": [157.0, 142.0, 130.0],
      "BLD": [164.0, 138.0, 93.0],
      "PRO": [148.0, 150.0, 118.0],
      "NIT": [179.0, 160.0, 146.0], 
      "LEU": [172.0, 163.0, 151.0], 
      "GLU": [152.0, 159.0, 137.0],
      "SG": [166.0, 166.0, 141.0], 
      "PH": [172.0, 152.0, 122.0]
    }
    ```

## Visual Representation:

  * Image4
    
  ![image](https://github.com/subru-37/Django-Urin-Strip-test/assets/93091455/c255b34a-96c0-4756-88fd-7a43eb8b0481)

  * Image6

  ![image](https://github.com/subru-37/Django-Urin-Strip-test/assets/93091455/630f7282-816a-471b-aead-a8d0429d988b)

