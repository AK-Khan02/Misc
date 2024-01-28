# Congress Trading History Retriever

This Python script retrieves the trading history of members of Congress by downloading and processing financial disclosure documents from the official disclosures clerk website. Users can choose to retrieve data for the top 36 active traders among the members of Congress or specify a member to get their trading history for a given year.

## Features

- Retrieve trading history for the top 36 active traders in Congress.
- Retrieve trading history for a specific member of Congress.
- Download and process financial disclosure PDFs for the specified year.

## Getting Started

### Prerequisites

- Python 3.x installed on your machine.
- Required Python packages: `requests`, `zipfile` (part of the standard library), `os` (standard library), `csv` (standard library).

### Installation

1. Clone this repository or download the script to your local machine.

    ```bash
    git clone https://your-repository-url.git
    ```

2. Navigate to the script's directory.

3. Install the required Python packages (if not already installed).

    ```bash
    pip install requests
    ```

### Configuration

- Update the `BASE_PATH` variable in the script to the desired location on your machine where files will be downloaded and processed.
- Ensure you have permission to write to the `BASE_PATH` directory.

## Usage

Run the script from your terminal or command prompt:

```bash
python congress_trading_history.py
```
Follow the on-screen prompts to choose between retrieving data for the top 36 active traders or a specific member, and enter the year of interest.

## Example

```python
Enter [1] for the top 36 active Congress traders, [2] for a specific member: 1
Enter the year of trading history (at least 2008): 2020
```
