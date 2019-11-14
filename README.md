# SLaT
**S**imple **La**mbda **T**oolkit

[![CircleCI](https://circleci.com/gh/samkeen/SLaT.svg?style=svg)](https://circleci.com/gh/samkeen/SLaT)
[![Coverage Status](https://coveralls.io/repos/github/samkeen/SLaT/badge.svg?branch=master)](https://coveralls.io/github/samkeen/SLaT?branch=master)

Collection of reusable Python tools for lambda development.

This project is meant to :meat_on_bone: (or :corn:) these requirements
- As a lambda developer I want to write as little boilerplate as possible
- As a lambda developer I want to ensure I produce high value, discoverable logs
- As a lambda developer I want to ensure I sends proper, consistent, well formed responses
- *As a lambda developer I want ToBeDetermined*

Example hello world Lambda
```python
from slat.log_util import LogUtil
from slat.response import LambdaProxyResponse
from slat.types import JsonapiBody

# initiate you logger outside the handler
log = LogUtil.init_logger(env_var_name='LOG_LEVEL', default_level='INFO')

def lambda_handler(event, context):
    # bind the request id to the logger
    LogUtil.init_request({'request_id': context.aws_request_id})
    # make log statements as normal
    log.debug('Lambda Handler Event', lambda_handler_event=event)
    # prepare a Jsonapi payload (https://jsonapi.org/)
    response_body = JsonapiBody(data={'hello': 'world!'}, errors=[], meta={})
    # respond in the expected APIGateway lambda proxy format (https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-output-format)
    return LambdaProxyResponse.respond(200, response_body, context)
```

# Slat Tools

## Responses
TBDocumented

## Logging
 [Structlog](http://www.structlog.org/en/stable/index.html) is used for structured JSON logging
 
**Example Usage**
```python
import logging
from slat.log_util import LogUtil

log = LogUtil.init_logger(default_level='INFO',  correlation_id_key_val={'request_id': '999'})
log.info('is this JSON: {"answer": 42}')
log.error("the log message", some="value", extra_data=[1, 2, 3, "4"])
# only OUR logger will render as JSON
logging.getLogger("test").warning("hello")
```
output:
```
{"event": "is this JSON: {\"answer\": 42}", "level": "info", "logger": "slat.log_util", "request_id": "999", "timestamp": "2019-11-06T21:04:33.517295Z"}
{"event": "the log message", "extra_data": [1, 2, 3, "4"], "level": "error", "logger": "slat.log_util", "request_id": "999", "some": "value", "timestamp": "2019-11-06T21:04:33.517652Z"}
hello
```

For test runs you can add an ENV flag `TESTING_RUN=true` and log statements will be written to `./testing.log`
```
TESTING_RUN=true pytest
```

# Running tests
```
pytest

# with coverage 
pytest --cov=slat

# generage html report
coverage html
open ./htmlcov/index.html
```

# Developing

**create file ~/.pypirc**
```
[distutils]
index-servers =
  pypi
  pypitest

[pypi]
repository: https://upload.pypi.org/legacy/
username:
password:

[pypitest]
repository: https://test.pypi.org/legacy/
username:
password:
```

**build**
```
# tick to semver `version` in setup.py
rm -rf dist
python setup.py bdist_wheel --universal
```

**pypitest**
```
twine upload --repository pypitest dist/*
pip install slat --index-url https://test.pypi.org/simple/ --upgrade
```

**pypi**
```
twine upload --repository pypi dist/*
pip install slat --upgrade
```
