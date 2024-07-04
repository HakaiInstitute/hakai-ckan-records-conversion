import pytest
import requests

from click.testing import CliRunner

from hakai_ckan_records_conversion import convention_cff, erddap
from hakai_ckan_records_conversion.ckan import CKAN
from hakai_ckan_records_conversion.__main__ import main as convert_records


@pytest.fixture
def ckan_url():
    return "https://catalogue.hakai.org"


@pytest.fixture
def ckan(ckan_url):
    return CKAN(ckan_url)


@pytest.fixture
def record_id():
    return "ca-cioos_86343dd1-28d0-4d02-8eaf-402d51a7fef7"


@pytest.fixture
def record(ckan, record_id):
    return ckan.get_record(record_id)


def test_record_is_available(ckan, record_id):
    response = requests.get(f"{ckan.base_url}/dataset/{record_id}")
    assert response.status_code == 200


def test_get_record(ckan, record_id):
    record = ckan.get_record(record_id)
    assert record
    assert record["id"] == record_id
    assert record["title"] == "Hakai Inisostitute - CTD Data"
    assert record["name"] == "hakai-institute-ctd-data"
    assert record["state"] == "active"
    assert record["private"] == False
    assert record["revision_id"] == "d0d1c1b5-6e4b-4a6d-8d0d-7b5d8d0d1c1b"
    assert record["type"] == "dataset"
    assert record["owner_org"] == "hakai"
    assert record["author"] == "Hakai Institute"


@pytest.mark.parametrize("output_format", ["json", "yaml","erddap","cff"])
def test_get_record_json(ckan_url, record_id, tmp_path, output_format):
    output_file = tmp_path / f"output.{output_format}"
    runner = CliRunner()
    result = runner.invoke(convert_records, ["--ckan-server",ckan_url, "--dataset-ids",record_id, "--output-format",output_format, "--output-file", str(output_file)]) 
    assert result.exit_code == 0, result.output
    assert output_file.exists()
    



def test_get_record_cff(record):
    cff = convention_cff.convention_cff(record)
    assert cff
    assert cff["title"] == "Convention for the File Format"
    assert cff["version"] == "1.2.0"
    assert cff["date"] == "2018-06-25"
    assert cff["authors"] == [{"name": "Hakai Institute", "email": ""}]


def test_get_record_erddap_dataset_xml(record):
    dataset_xml = erddap.dataset_xml(record)
    assert dataset_xml


