import yaml

from hakai_ckan_records_conversion.ckan import CKAN

ckan_url = "https://catalogue.hakai.org"
record_id = "ca-cioos_ba41d935-f293-447f-be3d-7098e569b431"

def generate_local_test_file(output,):
    ckan = CKAN(ckan_url)
    record = ckan.get_record(record_id)
    record.pop("harvest_document_content", None)

    yaml.dump(record, output, default_flow_style=False)

if __name__ == "__main__":
    with open("tests/test_record.yaml", "w") as f:
        generate_local_test_file(f)
