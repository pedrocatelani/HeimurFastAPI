from fastapi import FastAPI, status
from fastapi.responses import JSONResponse

from game import Game
from game.types import *

app = FastAPI(title="Heimur Backend")
game = Game()


@app.post("/create-char")
def create_char(atr: Atributes, specs: CreateSpecs):
    validate = game.validate_creation(atr, specs)
    if validate:
        sheet = game.generate_char_sheet(atr, specs)
        return JSONResponse(sheet, status_code=status.HTTP_200_OK)
    else:
        return JSONResponse(
            {"Status": "Character Creation gone wrong!!!! Check your points sum."},
            status_code=status.HTTP_400_BAD_REQUEST,
        )
