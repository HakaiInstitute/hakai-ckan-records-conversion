"""
Module dedicated to the citation file format:
<https://citation-file-format.github.io>
"""


import yaml
from loguru import logger


def get_cff_author(author):
    return {
        "name": author["individual-name"],
        "email": author["contact-info_email"],
        "role": ','.join(author["role"]),
        "affiliation": author["organisation-name"],
        "orcid": author.get("individual-uri_code"),
        "orgniasation": author.get("organisation-name"),
        "ror": author.get("organisation-uri_code"),
    }

def convention_cff(record, output_format="yaml"):
    """Generate a convention.cff file from a CKAN record.

    This is based on the documentation at: 
    <https://github.com/citation-file-format/citation-file-format/blob/main/schema-guide.md#identifiers>
    """
    record = {
        "title": record['title'],
        "abstract": record['notes'],

        "cff-version": "1.2.0",
        "date": record['metadata_modified'],
        "contact": [
            get_cff_author(author) for author in record['metadata-point-of-contact']
        ],
        "authors": [
            get_cff_author(author) for author in record['cited-responsible-party']
                
        ],
        "identifiers": [],
        "keywords": record['keywords']["en"] + record["keywords"]["fr"],   
        "license": record['license_id'],
        "license-url": record['license_url'],
        "message": record['notes'],
        "preferred-citation": f"en: {record['citation']['en']}\n" + f"fr: {record['citation']['en']}",
        "type": record["resource-type"],
        "url": record['url'],
        "version": record.get('version'), #TODO: check if this is the correct field
    }
    if doi := record.get('unique-resource-identifier-full',{}).get("code"):
        record["identifier"] += [{
            "description": "Hakai Metadata record DOI",
            "type": "doi",
            "value": doi.replace(' https://doi.org/','')
        }]
    if output_format=="yaml":
        return yaml.dump(record, default_flow_style=False)
    return record
