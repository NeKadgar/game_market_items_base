from typing import Any
from flask import abort


class ArgumentsSchema:
    """Validator for get parameters"""

    def __init__(self):
        self._arguments = []

    def add_argument(self, name: str, arg_type: Any) -> None:
        """Add argument for future validation type of args

        :param name: name of argument
        :param arg_type: expected type
        :return:
        """
        self._arguments.append({
            "name": name,
            "type": arg_type,
        })

    def validate(self, request_args):
        for parse_arg in self._arguments:
            request_arg = request_args.get(parse_arg["name"], None)

            try:
                parse_arg["type"](request_arg)
            except ValueError:
                return abort(400, f"Wrong type for '{parse_arg['name']}', must be {parse_arg['type'].__name__}")
            except TypeError:
                return abort(400, f"Argument '{parse_arg['name']}' required")
