from sanic import Sanic, json, text

# from secrets import API_KEY

app = Sanic('Bambilici')


@app.get('/joaca')
async def play(request):
    # if not request.headers.get('API_KEY') == API_KEY:
    #     return json(status=403)
    try:
        return text(f'{int(request.args.get("numar")) + 1}. Te-am batut.')
    except Exception as e:
        return text(f'Fault tehnic. Am castigat. \n\nCum ai dat fault: {e}')


if __name__ == '__main__':
    app.run('0.0.0.0', 8000, debug=True, auto_reload=True, workers=4, access_log=True)