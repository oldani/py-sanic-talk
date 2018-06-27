from sanic import Sanic


app = Sanic()


@app.websocket('/echo')
async def echo(request, ws):
    while True:
        data = await ws.recv()
        await ws.send(f'Data recieved: {data}')


if __name__ == '__main__':
    app.run(port=5005)
