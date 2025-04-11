import sys
from hatchling.builders.hooks.plugin.interface import BuildHookInterface


class CustomHook(BuildHookInterface):
    def initialize(self, version, build_data):
        if build_data.get('pure_python') and not build_data.get('infer_tag'):
            build_data['tag'] = (
                f'py{sys.version_info.major}{sys.version_info.minor}-none-any'
            )
