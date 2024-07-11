# CKAN Metadata Format Generator

:warning: We recommand using the [hakai-metadata-conversion](https://github.com/HakaiInstitute/hakai-metadata-conversion) [^1] :warning:
[^1]: The [hakai-metadata-conversion](https://github.com/HakaiInstitute/hakai-metadata-conversion) relies on the original metadata form schema instead of the CKAN one.

This project provides a tool to generate various metadata formats and standards
from CKAN (Comprehensive Knowledge Archive Network) catalog records. It aims to
facilitate the sharing and citation of datasets by converting CKAN metadata into
widely recognized standards.

## Currently Supported Standards

- `citation.cff`: Citation File Format, a human and machine-readable file format
which provides citation metadata for software.

## Features

- **Easy Integration**: Seamlessly integrates with existing CKAN instances to
fetch catalog records.
- **Extensible**: Designed with extensibility in mind, allowing for the addition
of more metadata standards in the future.
- **User-Friendly**: Provides a simple and intuitive interface for generating
metadata files.

## Getting Started

To use this tool, follow these steps:

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/your/repository.git
   cd repository
   ```

2. **Install Dependencies:**

    ```bash
    pip install -e .
    ```

3. **Run the Tool:**
4. mkd

    ```bash
    python generate_metadata.py
    ```

## How to Contribute

We welcome contributions! If you would like to add support for more metadata standards or improve the tool, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature (git checkout -b feature/AmazingFeature).
3. Commit your changes (git commit -m 'Add some AmazingFeature').
4. Push to the branch (git push origin feature/AmazingFeature).
5. Open a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

Thanks to the CKAN community for providing the platform that inspired this tool.
Special thanks to all contributors who have helped extend and maintain this project.
