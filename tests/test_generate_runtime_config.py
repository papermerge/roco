import pytest
import os

from pydantic.error_wrappers import ValidationError
from roco.main import generate_runtime_config

from .utils import reset_env


@pytest.mark.parametrize("provider", ["google", "github"])
def test_only_google_client_id_provided(provider):
    """
    Either none or all `<provider>_client_id`, `<provider>_authorize_url`,
    `<provider>_redirect_uri` should be supplied.
    In this scenario only `<provider>_client_id` is provided -> validation
    error is expected
    """
    reset_env()

    os.environ[f"PAPERMERGE__AUTH__{provider.upper()}_CLIENT_ID"] = "google123"
    os.environ[f"PAPERMERGE__AUTH__{provider.upper()}_AUTHORIZE_URL"] = ''
    os.environ[f"PAPERMERGE__AUTH__{provider.upper()}_REDIRECT_URI"] = ''

    with pytest.raises(ValidationError):
        generate_runtime_config()


@pytest.mark.parametrize("provider", ["google", "github"])
def test_only_google_authorize_url_provided(provider):
    """
    Either none or all `<provider>_client_id`, `<provider>_authorize_url`,
    '<provider>_redirect_uri' should be supplied.
    In this scenario only `authorize_url` is provided -> validation
    error is expected
    """
    reset_env()

    os.environ[
        f"PAPERMERGE__AUTH__{provider.upper()}_AUTHORIZE_URL"
    ] = "some-google-url"
    os.environ[f"PAPERMERGE__AUTH__{provider.upper()}_CLIENT_ID"] = ''
    os.environ[f"PAPERMERGE__AUTH__{provider.upper()}_REDIRECT_URI"] = ''

    with pytest.raises(ValidationError):
        generate_runtime_config()


def test_none_of_the_google_oauth2_fields_is_present():
    """
    In scenario no <provider> oauth2 fields are present. Such scenario
    is valid.
    """
    reset_env()

    result = generate_runtime_config()
    assert "window" in result


@pytest.mark.parametrize("provider", ["google", "github"])
def test_both_of_the_google_oauth2_fields_is_present(provider):
    """
    In this scenario all google oauth2 fields i.e.
    `google_authorize_url`, `google_client_id`, ``google_redirect_uri`
    are present. Such scenario is obviously valid.
    """
    reset_env()

    os.environ[
        f"PAPERMERGE__AUTH__{provider.upper()}_AUTHORIZE_URL"
    ] = 'some-google-url'
    os.environ[
        f"PAPERMERGE__AUTH__{provider.upper()}_CLIENT_ID"
    ] = 'some-google-client-id'
    os.environ[
        f"PAPERMERGE__AUTH__{provider.upper()}_REDIRECT_URI"
    ] = "abc/callback"

    result = generate_runtime_config()

    assert "some-google-url" in result
    assert "some-google-client-id" in result
    assert "abc/callback" in result
