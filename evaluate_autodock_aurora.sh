# Script that runs both local search methods.
# Parametrization focused on population size, so that
# a comparison against GPUs/CPUs can be made

#!/bin/bash

source list_inputs.sh
source evaluate.sh

RES_AURORA_DIR=results_aurora
AURORA_VH_BIN=./autodock-aurora
AURORA_VE_BIN=./bin/libkernel_ga.so

# Bash functions
function verify_folder_results_exist_in_local_folder() {
    if [ ! -d ${RES_AURORA_DIR} ]; then
        mkdir ${RES_AURORA_DIR}
    else
        echo "${info}: Be cautious. Folder \"${RES_AURORA_DIR}\" for storing results already exists!"
    fi
}

function verify_binaries_exist_in_local_folder() {
  echo " "
  echo "${info}: Verifying that AutoDock-Aurora binaries are present in current folder."
  echo " "
  
  if [ -f "${AURORA_VH_BIN}" ]; then
    echo "${info}: \"${AURORA_VH_BIN}\" exists."
  else
    echo "${info}: \"${AURORA_VH_BIN}\" does not exist. Make sure binary is copied over first!"
    echo "${info}: Terminated."
    exit 9999 # Die with error code 9999
  fi

  if [ -f "${AURORA_VE_BIN}" ]; then
    echo "${info}: \"${AURORA_VE_BIN}\" exists."
  else
    echo "${info}: \"${AURORA_VE_BIN}\" does not exist. Make sure binary is copied over first!"
    echo "${info}: Terminated."
    exit 9999 # Die with error code 9999
  fi
}

# Main execution
verify_folder_results_exist_in_local_folder
verify_binaries_exist_in_local_folder
evaluate ${AURORA_VH_BIN} ${RES_AURORA_DIR}
