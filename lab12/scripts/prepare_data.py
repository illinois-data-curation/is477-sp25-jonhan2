"""
IS477 Data Management, Curation, and Reproducibilty

This script downloads and verifies the following dataset:

  Becker, Barry and Kohavi, Ronny. (1996). Adult.
  UCI Machine Learning Repository.
  https://doi.org/10.24432/C5XW20.
"""

import requests
import os
import hashlib
import zipfile

def unzip(path_to_zip, target_path): 
    print (f"Unzipping {path_to_zip}")
    with zipfile.ZipFile(path_to_zip) as z:
        z.extractall(target_path)

def download_and_validate(url, path, expected_hash):

    response = requests.get(url)
    response.raise_for_status()

    if not os.path.exists(path):
        base_dir = os.path.dirname(path)
        print(f"Creating directory for {path}")
        os.makedirs(base_dir, exist_ok=True)

    with open(path, mode="wb") as f:
        f.write(response.content)

    with open(path, mode="rb") as f:
        data = f.read()
        computed_hash = hashlib.sha256(data).hexdigest()

    if computed_hash != expected_hash:
        print(f"WARNING: Computed hash does not match expected has for {path}")
    else:
        print(f"INFO: Computed hash matches expected hash for {path}")

# UCI Adult Dataset https://doi.org/10.24432/C5XW20
uci_adult_path = "data/adult.zip"
uci_adult_url = "https://archive.ics.uci.edu/static/public/2/adult.zip"
uci_adult_expected_hash = "7537312dd56c2b98035880805ce99e68183a30ee468aa5329d6df0fbb3cc21bb"

# Download, validate, and extract the UCI Adult dataset
download_and_validate(uci_adult_url, uci_adult_path, uci_adult_expected_hash)
unzip(uci_adult_path, "data/adult")
