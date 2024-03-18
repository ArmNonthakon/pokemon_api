from fastapi import FastAPI
import requests
import json

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
@app.post("/pokemon")
async def sentPokemonFId(id):
    result = {}
    url = 'https://pokeapi.co/api/v2/pokemon-form/{}/'.format(id)

    #fetch name, sprites 
    response = requests.get(url)
    data = response.json()
    result['pokemon'] = data['pokemon']
    result['sprites'] = data['sprites']

    #fetch url and use it to continue fetch stats
    url = data['pokemon']['url']
    response = requests.get(url)
    data = response.json()
    result['stats'] = data['stats']

    return result
    