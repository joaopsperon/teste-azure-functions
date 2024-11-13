import os
import requests
import random
import logging
import azure.functions as func

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)


@app.route(route="http_trigger")
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Iniciando função teste HTTP Trigger: RunesCape Bestiary")

    API_URL = os.getenv("API_URL")
    beast_id = str(random.randint(1, 100))
    url = API_URL + beast_id

    response = requests.get(url)

    if response.status_code == 200:
        return func.HttpResponse(
            str(response.json()),
            status_code=200,
        )
    else:
        return func.HttpResponse(
            response.text,
            status_code=response.status_code,
        )
