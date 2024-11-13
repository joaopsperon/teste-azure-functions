import azure.functions as func
import logging
from os import getenv

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)


@app.route(route="teste_http_trigger")
def teste_http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")

    name = req.params.get("name")
    ENVIROMENT_VARIABLE = getenv("ENVIROMENT_VARIABLE_1")
    logging.info(f"A variavel .env é: {ENVIROMENT_VARIABLE}")
    return func.HttpResponse(
        "This HTTP triggered function executed successfully.",
        status_code=200,
    )
