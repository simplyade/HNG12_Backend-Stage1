Number Classification API

A Flask API that classifies numbers and provides fun facts about them.

Table of Contents
- #installation
- #running-the-api-locally
- #api-endpoint
- #deployment-on-render

Installation
To install the API, follow these steps:

1. Clone the repository: git clone <repository_url>
2. Change into the repository directory: cd HNG12_BACKEND_STAGE1
3. Install dependencies: pip install -r requirements.txt

Running the API Locally
To run the API locally, you can use either the Flask development server or Gunicorn.

Using Flask Development Server
1. Run the command: flask run --host=0.0.0.0 --port=5000
2. Open a web browser and navigate to http://127.0.0.1:5000

Using Gunicorn (Recommended for Deployment)
1. Run the command: gunicorn -w 4 -b 127.0.0.1:5000 app:app
2. Open a web browser and navigate to http://127.0.0.1:5000

API Endpoint
Classify a Number
- URL: GET /api/classify-number
- Query Parameter: number=<integer>
- Example Request: curl "http://127.0.0.1:5000/api/classify-number?number=371"
- Response: JSON object containing the number's classification and fun fact

Example Response:

{
  "number": 371,
  "is_prime": false,
  "is_perfect": false,
  "properties": ["armstrong", "odd"],
  "digit_sum": 11,
  "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}


Deployment on Render
To deploy the API on Render, follow these steps:

1. Push your changes to GitHub.
2. Connect the repository to Render.
3. Create a render.yaml file with the following contents:

services:
  - type: web
    name: Number Classification API
    runtime:
      language: python
    plan: free
    autoDeploy: false
    buildCommand: "pip install -r requirements.txt"
    startCommand: "gunicorn -w 4 app:app"
    ports:
      - 5000

4. Add a Gunicorn Start Command in Render settings: gunicorn -w 4 -b 0.0.0.0:5000 app:app