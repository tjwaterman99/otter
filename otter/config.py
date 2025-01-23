from pathlib import Path

config_path = Path(__file__)
otter_path = config_path.parent
templates_path = otter_path / 'templates'
static_files_directory = otter_path / 'static'