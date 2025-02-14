from flask import Flask, request, jsonify
from flask_cors import CORS
from number_classifier import classify_number
import requests
from http import HTTPStatus
import logging
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
CORS(app)
logging.basicConfig(level=logging.INFO)

def get_fun_fact(number: int) -> str:
    try:
        if classify_number(number)['properties'] == ["armstrong", "odd"] or classify_number(number)['properties'] == ["armstrong", "even"]:
            armstrong_eq = " + ".join([f"{digit}^{len(str(number))}" for digit in str(number)])
            return f"{number} is an Armstrong number because {armstrong_eq} = {number}"
        else:
            url = f"http://numbersapi.com/{number}/math?json=true"
            response = requests.get(url)
            return response.text if response.status_code == 200 else "No fun fact available."
    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")
        return f"An error occurred: {str(e)}"
@app.route('/api/classify-number/', methods=['GET'])
def api_classify_number():
    try:
        number = request.args.get('number')
        if number is None:
            return jsonify({"number": "alphabet", "error": True}), 404
        number = int(number)
        result = classify_number(number)
        result['fun_fact'] = get_fun_fact(number)
        return jsonify(dict(
            number=result['number'],
            is_prime=result['is_prime'],
            is_perfect=result['is_perfect'],
            properties=result['properties'],
            digit_sum=result['digit_sum'],
            fun_fact=result['fun_fact']
        )), HTTPStatus.OK
    except ValueError:
        return jsonify({"number": "alphabet", "error": True}), 404

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)