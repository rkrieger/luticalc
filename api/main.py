from typing import Union
from typing_extensions import Annotated
from fastapi import FastAPI, Path, Query
import luti
import math
import datetime as DT
import time

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "This is LUticalc"}


@app.get("/calc")
def calculate(
    function_id: Annotated[
        int, Query(title="The ID of the calculating function to use")
    ] = 0,
    epoch: Annotated[
        int, Query(title="Point-in-time to use (post-epoch seconds)")
    ] = None
):

    if epoch is None:
        epoch = int(time.time())    

    calc = {0: lambda t: math.log2(2 * t ^ 3), 1: lambda t: math.log10(2 * t ^ 3)}
    result = calc[function_id](epoch)
    return {
        "function": function_id,
        "time": DT.datetime.fromtimestamp(epoch, DT.timezone.utc),
        "moment": epoch,
        "result": result,
    }


@app.get("/functions/")
def read_functions():
    # TODO  Code the functions in LUti.py and list them
    functions = [
        {"id": 0, "description": "Default LUticalc"},
        {"id": 1, "description": "Habibiti"},
    ]
    return {"functions": [functions]}


@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}
