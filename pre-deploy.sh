#!/bin/bash
python pre-deploy.py 2>&1 /dev/null
script_output=$?
TEST_DEPLOY=false
if [ $script_output -eq 0 ]; then
    TEST_DEPLOY=true
else
    TEST_DEPLOY=false
fi