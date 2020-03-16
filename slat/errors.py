"""
Exception to through that ensures all needed information is gathered in order to return
a well formed lambda response
"""
import json


class ErrorResponse(Exception):
    """
    Build a custom Exception to ensure we get predictable responses back to APIG
    see: https://aws.amazon.com/blogs/compute/error-handling-patterns-in-amazon-api-gateway-and-aws-lambda/
    """

    def __init__(self, message: str, status_code: int, error_code: str = ''):
        # Call the base class constructor with the parameters it needs
        super(ErrorResponse, self).__init__(message)
        self.message = message
        self.error_code = error_code
        self.status_code = status_code

    def __str__(self):
        my_error_obj = {
            'httpStatus': self.status_code,
            'message': self.message
        }
        return json.dumps(my_error_obj)
