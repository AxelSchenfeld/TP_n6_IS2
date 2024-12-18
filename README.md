# Token Extractor for API Access to Banco XXX Services (version 1.0)

This program allows the extraction of the API access key to use Banco XXX services.

## Usage

The program operates as a microservice and can be invoked using the following command:

`{executable path}/getJason.pyc {JSON file path}/{JSON file name}.json`

### Example

`./getJason.pyc ./sitedata.json`

The token will be retrieved via the standard output in the following format:

`{1.0}XXXX-XXXX-XXXX-XXXX`

## Help

To get a detailed help message, run:

`./getJason.pyc -h`

## Exceptions

All error conditions will produce an appropriate error message before the program terminates.


