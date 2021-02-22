from uvicorn import run
if __name__ == '__main__':
    run("khairo:app", debug=True, host="127.0.0.1",
        workers=4, port=8000, reload=True, log_level="info")
