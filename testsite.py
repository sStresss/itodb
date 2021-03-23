from flask import Flask

app = Flask(__name__)
print('local server start!!!')
@app.route('/', methods=['GET', 'POST'])
def inboundsms():
    data = 'Hello!'

    return (data)


if __name__ == '__main__':
    app.run()