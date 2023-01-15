import os
import sys
from datetime import datetime, timedelta,timezone
from subprocess import check_output

def git_info(path):
    os.chdir(path)
    branch = check_output(['git', 'rev-parse','--abbrev-ref','HEAD']).strip()
    print(f'Active branch:',branch.decode())

    modified_files = check_output(['git', 'status', '--porcelain'])
    print('local changes:',bool(modified_files))

    commit_date = check_output(['git', 'log', '-1', '--format=%ci']).strip()
    commit_datetime = datetime.strptime(commit_date.decode('ascii'), '%Y-%m-%d %H:%M:%S %z')
    recentcommit = datetime.now(timezone.utc) - commit_datetime < timedelta(weeks=1)
    print('recent commit:',bool(recentcommit))

    author = check_output(['git', 'log', '-1', '--format=%an']).strip()
    if author.decode() == 'Rufus':
        print('blame Rufus',True)
    else:
        print('blame Rufus',False)


if __name__ == "__main__":
    path = sys.argv[1]
    git_info(path)
