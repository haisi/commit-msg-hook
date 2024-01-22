#!/usr/bin/env bash

files=$(find "tests" -type f -name "fail*")

for file in "tests"/fail-*; do
    if [ -f "$file" ]; then
        echo "Verifying that $file fails"
        ./commit-msg.py "$file"
        if [ $? -eq 0 ]; then
            echo "Test for $file should have failed, but didn't!"
            exit -1
        fi
    fi
done

for file in "tests"/pass-*; do
    if [ -f "$file" ]; then
        echo "Verifying that $file succeeds"
        ./commit-msg.py "$file"
        if [ $? != 0 ]; then
            echo "Test for $file should have succeeded, but didn't!"
            exit -1
        fi
    fi
done

echo ""
echo "=========================="
echo "Yay, you passed all tests!"
echo "=========================="