import os

from django.apps import AppConfig


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class Settings:
    WEBPACK_LOADER = {
        "INTERACTWEL": {
            "BUNDLE_DIR_NAME": "interactwel/dashboard/dist/",  # must end with slash
            "STATS_FILE": os.path.join(
                BASE_DIR,
                "static",
                "interactwel",
                "dashboard",
                "dist",
                "webpack-stats.json",
            ),
        }
    }


class InteractwelAppConfig(AppConfig):
    name = "interactwel"
    label = name
    verbose_name = "InterACTWEL Dashboard"
    fa_icon_class = "fa-map"
    url_prefix = "interactwel"
    settings = Settings()
    nav = [
        {
            "label": "InterACTWEL Dashboard",
            "icon": "fa fa-map",
            "url": "interactwel:app",
            "active_prefixes": [""],
        }
    ]
