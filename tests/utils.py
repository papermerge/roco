import os


def reset_env():
    for provider in ['google', 'github']:
        os.environ[f"PAPERMERGE__AUTH__{provider.upper()}_CLIENT_ID"] = ''
        os.environ[f"PAPERMERGE__AUTH__{provider.upper()}_AUTHORIZE_URL"] = ''
        os.environ[f"PAPERMERGE__AUTH__{provider.upper()}_REDIRECT_URI"] = ''
