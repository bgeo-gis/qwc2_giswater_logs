import os

from plugins.giswater_logs.controllers import GwLogController


name = "Giswater Logs"


def load_plugin(app, handler):
    # check required config
    config = handler().config()
    gw_log_path = config.get('gw_log_path')
    if gw_log_path is None or not os.path.isdir(gw_log_path):
        app.logger.error(
            "Giswater Log plugin: "
            "Required config option 'gw_log_path' is not set or invalid"
        )
    gw_log_file_prefix = config.get('gw_log_file_prefix')
    if gw_log_file_prefix is None:
        app.logger.error(
            "Giswater Log plugin: "
            "Required config option 'gw_log_file_prefix' is not set"
        )

    # create controller (including routes)
    GwLogController(app, handler)
