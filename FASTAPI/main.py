import uvicorn # server

if __name__=="__main__":
    uvicorn.run("app.app:app", host='0.0.0.0', port=8080, reload=True)
    # uvicorn.run("app.app:app", host='0.0.0.0', reload=True)