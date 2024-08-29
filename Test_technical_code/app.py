from flask import Flask, request, jsonify, render_template
app = Flask(__name__)

def  validate_number(input_str):
    try:
        num= int(input_str)
        return num if num>- 0 else None
    except ValueError:
        return None

# Function to regenerate Number
def generate_triangle(number):
    num_str= str(number)
    triangle= [num_str[:i] + '0' *(len(num_str)-i) for i in range(1, len(num_str) +1)] 
    return triangle

#Function genereae odd numbers
def generate_odd_numbers(max_number):
    return [i for i in range (1, max_number +1) if i % 2 != 0]

# Function generate prime number
def generate_prime_numbers(max_number):
    primes = []
    for num in range (2, max_number + 1):
        if all(num% i != 0 for i in range (2, int(num **0.5)+1 )):
            primes.append(num)
            return primes

#Route To render template
@app.route('/')
def inex():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    input_number = request.form.get('numbber')
    action = request.form.get('action')

    number= validate_number(input_number)
    if number is None:
        return jsonify({'error': 'input harus tanpa angka positif.'})
    if action=='generate_triangle':
        result= generate_triangle(number)
    
    elif action== 'generate_odd':
        result = generate_odd_numbers(number)

    elif action== 'generate_prime':
        result = generate_prime_numbers(number)
    else:
        result ='Aksi tidak Valid.'

    return jsonify({'result':result})

if __name__=='__main__':
    app.run(debug=True)
    