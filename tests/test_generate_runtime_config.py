import pytest
import os

from pydantic.error_wrappers import ValidationError
from roco.main import generate_runtime_config


def test_only_google_client_id_provided():
    """
    Either none or all `google_client_id`, `google_authorize_url`,
    `google_redirect_uri` should be supplied.
    In this scenario only `google_client_id` is provided -> validation
    error is expected
    """
    os.environ["PAPERMERGE__AUTH__GOOGLE_CLIENT_ID"] = "google123"
    os.environ["PAPERMERGE__AUTH__GOOGLE_AUTHORIZE_URL"] = ''
    os.environ["PAPERMERGE__AUTH__GOOGLE_REDIRECT_URI"] = ''

    with pytest.raises(ValidationError):
        generate_runtime_config()


def test_only_google_authorize_url_provided():
    """
    Either none or all `google_client_id`, `google_authorize_url`,
    'google_redirect_uri' should be supplied.
    In this scenario only `authorize_url` is provided -> validation
    error is expected
    """
    os.environ["PAPERMERGE__AUTH__GOOGLE_AUTHORIZE_URL"] = "some-google-url"
    os.environ["PAPERMERGE__AUTH__GOOGLE_CLIENT_ID"] = ''
    os.environ["PAPERMERGE__AUTH__GOOGLE_REDIRECT_URI"] = ''

    with pytest.raises(ValidationError):
        generate_runtime_config()


def test_none_of_the_google_oauth2_fields_is_present():
    """
    In scenario no google oauth2 fields are present. Such scenario
    is valid.
    """
    os.environ["PAPERMERGE__AUTH__GOOGLE_AUTHORIZE_URL"] = ''
    os.environ["PAPERMERGE__AUTH__GOOGLE_CLIENT_ID"] = ''
    os.environ["PAPERMERGE__AUTH__GOOGLE_REDIRECT_URI"] = ''

    result = generate_runtime_config()
    assert "window" in result


def test_both_of_the_google_oauth2_fields_is_present():
    """
    In this scenario all google oauth2 fields i.e.
    `google_authorize_url`, `google_client_id`, ``google_redirect_uri`
    are present. Such scenario is obviously valid.
    """

    os.environ["PAPERMERGE__AUTH__GOOGLE_AUTHORIZE_URL"] = 'some-google-url'
    os.environ["PAPERMERGE__AUTH__GOOGLE_CLIENT_ID"] = 'some-google-client-id'
    os.environ["PAPERMERGE__AUTH__GOOGLE_REDIRECT_URI"] = "abc/callback"

    result = generate_runtime_config()

    assert "some-google-url" in result
    assert "some-google-client-id" in result
    assert "abc/callback" in result

