from flask import Flask, render_template, request

app = Flask(__name__)

# List of AQ-10 Autism assessment questions
questions = [
    "1. Do you often notice small sounds when others do not?",
    "2. Do you usually concentrate more on the whole picture, rather than the small details?",
    "3. In a social group, can you easily keep track of several different people’s conversations?",
    "4. Do you find it easy to go back and forth between different activities?",
    "5. Do you find it difficult to imagine what it would be like to be someone else?",
    "6. Do you find yourself drawn more strongly to things than to people?",
    "7. Do you find it easy to work out what someone is thinking or feeling just by looking at their face?",
    "8. Do you often become so strongly absorbed in one thing that you lose sight of other things?",
    "9. Do you find it easy to figure out people’s intentions?",
    "10. Do you find it hard to make small talk with others?"
]

@app.route('/')
def home():
    return render_template('index.html', questions=questions)

@app.route('/submit', methods=['POST'])
def submit():
    responses = [request.form.get(f'q{i+1}') for i in range(10)]
    # Convert Yes/No to binary (1/0)
    binary_responses = [1 if response == "Yes" else 0 for response in responses]
    # Example rule for classification (for demonstration, replace with your ML model logic)
    has_autism = sum(binary_responses) > 5  # Simple threshold-based rule
    result = "The responses suggest Autism." if has_autism else "The responses do not suggest Autism."
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)

