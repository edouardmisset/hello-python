#!/bin/sh

find ./basics -name '*.py' | entr -nrc sh -c 'python3 "$0"' /_

# 1. find ./basics -name '*.py'
# This finds all files ending with .py in the basics directory (recursively).
# It outputs a list of Python file paths, one per line.

# 2. | entr -n ...
# The output of find is piped into entr.
# entr watches all files listed and runs a command when any of them changes.
# The -n flag tells entr to run the command only if a file is newly written to
# (not just touched).
# The -c flag tells entr to clear the screen before running the command.
# The -r flag tells entr to restart the command if it exits.

# 3. sh -c 'python3 "$0"' /_
# sh -c 'python3 "$0"' /_ runs a shell with the command python3 "$0".
# In this context:
# sh -c allows you to run a shell command as a string.
# "$0" refers to the first positional argument passed to the shell script.
# /_ is the argument passed to the shell script, so $0 becomes /_.
# So, this command will run python3 /_ every time a file changes.
