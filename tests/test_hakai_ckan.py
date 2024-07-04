import pytest
import requests
from click.testing import CliRunner

from hakai_ckan_records_conversion import citation_cff, erddap
from hakai_ckan_records_conversion.__main__ import main as convert_records
from hakai_ckan_records_conversion.ckan import CKAN


@pytest.fixture
def ckan_url():
    return "https://catalogue.hakai.org"


@pytest.fixture
def ckan(ckan_url):
    return CKAN(ckan_url)


@pytest.fixture
def record_id():
    return "ca-cioos_ba41d935-f293-447f-be3d-7098e569b431"


@pytest.fixture
def record(ckan, record_id):
    return ckan.get_record(record_id)


def test_record_is_available(ckan, record_id):
    response = requests.get(f"{ckan.base_url}/dataset/{record_id}")
    assert response.status_code == 200


def test_get_record(ckan, record_id):
    record = ckan.get_record(record_id)
    assert record
    assert record["name"] == record_id
    assert record["title"] 
    assert record["state"] 
    assert not record["private"]
    assert record["metadata_created"] 
    assert record["metadata_modified"]
    assert record["type"] == "dataset"
    assert record["owner_org"]
    assert record["cited-responsible-party"]
    assert record["resources"]
    assert record['keywords']
    assert record['groups']
    assert record['spatial']
    assert record['projects']


@pytest.mark.parametrize("output_format", ["json", "yaml", "erddap", "cff"])
def test_get_record_json(ckan_url, record_id, tmp_path, output_format):
    output_file = tmp_path / f"output.{output_format}"
    runner = CliRunner()
    result = runner.invoke(
        convert_records,
        [
            "--ckan-server",
            ckan_url,
            "--dataset-ids",
            record_id,
            "--output-format",
            output_format,
            "--output-file",
            str(output_file),
        ],
    )
    assert result.exit_code == 0, result.output
    assert output_file.exists()


def test_get_record_cff(record):
    cff = citation_cff.convention_cff(record, output_format=None)
    assert cff
    assert cff["title"]
    assert cff["cff-version"]
    assert cff["abstract"]
    assert cff["authors"]


def test_get_record_erddap_dataset_xml(record):
    dataset_xml = erddap.dataset_xml(record)
    assert dataset_xml
