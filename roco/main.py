import pathlib
from jinja2 import Environment, PackageLoader, select_autoescape


env = Environment(
    loader=PackageLoader("roco"),
    autoescape=select_autoescape()
)


def get_template():
    cur_dir = pathlib.Path(__file__).parent.resolve()
    template_path = cur_dir / "templates"

    return env.get_template(
        name="runtime-config.js.jinja2",
        parent=str(template_path)
    )


def get_context():
    """Builds context dictionary from environment variables"""

    return dict(
        internal_token_url="one",
        redirect_uri="two",
        google_client_id="abc",
        google_authorize_url="123"
    )


def generate_runtime_config() -> str:
    template = get_template()
    context = get_context()

    return template.render(context)
