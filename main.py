import utils
from fastapi import FastAPI, Body

from starlette.responses import FileResponse

app = FastAPI()


@app.post("/")
def get_csv_impact(mock_for_test: list = Body(..., embed=True)):

    event_list = utils.refactor_input(mock_for_test)
    utils.div_by_10(event_list)
    csv_output = utils.csv_export(event_list)
    ret = utils.get_ids(mock_for_test)
    print(ret)
    return FileResponse(csv_output)
