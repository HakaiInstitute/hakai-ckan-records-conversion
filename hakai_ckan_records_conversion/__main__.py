import json

import click
import yaml
from loguru import logger

from hakai_ckan_records_conversion import citation_cff, erddap
from hakai_ckan_records_conversion.ckan import CKAN

standard_formats = {
    "json": lambda x: json.dumps(x, indent=2),
    "yaml": lambda x: yaml.dump(x, default_flow_style=False),
    "erddap": erddap.dataset_xml,
    "cff": citation_cff.convention_cff,
}


@click.command()
@click.option(
    "--ckan-server", required=True, help="URL of the CKAN server.", envvar="CKAN_SERVER"
)
@click.option(
    "--record-id",
    required=True,
    help="IDs of the datasets to retrieve.",
    envvar="RECORD_ID",
)
@click.option(
    "--output-format",
    required=True,
    help="Output format (json or yaml).",
    type=click.Choice(list(standard_formats.keys())),
)
@click.option("--output-file", required=True, help="Output file.")
@logger.catch(reraise=True)
def main(ckan_server, record_id, output_format, output_file):
    """Convert CKAN records to different metadata formats or standards."""
    ckan = CKAN(ckan_server)
    logger.debug(f"Retrieving dataset {record_id}")
    record = ckan.get_record(record_id)
    if not record:
        logger.error(f"Dataset {record_id} not found.")

    logger.debug(f"Converting dataset {record_id}")
    converter = standard_formats[output_format]
    converted = converter(record)

    if output_file:
        with open(output_file, "w") as f:
            f.write(converted)
    else:
        return converted

if __name__ == "__main__":
    main()