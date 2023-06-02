from pydantic import BaseSettings, HttpUrl, validator


class Settings(BaseSettings):

    internal_token_url: str | None = None
    redirect_uri: str | None = None

    google_client_id: str | None = None
    google_authorize_url: str | None = None
    google_scope: str = 'openid email'

    github_client_id: str | None = None
    github_authorize_url: str | None = None
    github_scope: str = 'openid email'

    # will be true if both `internal_token_url` and `redirect_uri`
    # are non-empty
    oauth2: bool = False

    @validator("oauth2", always=True)
    def validator_oauth2(cls, value, values):
        """
        oauth2 field will be True if both internal_token_url
        and redirect_uri are non-empty
        """
        if values["internal_token_url"] and values["redirect_uri"]:
            return True

        return False

    class Config:
        env_prefix = 'PAPERMERGE__AUTH__'


def get_settings():
    return Settings()
