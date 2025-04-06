from app import lambda_handler
from Tests.settings import HANDLER_BODY


class TestApp:
    def test_app(self) -> None:
        lambda_handler(HANDLER_BODY)
