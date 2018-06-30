from sanic import Sanic
from sanic.response import text, json, html

app = Sanic(__name__)


@app.route('/async')
async def index(request) -> json:
    return json({'hello': 'PyDO'})


@app.route('/noasync')
def noasync(request) -> text:
    return text('Hello PyDO')


@app.route('/hello/<name>')
async def hello(request, name: str) -> json:
    return json({'hello': name})


@app.route('/age/<age:int>')
async def age(request, age: int) -> json:
    return json({'hello': age})


async def phrase(request) -> html:
    json_body = request.json
    # query_strings = request.args
    # form = request.form
    return html(f'<p>Hey say something: <strong>{json_body.phrase}</strong></p>')


app.add_route(phrase, '/phrase', methods=['POST'])

if __name__ == '__main__':
    # app.run(port=5000)
    app.run(host='0.0.0.0', port=1337, workers=4)
