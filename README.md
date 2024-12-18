# Token Extractor for API Access to Banco XXX Services (version 1.0)

A microservice that extracts the API access key (token) required to interact with Banco XXX services. 

## Features
- Extracts the token from a JSON file.
- Returns the token in a standardized format.
- Provides detailed error messages for incorrect usage.
- Includes a help menu for guidance.

## Requirements
- Python 3.x installed on your system.
- Ensure the required JSON file is available at the specified path.

## Installation
No installation is needed. Simply ensure you have the executable file `getJason.pyc` and the necessary JSON input file.

## Usage

Run the program as follows:
`{executable path}/getJason.pyc {JSON file path}/{JSON file name}.json`

### Example
`./getJason.pyc ./sitedata.json`

The program will output the token in the following format:
`{1.0}XXXX-XXXX-XXXX-XXXX`

## Help Menu

For a detailed help message, run:
`./getJason.pyc -h`

## Error Handling

The program ensures all error conditions are handled gracefully and will provide descriptive error messages in cases such as:
- Missing or incorrect file paths.
- Invalid or improperly formatted JSON files.
- Any other unexpected issues.

## Contributing
Feel free to fork this repository and submit pull requests for any improvements or new features.

