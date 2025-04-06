from type import ApiInput

API_INPUT = ApiInput(id="kamonohasi", name="notkamonohasi", age=5)

HANDLER_BODY: dict = API_INPUT.model_dump()
