from flask import Flask

app = Flask(__name__)


@app.route('/mul5/<number>', methods=['GET'])
def calc(number):
    return str(float(number)*5).replace(".0","")

if __name__ == '__main__':
    app.run(debug=True)