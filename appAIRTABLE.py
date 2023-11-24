from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

AIRTABLE_API_KEY = 'patPY4D2X9qxWTeRl'
AIRTABLE_BASE_ID = 'Calcuradora'
AIRTABLE_TABLE_NAME = 'CalcuradoraData'

AIRTABLE_ENDPOINT = f'https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{AIRTABLE_TABLE_NAME}'

@app.route('/')
def calculadora():
    operaciones = obtener_operaciones_airtable()
    return render_template('calcweb2.html', operaciones=operaciones)

@app.route('/realizar/<operacion>/', methods=['POST'])
def realizar_operacion(operacion):
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    resultado = realizar_calculo(operacion, num1, num2)

    guardar_operacion_airtable(operacion, resultado)

    return redirect(url_for('calculadora'))

def realizar_calculo(operacion, num1, num2):
    if operacion == 'suma':
        return num1 + num2
    elif operacion == 'resta':
        return num1 - num2
    elif operacion == 'multiplicacion':
        return num1 * num2
    elif operacion == 'division':
        if num2 != 0:
            return num1 / num2
        else:
            return "No se puede dividir entre cero."

def obtener_operaciones_airtable():
    headers = {
        'Authorization': f'Bearer {AIRTABLE_API_KEY}',
    }

    response = requests.get(AIRTABLE_ENDPOINT, headers=headers)
    data = response.json().get('records', [])

    operaciones = [{'operacion': record['fields']['Operacion'], 'resultado': record['fields']['Resultado']} for record in data]
    return operaciones

def guardar_operacion_airtable(operacion, resultado):
    headers = {
        'Authorization': f'Bearer {AIRTABLE_API_KEY}',
        'Content-Type': 'application/json',
    }

    data = {
        'fields': {
            'Operacion': operacion,
            'Resultado': resultado,
        }
    }

    response = requests.post(AIRTABLE_ENDPOINT, headers=headers, json=data)
    return response.json()

if __name__ == '__main__':
    app.run(debug=True)
