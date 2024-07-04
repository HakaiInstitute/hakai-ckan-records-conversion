import click
import yaml
import json
from loguru import logger
from . import convention_cff, erddap
from .ckan import CKAN

standard_formats = {
    "json": lambda x: json.dumps(x, indent=2),
    "yaml": lambda x: yaml.dump(x, default_flow_style=False),
    "erddap": erddap.dataset_xml,
    "cff": convention_cff.convention_cff,
}




@click.command()
@click.option(
    "--ckan-server", required=True, help="URL of the CKAN server.", envvar="CKAN_SERVER"
)
@click.option(
    "--dataset-ids",
    required=True,
    help="IDs of the datasets to retrieve.",
    multiple=True,
    envvar="DATASET_IDS",
)
@click.option(
    "--output-format",
    required=True,
    help="Output format (json or yaml).",
    type=click.Choice(standard_formats.keys()),
)
@click.option("--output-file", required=True, help="Output file.")
def main(ckan_server, dataset_ids, output_format, output_file):
    ckan = CKAN(ckan_server)
    for dataset_id in dataset_ids:
        logger.debug(f"Retrieving dataset {dataset_id}")
        record = ckan.get_record(dataset_id)
        if not record:
            logger.error(f"Dataset {dataset_id} not found.")

        logger.debug(f"Converting dataset {dataset_id}")
        converter = standard_formats[output_format]
        converted = converter(record)

        if output_file:
            with open(output_file, "w") as f:
                f.write(converted)
        else:
            print(converted)
