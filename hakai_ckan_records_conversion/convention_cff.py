import yaml


def convention_cff(record):
    record = {
        "title": "Convention for the File Format",
        "version": "1.2.0",
        "date": "2018-06-25",
        "authors": [
            {
                "name": "Hakai Institute",
                "email": "",
            }
        ],
    }
    return yaml.dump(record, default_flow_style=False)
