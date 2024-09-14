#!/bin/sh
# This is a comment!
echo Hello World        # This is a comment, too!
fastapi run quizapp/main.py &
ORIGIN=http://localhost:3000 node ./client/main.js