import azure.functions as func
import os
import logging

app = func.FunctionApp()

# Rota da função: /api/print_enviroment_variable
@app.route(route="print_enviroment_variable", auth_level=func.AuthLevel.FUNCTION)
def print_enviroment_variable(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # Ler variável de ambiente
    minha_variavel = os.getenv('ENVIROMENT_VARIABLE_1', 'Variável não definida')
    logging.info(f'O valor de MINHA_VARIAVEL é: {minha_variavel}')

    name = req.params.get('name')

    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(
            f"Hello, {name}. This HTTP triggered function executed successfully. "
            f"A variável MINHA_VARIAVEL é: {minha_variavel}"
        )
    else:
        return func.HttpResponse(
            f"This HTTP triggered function executed successfully. "
            f"A variável MINHA_VARIAVEL é: {minha_variavel}",
            status_code=200
        )
