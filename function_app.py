import azure.functions as func
import logging
from os import getenv
from scripts import script_1

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)


@app.route(route="teste_http_trigger")
def teste_http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")
    script_1.main()
    return func.HttpResponse(
        "This HTTP triggered function executed successfully.",
        status_code=200,
    )
