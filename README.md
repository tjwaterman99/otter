# Otter

DLI Gradebook management software.

## Install

[Download and install Python](https://www.python.org/downloads/), using at least version 3.12.

Then install `pipx` using the Python package manager `pip`.

```
pip install pipx
```

Using `pipx`, install `otter`.

```
pipx install git@github.com:tjwaterman99/otter.git
```

Finally, confirm that the installation was successful by running the following command.

```
otter --help
```

## Usage

1. Create a free account at [llamaindex.ai](https://cloud.llamaindex.ai/login).
2. Create a new llamaindex.ai API key. 
  - Click on "API Key" on the left hand navigation, and then the `Generate New Key` button. 
  - Copy and save the value of the generated API key. This key will be used later
3. Set the API Key in your environment: `export LLAMA_CLOUD_API_KEY=...`

### Convert a Gradebook to .csv format

```
otter gradebooks convert --format csv path/to/gradebook.xlsx
```
