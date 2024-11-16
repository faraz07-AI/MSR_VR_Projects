#Author Name: Faraz Gurramkonda

import csv
from cmath import e

import pydriller
import os

from pydriller import Repository
from git.exc import InvalidGitRepositoryError

import clone
from dotenv import load_dotenv

from src.main import utility
from utility import extract_details

def clone_reps(result,project_dir,csv_file_path):
    for res_link in result:
        owner_name, project_name = utility.extract_details(res_link)
        repo_directory = project_dir+f"{owner_name}/{project_name}"
        print("repo directory -> traversed: ",repo_directory)
        try:
            for commit in Repository(repo_directory).traverse_commits():
                commit_id = commit.hash
                commit_message = commit.msg
                commit_search_list = ["performance", "speed up", "accelerate", "fast", "slow", "latency", "contention", "optimize", "efficient"]
                for search_keyword in commit_search_list:
                    if search_keyword in commit_message.lower():
                        data = [project_name, commit_message, commit_id]
                        with open(csv_file_path,'a') as csvfile:
                            writer = csv.writer(csvfile)
                            writer.writerow(data)
        except Exception as e:
            print(f"An error occurred with repository {repo_directory} because the repository deos not have the source code: {e}")
    print("data appended to the csv file {}".format(csv_file_path))


if __name__ == "__main__":
    load_dotenv()
    project_dir = os.getenv('PROJECT_DIR')
    root = os.getenv('ROOT_DIR')
    git_repo_file = os.getenv('GIT_REPO_FILES')
    path = root+git_repo_file
    repo = []
    csv_file_path = project_dir+'commit_information.csv'
    result = utility.repo_collection(path, repo)
    clone_reps(result, project_dir,csv_file_path)
