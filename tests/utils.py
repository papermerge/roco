import os


def reset_env():
    os.environ[f"PAPERMERGE__AUTH__OIDC_CLIENT_ID"] = ''
    os.environ[f"PAPERMERGE__AUTH__OIDC_AUTHORIZE_URL"] = ''
    os.environ[f"PAPERMERGE__AUTH__OIDC_REDIRECT_URL"] = ''
    os.environ[f"PAPERMERGE__AUTH__OIDC_LOGOUT_URL"] = ''
