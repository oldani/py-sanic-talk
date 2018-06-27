from sanic import Sanic
from sanic import response

app = Sanic(__name__)


@app.route('/async')
async def index(request):
    # return response.text('hi')
    return response.json({
        'hello': 'PyDO'
    })


@app.route('/noasync')
def noasync(request):
    # return response.text('No Async')
    return response.json({
        'hello': 'PyDO2'
    })


if __name__ == '__main__':
    app.run(port=5000)
