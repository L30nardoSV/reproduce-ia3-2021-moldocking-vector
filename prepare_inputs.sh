# Script that prepares molecular inputs.
# Automatically pulls git submodule first.
# This should be run at the very beginning.

#!/bin/bash

set -o xtrace

# Pulling dataset
# Source: https://gitlab.com/L30nardoSV/ad-gpu_miniset_20
git submodule update --init --recursive
