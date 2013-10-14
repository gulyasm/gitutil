#!/usr/bin/python

import sys
import getopt
import os
import git


def main(argv):
    folder = ''
    try:
        opts, args = getopt.getopt(argv, 'r', ["root="])
    except getopt.GetoptError:
        print('Usage: gitutil.py -r')
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-r", "--root"):
            folder = arg
    git_roots = []
    for dirname, dirs, files in os.walk(folder):
        if ".git" in dirs:
            git_roots.append(dirname)
            dirs.remove(".git")
    for d in git_roots:
        g = git.Repo(d)
        changed_str = "Changed" if g.is_dirty() else "Not changed"
        if g.is_dirty():
            print g.working_dir.replace(folder, "", 1).ljust(70), g.active_branch.name.ljust(
                12), changed_str.ljust(20)


if __name__ == "__main__":
    main(sys.argv[1:])