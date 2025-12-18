#!/bin/bash
# Push with rebase to handle auto-generated README.md
git pull --rebase origin main && git push origin main
