from sanic import Sanic
from sanic import response

app = Sanic(__name__)


@app.route('/')
async def index(request):
    return response.text('hola')


@app.route('/noasync')
def noasync(request):
    return response.text('No Async')


if __name__ == '__main__':
    app.run(port=5000)
