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
- [License](#license)

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


