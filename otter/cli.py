from pathlib import Path
import os
from click import group, option, argument, Choice
from otter.models import Gradebook
from otter.services import GradebookFormatter


@group
@option('--llamacloud-api-key', default=None, envvar='LLAMA_CLOUD_API_KEY', help="API Key to access https://cloud.llamaindex.ai")
def cli(llamacloud_api_key: str):
    """
    DLI Gradebook management helpers
    """

    os.environ['LLAMA_CLOUD_API_KEY'] = llamacloud_api_key


@cli.group()
def gradebooks():
    """
    Commands for managing Gradebooks
    """
    pass


@gradebooks.command()
@option('--format', 'format_type', type=Choice(GradebookFormatter.FormatType._member_names_), help="The target format of the gradebook", default=GradebookFormatter.FormatType.json.value)
@argument('path', nargs=1, type=Path)
def convert(format_type: str, path: Path):
    """
    Convert a Gradebook from .xlsx format to other formats
    """

    format_type = GradebookFormatter.FormatType(format_type)
    gradebook = Gradebook(path=path)
    gradebook.parse()
    formatter = GradebookFormatter(gradebook=gradebook)

    if format_type == GradebookFormatter.FormatType.json:
        print(formatter.to_json())
    else:
        raise ValueError("Unsupported format:", format_type)
