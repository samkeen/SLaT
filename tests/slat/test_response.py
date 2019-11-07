from dataclasses import dataclass

import pytest

from slat.response import LambdaProxyResponse
from slat.types import JsonapiBody


@dataclass(frozen=True)
class ContextObject:
    aws_request_id: str = 'deadbeef-b638-402f-8c17-8080deadbeef'


@pytest.fixture()
def context_object():
    return ContextObject()


def test_proxy_response(context_object):
    response_payload = JsonapiBody(
        data=[],
        errors=[],
        meta={}
    )
    expected = {
        'statusCode': 200,
        'body': '{"data": [], "errors": [], "meta": {"request_id": "' + context_object.aws_request_id + '"}}',
        'headers': {
            'Content-Type': 'application/json',
            'X-Hb-Request-Id': context_object.aws_request_id,
        },
        'multiValueHeaders': {},
        'isBase64Encoded': False
    }
    assert LambdaProxyResponse.respond(200, resp_payload=response_payload, context=context_object) == expected
