import os

from roco.main import generate_runtime_config

from .utils import reset_env


def test_none_of_the_oidc_fields_is_present():
    """
    In scenario no oidc fields are present. Such scenario
    is valid.
    """
    reset_env()

    result = generate_runtime_config()
    assert "window" in result


def test_all_of_the_oidc_fields_is_present():
    """
    In this scenario all oidc fields i.e.
    `oidc_authorize_url`, `oidc_client_id`, ``oidc_redirect_url`
    are present. Such scenario is obviously valid.
    """
    reset_env()

    os.environ[
        f"PAPERMERGE__AUTH__OIDC_AUTHORIZE_URL"
    ] = 'some-google-url'
    os.environ[
        f"PAPERMERGE__AUTH__OIDC_CLIENT_ID"
    ] = 'some-google-client-id'
    os.environ[
        f"PAPERMERGE__AUTH__OIDC_REDIRECT_URL"
    ] = "abc/callback"
    os.environ[
        f"PAPERMERGE__AUTH__OIDC_LOGOUT_URL"
    ] = "abc/logout-url"

    result = generate_runtime_config()

    assert "some-google-url" in result
    assert "some-google-client-id" in result
    assert "abc/callback" in result


def test_login_provider_is_ldap():
    """
    In this scenario env variable PAPERMERGE__AUTH__LDAP_URL is defined and
    has a non empty value. It is expected that generated template will
    contain "login_provider: 'ldap'"
    """
    reset_env()

    os.environ[
        f"PAPERMERGE__AUTH__LDAP_URL"
    ] = 'ldap.trusel.net'

    result = generate_runtime_config()

    assert "login_provider: 'ldap'" in result
