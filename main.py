import os
from pathlib import Path

from cheroot.wsgi import Server
from wsgidav.wsgidav_app import WsgiDAVApp

# Wispbyte normally supplies an assigned application port. PORT is also
# supported for environments that use the conventional variable name.
HOST = "0.0.0.0"
PORT = int(os.environ.get("SERVER_PORT") or os.environ.get("PORT") or "8080")

USERNAME = os.environ.get("DAV_USER", "davuser")
PASSWORD = os.environ.get("DAV_PASSWORD")
STORAGE_DIR = Path(os.environ.get("DAV_ROOT", "storage")).resolve()

if not PASSWORD:
    raise RuntimeError(
        "Set DAV_PASSWORD in Wispbyte → Startup → Environment Variables."
    )

STORAGE_DIR.mkdir(parents=True, exist_ok=True)

config = {
    "provider_mapping": {
        "/": {
            "root": str(STORAGE_DIR),
            "readonly": False,
        }
    },
    "http_authenticator": {
        "domain_controller": None,
        "accept_basic": True,
        "accept_digest": True,
        "default_to_digest": True,
    },
    "simple_dc": {
        "user_mapping": {
            "*": {
                USERNAME: {
                    "password": PASSWORD,
                    "roles": ["admin"],
                }
            }
        }
    },
    "dir_browser": {
        "enable": True,
        "davmount": True,
        "ms_mount": True,
    },
    "verbose": 1,
}

app = WsgiDAVApp(config)

print(f"WsgiDAV listening on {HOST}:{PORT}")
print(f"Storage directory: {STORAGE_DIR}")

server = Server((HOST, PORT), app)
server.start()
