from typing import Literal
from typing_extensions import Self
from pydantic import model_validator, ConfigDict
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    model_config = ConfigDict(env_prefix='PAPERMERGE__AUTH__')

    google_client_id: str | None = None
    google_authorize_url: str | None = None
    google_redirect_uri: str | None = None
    google_scope: str = 'openid email'

    github_client_id: str | None = None
    github_authorize_url: str | None = None
    github_redirect_uri: str | None = None
    github_scope: str = 'openid email'

    login_provider: Literal['db', 'ldap'] = 'db'

    @model_validator(mode='after')
    def check_google_params(self):
        three_values = [
            self.google_client_id,
            self.google_authorize_url,
            self.google_redirect_uri
        ]
        count = len([v for v in three_values if v])

        if count not in (0, 3):
            raise ValueError(
                'google_client_id, google_authorize_url and google_redirect_uri'
                ' should be either all absent or all present'
            )

        return self

    @model_validator(mode='after')
    def check_github_params(self):
        three_values = [
            self.github_client_id,
            self.github_authorize_url,
            self.github_redirect_uri
        ]
        count = len([v for v in three_values if v])

        if count not in (0, 3):
            raise ValueError(
                'github_client_id, github_authorize_url and github_redirect_uri'
                ' should be either all absent or all present'
            )

        return self


def get_settings():
    return Settings()
