from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Function to generate numbers in the specific triangle pattern
def generate_triangle(num):
    num_str = str(num)
    triangle = ['10']  # Start with '10' as the first line
    for i in range(1, len(num_str)):
        # Create subsequent lines with increasing trailing zeros
        triangle.append(num_str[i] + '0' * i)
    return triangle

# Function to generate odd numbers up to the input number
def generate_odd_numbers(num):
    return [i for i in range(1, num + 1) if i % 2 != 0]

# Function to generate prime numbers up to the input number
def generate_prime_numbers(num):
    primes = []
    for possiblePrime in range(2, num + 1):
        isPrime = True
        for n in range(2, int(possiblePrime ** 0.5) + 1):
            if possiblePrime % n == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(possiblePrime)
    return primes

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    num = data.get('number')

    # Validate the input as a positive integer
    if not isinstance(num, int) or num < 0:
        return jsonify({'error': 'Invalid input. Please enter a positive integer.'}), 400

    operation = data.get('operation')
    if operation == 'triangle':
        result = generate_triangle(num)
    elif operation == 'odd':
        result = generate_odd_numbers(num)
    elif operation == 'prime':
        result = generate_prime_numbers(num)
    else:
        return jsonify({'error': 'Invalid operation.'}), 400

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
