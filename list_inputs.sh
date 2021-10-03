#!/bin/bash

#set -o xtrace

# Defining dataset
# Source: https://gitlab.com/L30nardoSV/ad-gpu_miniset_20

## Full and basic data subset
LIST_PDBS_FULL=(1u4d 1xoz 1yv3 1owe 1oyt 1ywr 1t46 2bm2 1mzc 1r55 5wlo 1kzk 3s8o 5kao 1hfs 1jyq 2d1o 3drf 4er4 3er5)
LIST_PDBS_BASIC=(1u4d 1yv3 1mzc)

## Complementary data subsets, based on the number of rotatable bonds
LIST_PDBS_MAX_8_ROTBONDS=(1u4d 1xoz 1yv3 1owe 1oyt 1ywr 1t46 2bm2 1mzc)
LIST_PDBS_MIN_9_ROTBONDS=(1r55 5wlo 1kzk 3s8o 5kao 1hfs 1jyq 2d1o 3drf 4er4 3er5)

# Execution parameters
NEV=2048000
NGEN=99999
NRUN=100
EVAL_INPUTS_20_DIR=./ad-gpu_miniset_20/data # Inputs to be tested
LIST_PSIZES=(128 256 512 1024 2048) # Population sizes to be tested
LS_METHODS=(sw ad) # Local-Search methods to be tested
