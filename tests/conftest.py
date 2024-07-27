import pytest

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import myapp


@pytest.fixture()
def flask_app():
    return myapp.app


@pytest.fixture()
def client(flask_app):
    return flask_app.test_client()
