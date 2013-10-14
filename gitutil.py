#!/usr/bin/python

import sys
import getopt
import os
import git


def check_repo(folder, g):
    changed_str = "Changed" if g.is_dirty() else "Not changed"
    if g.is_dirty():
        print g.working_dir.replace(folder, "", 1).ljust(70), g.active_branch.name.ljust(12), changed_str.ljust(20)


def main(argv):
    folder = ''
    check = False
    try:
        opts, args = getopt.getopt(argv, 'r:c', ["root=", "check"])
    except getopt.GetoptError:
        print('Usage: gitutil.py -r')
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-r", "--root"):
            folder = arg
        elif opt in ("-c", "--check"):
            check = True
    git_roots = []
    for dirname, dirs, files in os.walk(folder):
        if ".git" in dirs:
            git_roots.append(dirname)
            dirs.remove(".git")
    for d in git_roots:
        g = git.Repo(d)
        if check:
            check_repo(folder, g)

if __name__ == "__main__":
    main(sys.argv[1:])