from type import ApiInput, ApiOutput, Status


def optimize(api_input: ApiInput) -> ApiOutput:
    """
    optimize

    Args:
        api_input (ApiInput): _description_

    Returns:
        ApiOutput: _description_
    """
    print(f"{api_input=}")
    return ApiOutput(status=Status.BLUE)
