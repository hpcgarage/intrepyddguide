#!/usr/bin/env bash

rm -f notebooks.tar.bz2
git ls-tree --full-tree -r --name-only HEAD \
    | grep "^notebooks/" \
    | xargs tar cvf - \
    | bzip2 -c > notebooks.tar.bz2

# eof
