# Changelog

## 0.4.3 - 2024-05-02

- Add OIDC's `oidc_post_logout_redirect_url` parameter
- Relax validation of oidc params

## 0.4.2 - 2024-03-26

- Add OIDC's `logout_url`

## 0.4.1 - 2024-03-02

- Rename `redirect_uri` to `redirect_url`

## 0.4.0 - 2024-03-01

- Add support for OIDC

## 0.3.0 - 2024-02-28
- Add support for "remote_user: { logout_endpoint: ... }"

## 0.2.0 - 2024-02-17

- Add support for "login_provider = db | ldap"
- Upgrade pydantic from 1.x -> 2.x
- Use typer instead of click
