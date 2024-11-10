# MSR_VR_Projects
Data analysis for VR projects
Sure! Below is the detailed **README** file that provides instructions on how to set up, run, and use your project, considering that you're using **PyDriller** for mining Git repositories based on performance-related bug fixes.

---

# VR Performance Bug Fix Mining from GitHub Repositories

This project is aimed at mining GitHub repositories to identify performance-related bug fixes in Virtual Reality (VR) projects. We use **PyDriller** to analyze the commit messages and search for performance-related keywords. The results are stored in a CSV file containing the project name, performance-related commit message, and commit ID.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Configuration](#configuration)
5. [Usage](#usage)
6. [Folder Structure](#folder-structure)
7. [Generated Output](#generated-output)
8. [Contributing](#contributing)
9. [License](#license)

## Project Overview

This project analyzes multiple GitHub repositories, clones them locally, and searches for performance-related fixes based on specific keywords. The result is a CSV file that contains the following information:

- **Project Repo Name**: The name of the repository.
- **Performance Fix Commit Message**: The commit message where a performance fix is identified.
- **Commit ID**: The unique identifier for each commit.

## Prerequisites

Before running the project, make sure the following tools and dependencies are installed:

1. **Python 3.x** (Recommended: Python 3.8+)
2. **pip** (Python's package installer)
3. **Virtual Environment (Optional but Recommended)**

### Python Libraries
- **PyDriller**: A Python library for mining Git repositories.
- **dotenv**: For reading configuration variables from a `.env` file.
- **GitPython** (Optional if required for other git operations)

Install required Python libraries:

```bash
pip install -r requirements.txt
```

### Environment Configuration

1. **.env file**: A `.env` file is included in the project to manage the configuration parameters. This file contains variables for:

    - `PROJECT_REPO_PATH`: Path to store the cloned repositories locally.
    - `CSV_OUTPUT_PATH`: Path where the output CSV file will be saved.

Example `.env` file:

```
PROJECT_REPO_PATH=./project_repo
CSV_OUTPUT_PATH=./project_repo/performance_fixes.csv
```

Make sure to edit this file with the correct paths for your local setup.

## Installation

1. Clone this repository to your local machine:

```bash
git clone <repository_url>
cd <repository_directory>
```

2. Install the required Python dependencies:

```bash
pip install -r requirements.txt
```

3. Make sure you have the **.env** file properly configured for paths.

## Configuration

Before running the program, you need to configure the following:

1. **.env File**: Update the `.env` file with the correct paths for the local project folder and the location where the CSV output should be stored.

    Example of `.env` file:
    ```text
    PROJECT_REPO_PATH=./project_repo
    CSV_OUTPUT_PATH=./project_repo/performance_fixes.csv
    ```

    - `PROJECT_REPO_PATH`: Path where the repositories will be cloned.
    - `CSV_OUTPUT_PATH`: Path where the CSV file will be saved.

2. **GitHub Repository List**: Make sure that the text file with the list of GitHub repository URLs (provided in the assignment) is accessible by the program. This will be used by `clone.py` to clone each repository.

## Usage

### Step 1: Clone the GitHub Repositories

To start the process, use the `clone.py` script to clone all the repositories mentioned in the project list text file.

```bash
python clone.py
```

This script will:
- Read the list of repository URLs from the provided text file.
- Clone each repository into the directory specified by `PROJECT_REPO_PATH`.

### Step 2: Mine Commit Data for Performance Fixes

Once the repositories are cloned, use the `main.py` script to mine the commit data.

```bash
python main.py
```

This script will:
- Load each cloned project.
- Search through all the commit messages for performance-related keywords such as "performance", "speed up", "optimize", etc.
- Save the results (Project Repo Name, Commit Message, and Commit ID) into a CSV file located at the `CSV_OUTPUT_PATH`.

### Step 3: View the Output

After running the `main.py`, the generated CSV file (`performance_fixes.csv`) will contain the following columns:

- **Project Repo Name**: The name of the repository.
- **Performance Fix Commit Message**: The commit message containing one of the performance-related keywords.
- **Commit ID**: The unique identifier of the commit.

You can open the CSV file in any text editor or spreadsheet software (e.g., Excel, Google Sheets) to view the results.

## Folder Structure

The project folder should have the following structure:

```
/VR_Performance_Bug_Fix_Mining
    ├── /project_repo                # Cloned repositories will be stored here
    ├── .env                         # Configuration file
    ├── clone.py                     # Script to clone repositories
    ├── main.py                      # Script to mine commits and generate CSV
    ├── requirements.txt             # Python dependencies
    ├── performance_fixes.csv        # Output CSV file (generated after running main.py)
    ├── README.md                    # This readme file
```

## Generated Output

The script will generate a `performance_fixes.csv` file in the `PROJECT_REPO_PATH` folder (as specified in the `.env` file). This CSV file will contain the following columns:

1. **Project Repo Name**: The name of the repository (e.g., "Awesome-VR-Project").
2. **Performance Fix Commit Message**: The commit message related to performance fixes.
3. **Commit ID**: The unique Git commit identifier.

## Contributing

Contributions are welcome! If you find any issues or would like to add features, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### Notes:
- Ensure that the `.env` file is set up correctly before running the scripts.
- You can extend the list of keywords for mining performance-related commits in the future.
