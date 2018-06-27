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


async def phrase(request, phrase: str) -> html:
    return html(f'<p>Hey say something: <strong>{phrase}</strong></p>')


app.add_route(phrase, '/phrase', methods=['POST'])

if __name__ == '__main__':
    app.run(port=5000)
