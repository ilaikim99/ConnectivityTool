
# Connectivity Tool

A command-line tool to test internet connectivity for various websites and protocols.
Testing capabilities include testing connectivity to a website and measuring
latency.


## Run Locally

Clone the project

```bash
git clone https://github.com/ilaikim99/ConnectivityTool.git 
```

Go to the project directory

```bash
cd path/to/ConnectivityTool
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the script (input/output files are optional, will use the default files from example dir).

```bash
python run.py --input_file path_to_input.yaml --output_file path_to_output.csv
```

## Run Tests

Go to the project directory

```bash
cd path/to/ConnectivityTool
```


Run with pytest

```bash
python -m pytest test
```


## Future Improvements

- Add bandwidth test - in http_tester.py the test function will call a new bandwidth_test function, and the result will be added to the additional_info dict.
- Make it a plug & play tool - upload the code as package to pypi. And just doing pip install connectivity-tool, and running connectivity-tool command from terminal will run the tests.
- Add lock when writing to the csv, to avoid race conditions.
- Store the results in a dedicated DB rather than a file (e.g: adding orm model to TestInstance using sqlalchemy/implementing different ResultsStorage class).
- Add more documentation in the code.
- Add more unit tests.
