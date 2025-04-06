from pathlib import Path

from fastapi import FastAPI

from Optimize import optimize
from type import ApiInput, ApiOutput

app = FastAPI(debug=True)


@app.post("/auth")
def _auth(api_input: ApiInput) -> bool:
    """
    dummy function
    """
    return api_input.id == "kamonohasi"


@app.post("/optimize")
def _optimize(api_input: ApiInput) -> ApiOutput:
    """
    dummy function
    """
    return optimize(api_input)


def generate(swagger_path: Path) -> None:
    with open(swagger_path, "w") as f:
        json.dump(app.openapi(), f, indent=4)


if __name__ == "__main__":
    import argparse
    import filecmp
    import json

    from const import ROOT_DIR

    parser = argparse.ArgumentParser(description="openapi")
    parser.add_argument("mode", choices=["gen", "check"], help="mode")
    args = parser.parse_args()

    local_swagger_path = ROOT_DIR.joinpath("swagger.json")
    tmp_swagger_path = Path("/tmp/swagger.json")
    if args.mode == "gen":
        generate(local_swagger_path)
    elif args.mode == "check":
        generate(tmp_swagger_path)
        result = filecmp.cmp(local_swagger_path, tmp_swagger_path, shallow=False)
        assert result is True
    else:
        raise AssertionError
