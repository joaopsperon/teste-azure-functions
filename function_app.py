import azure.functions as func
import logging

from scripts import test_script

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)


@app.route(route="teste_http_trigger")
def teste_http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")

    name = req.params.get("name")
    test_script.main()
    return func.HttpResponse(
        "This HTTP triggered function executed successfully.",
        status_code=200,
    )
