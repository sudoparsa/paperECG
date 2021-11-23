# Paper ECG

An application for digitizing ECG scans. (2021 Project)

See [paper-ecg](https://github.com/Tereshchenkolab/paper-ecg) for the main code.

## Authors

- Parsa Hosseini

## Overview

This code allows digitizing paper ECG image scans. Also, it scans the images with OCR.

## Installation

Download the latest release [here](https://github.com/sudoparsa/paperECG/releases).


## Setup Instructions (Windows)

This guide takes you from a fresh install of Windows to having the project running.

The steps involved are:

1. [Installing Python 3.6.7](#1-install-python-367)
1. [Installing dependencies](#2-install-dependencies)
1. [Install Tesseract](#3-install-tesseract)



### 1. Install Python 3.6.7

1. Install Python `3.6.7` via official installer. 

    - [Click here](https://www.python.org/ftp/python/3.6.7/python-3.6.7-amd64.exe) to download the installer.

        *OR*
    - View other installation options on the [python website](https://www.python.org/downloads/release/python-367/).

1. Verify that the install was successful with `py -3.6 --version`:

    ```
    > py -3.6 --version
    3.6.7
    ```



### 2. Install Dependencies

1. Navigate to the project root directory (`...\paperECG\`) and run:

    ```
    py -3.6 -m pip install --upgrade pip
    py -3.6 -m pip install -r requirements.txt
    ```



### 3. Install Tesseract

1. Install Google Tesseract OCR.

- [Click here](https://github.com/tesseract-ocr/tesseract) to see additional info how to install the engine on Linux, Mac OSX and Windows. Look for the binary installer for windows.

- You must be able to invoke the tesseract command as tesseract. If this isn’t the case, for example because tesseract isn’t in your PATH, you will have to change the “tesseract_cmd” variable pytesseract.pytesseract.tesseract_cmd. So all you have to do for this project is to change config.ini file.
---

You should now have:

- Python 3.6.7
- All required packages
- Tesseract-OCR


## Run

In order to to run the program first edit config.ini. Set all four paths.

Now you have to run src\main\python\Main.py

```
py -3.6 main.py
```


## Dependencies

The project currently requires Python `3.6.7`.

