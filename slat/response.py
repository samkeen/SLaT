from slat.types import JsonapiBody, JsonDict


class LambdaProxyResponse:

    @staticmethod
    def respond(status_code: int, resp_payload: JsonapiBody, context: object) -> JsonDict:
        """
        Returns the expected Proxy integration lambda response format
        structure mandated as per
        https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-output-format
        :param status_code:
        :type status_code: int
        :param resp_payload:
        :type resp_payload: JsonapiBody
        :param context:
        :type context: object
        :return:
        :rtype: JsonDict
        """
        if isinstance(resp_payload, JsonapiBody):
            resp_payload.meta['request_id'] = context.aws_request_id
        response = {
            'statusCode': status_code,
            'body': '' if not resp_payload or resp_payload == {} else str(resp_payload),
            'headers': {
                'Content-Type': 'application/json',
                'X-Hb-Request-Id': context.aws_request_id,
            },
            'multiValueHeaders': {},
            'isBase64Encoded': False
        }
        return response
