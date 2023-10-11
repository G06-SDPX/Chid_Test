from flask import Flask

app = Flask(__name__)


@app.route('/')
def helloworld():
    return 'Hello World'


@app.route('/is_prime/<int:x>')
def is_prime(x):
    if x <= 1:
        return 'False'
    for i in range(2, int(x**(1/2)+1)):
        if (x % 2 == 0):
            return 'False'
    return 'True'


if __name__ == ('__main__'):
    app.run(debug=True)
