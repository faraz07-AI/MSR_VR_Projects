# MSR VR Projects

This repository contains tools and scripts designed for managing and analyzing VR-related repositories. The goal of this project is to clone various VR projects, traverse their commit history, and extract relevant data based on predefined criteria. This data can be used for performance analysis, optimization, and understanding key changes in VR software development.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
  - [Cloning Repositories](#cloning-repositories)
  - [Analyzing Commits](#analyzing-commits)
  - [Keywords for Commit Filtering](#keywords-for-commit-filtering)
- [Configuration](#configuration)
- [Project Structure](#project-structure)
- [Contributing](#contributing)

## Project Overview

The MSR VR Projects tool automates the cloning and analysis of VR repositories. It uses Python scripts to traverse commit histories, extract relevant commit messages, and store useful information for further analysis.

## Features

- Clone VR repositories from a specified list of URLs.
- Traverse and analyze commit history using `pydriller`.
- Extract and filter commit messages based on specified keywords.
- Store relevant commit information in a CSV file for further processing.

## Requirements

The project relies on the following dependencies:

- Python 3.10 or above
- Git
- `pydriller` - A Python package to mine Git repositories
- `python-dotenv` - For loading environment variables
- `gitpython` (optional, if used)

To install the dependencies, use:

```bash
pip install -r requirements.txt

## Installation
Clone the repository:
git clone https://github.com/faraz07-AI/MSR_VR_Projects.git
cd MSR_VR_Projects
Install the required Python packages as mentioned in the Requirements section.

## Usage
Cloning Repositories
The clone.py script handles cloning of repositories listed in a text file specified by the GIT_REPO_FILES environment variable.

## Analyzing Commits
The main.py script traverses the commit history of cloned repositories and extracts relevant information based on a predefined list of keywords. The extracted data is saved in a CSV file.

## To execute:

python src/main/clone.py
python src/main/main.py

## Keywords for Commit Filtering
The following keywords are used to filter commit messages:

performance
speed up
accelerate
fast
slow
latency
contention
optimize
efficient
Configuration
Environment variables are used to configure the project. Create a .env file in the root directory and add the following variables:

PROJECT_DIR=/path/to/your/project_directory/
ROOT_DIR=/path/to/your/root_directory/
GIT_REPO_FILES=path/to/repo_list.txt

## Project Structure

```bash
MSR_VR_Projects/
├── src/
│   ├── main/
│   │   ├── clone.py        # Script for cloning repositories
│   │   ├── main.py         # Main script for traversing and analyzing commits
│   │   └── utility.py      # Utility functions for extracting repository details
├── .env                    # Environment variables configuration
├── requirements.txt        # List of required Python packages
└── README.md               # Project documentation (this file)

## Contributing
Contributions are welcome! Please fork this repository and create a pull request with your proposed changes. For major changes, please open an issue first to discuss what you would like to change.



