import pytest
import os

from pydantic.error_wrappers import ValidationError
from roco.main import generate_runtime_config


def test_only_google_client_id_provided():
    """
    Either none or both `google_client_id` and `google_authorize_url`
    should be supplied.
    In this scenario only `google_client_id` is provided -> validation
    error is expected
    """
    os.environ["PAPERMERGE__AUTH__REDIRECT_URI"] = "abc/callback"
    os.environ["PAPERMERGE__AUTH__INTERNAL_TOKEN_URL"] = "abc/api/token"
    os.environ["PAPERMERGE__AUTH__GOOGLE_CLIENT_ID"] = "google123"
    os.environ["PAPERMERGE__AUTH__GOOGLE_AUTHORIZE_URL"] = ''

    with pytest.raises(ValidationError):
        generate_runtime_config()


def test_only_google_authorize_url_provided():
    """
    Either none or both `google_client_id` and `google_authorize_url`
    should be supplied.
    In this scenario only `authorize_url` is provided -> validation
    error is expected
    """
    os.environ["PAPERMERGE__AUTH__REDIRECT_URI"] = "abc/callback"
    os.environ["PAPERMERGE__AUTH__INTERNAL_TOKEN_URL"] = "abc/api/token"
    os.environ["PAPERMERGE__AUTH__GOOGLE_AUTHORIZE_URL"] = "some-google-url"
    os.environ["PAPERMERGE__AUTH__GOOGLE_CLIENT_ID"] = ''

    with pytest.raises(ValidationError):
        generate_runtime_config()


def test_none_of_the_google_oauth2_fields_is_present():
    """
    In scenario no google oauth2 fields are present. Such scenario
    is valid.
    """
    os.environ["PAPERMERGE__AUTH__REDIRECT_URI"] = "abc/callback"
    os.environ["PAPERMERGE__AUTH__INTERNAL_TOKEN_URL"] = "abc/api/token"
    os.environ["PAPERMERGE__AUTH__GOOGLE_AUTHORIZE_URL"] = ''
    os.environ["PAPERMERGE__AUTH__GOOGLE_CLIENT_ID"] = ''

    result = generate_runtime_config()
    assert "redirect_uri" in result


def test_both_of_the_google_oauth2_fields_is_present():
    """
    In this scenario both google oauth2 fields i.e.
    `google_authorize_url` and `google_client_id` are present.
    Such scenario is obviously valid.
    """
    os.environ["PAPERMERGE__AUTH__REDIRECT_URI"] = "abc/callback"
    os.environ["PAPERMERGE__AUTH__INTERNAL_TOKEN_URL"] = "abc/api/token"
    os.environ["PAPERMERGE__AUTH__GOOGLE_AUTHORIZE_URL"] = 'some-google-url'
    os.environ["PAPERMERGE__AUTH__GOOGLE_CLIENT_ID"] = 'some-google-client-id'

    result = generate_runtime_config()

    assert "some-google-url" in result
    assert "some-google-client-id" in result





