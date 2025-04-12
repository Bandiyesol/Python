from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def printHello():
	return "Hello World"

@app.get("/json")
def printJson():
	return {
	"Number" : 12345
}