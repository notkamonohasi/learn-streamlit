from main import main
from type import ApiInput, ApiOutput


def lambda_handler(body: dict) -> ApiOutput:
    api_input = ApiInput(**body)
    return main(api_input)
