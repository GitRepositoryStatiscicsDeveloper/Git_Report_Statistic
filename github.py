# -*- coding: utf-8 -*-


from pydriller import Repository

import csv

column_name = ['File', 'Path', 'Commit_Count', 'Code_Churn', 'Contributors']

from pydriller.metrics.process.code_churn import CodeChurn
from pydriller.metrics.process.contributors_count import ContributorsCount
from pydriller.metrics.process.commits_count import CommitsCount

with open('output_3.csv', 'w', encoding='UTF8') as f:
    csvcreator = csv.writer(f)

    csvcreator.writerow(column_name)
    element=[]

    for commit in Repository('https://github.com/GitRepositoryStatiscicsDeveloper/Git_Report_Statistic').traverse_commits():
        print('Commit ID:',commit.hash)
        
        print('Commit Line:', commit.lines)
        print('Commit File: ' ,commit.files)
        print('Commit insertions:', commit.insertions)
        print('Commit deletions:', commit.deletions)
        
        print(commit.msg)
        print('Commit project_path:', commit.project_path )
    
        for file in commit.modified_files:
            element.append(str(file.filename))
            print(file.filename)

            element.append(str(file.filename))
            element.append(str(commit.project_path))

           
            metric_CommitsCount = CommitsCount(path_to_repo='https://github.com/GitRepositoryStatiscicsDeveloper/Git_Report_Statistic',
            from_commit=commit.hash,
            to_commit=commit.hash)

            element.append(str(metric_CommitsCount.count()))
            
 
            
            metric = ContributorsCount(path_to_repo='https://github.com/GitRepositoryStatiscicsDeveloper/Git_Report_Statistic',from_commit=commit.hash,to_commit=commit.hash)
            count = metric.count()
            minor = metric.count_minor()
            element.append(str(count))
            element.append(str(minor))
            

            
            csvcreator.writerow(element)