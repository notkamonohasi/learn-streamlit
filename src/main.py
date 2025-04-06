from Optimize import optimize
from type import ApiInput, ApiOutput


def main(api_input: ApiInput) -> ApiOutput:
    print(f"{api_input=}")
    return optimize(api_input)
