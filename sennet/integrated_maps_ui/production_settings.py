from pathlib import Path

print("Loading production settings")

DEBUG = True

SECRET_PATH = Path("/opt/integrated-maps-ui/secret")
# Static secret key is required
with open(SECRET_PATH / "django_secret_key.txt") as f:
    SECRET_KEY = f.read().strip()

ALLOWED_HOSTS = [
    "sn-integrated-mapping.sennetconsortium.org",
    "https://sn-integrated-mapping.sennetconsortium.org/",
    "sn-integrated-mapping.sennetconsortium.org/"
]