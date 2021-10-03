# Script that runs both local search methods.
# Parametrization focused on population size, so that
# a comparison against SX-Aurora can be made

#!/bin/bash

source list_inputs.sh
source evaluate.sh

ADGPU_GPU_BIN=./autodock_gpu_64wi
ADGPU_CPU_BIN=./autodock_cpu_16wi

# Bash functions
function select_device() {
  echo " "
  echo "${info}: Selecting device to test with AutoDock-GPU."
  echo " "
  echo "${info}: GPU? "
  read -p "[Y]: " TEST_GPU
  if [ "${TEST_GPU}" == "Y" ]; then
    echo " "
    echo "${info}: Type a meaningful label for your GPU device."
    read -p "E.g.: [v100] [rtx270] [rtx370] [vega56] [vega64] [etc]: " LABEL_GPU
    RES_GPU_DIR=results_${LABEL_GPU}
    if [ ! -d ${RES_GPU_DIR} ]; then
      mkdir ${RES_GPU_DIR}
    else
      echo "${info}: Be cautious. Folder \"${RES_GPU_DIR}\" for storing results already exists!"
    fi
  fi

  echo " "
  echo "${info}: CPU? "
  read -p "[Y]: " TEST_CPU
  if [ "${TEST_CPU}" == "Y" ]; then
    echo " "
    echo "${info}: Type a meaningful label for your CPU device."
    read -p "E.g.: [i5-4cores] [aws-18cores] [etc]: " LABEL_CPU
    RES_CPU_DIR=results_${LABEL_CPU}
    if [ ! -d ${RES_CPU_DIR} ]; then
      mkdir ${RES_CPU_DIR}
    else
      echo "${info}: Be cautious. Folder \"${RES_CPU_DIR}\" for storing results already exists!"
    fi
  fi

  echo " "
  echo "${info}: Devices to be tested: "
  if [ "${TEST_GPU}" == "Y" ]; then
    echo "\"${LABEL_GPU}\" GPU "
  fi
  if [ "${TEST_CPU}" == "Y" ]; then
    echo "\"${LABEL_CPU}\" CPU "
  fi
  if [ "${TEST_GPU}" != "Y" ] && [ "${TEST_CPU}" != "Y" ]; then
    echo "${info}: No device chosen."
    echo "${info}: Terminated."
    exit 9999 # Die with error code 9999
  fi
}

function verify_binaries_exist_in_local_folder() {
  echo " "
  echo "${info}: Verifying that AutoDock-GPU binaries are present in current folder."
  echo " "
  if [ "${TEST_GPU}" == "Y" ]; then
    if [ -f "${ADGPU_GPU_BIN}" ]; then
      echo "${info}: \"${ADGPU_GPU_BIN}\" exists."
    else
      echo "${info}: \"${ADGPU_GPU_BIN}\" does not exist. Make sure binary is copied over first!"
      echo "${info}: Terminated."
      exit 9999 # Die with error code 9999
    fi
  fi

  if [ "${TEST_CPU}" == "Y" ]; then
    if [ -f "${ADGPU_CPU_BIN}" ]; then
      echo "${info}: \"${ADGPU_CPU_BIN}\" exists."
    else
      echo "${info}: \"${ADGPU_CPU_BIN}\" does not exist. Make sure binary is copied over first!"
      echo "${info}: Terminated."
      exit 9999 # Die with error code 9999
    fi
  fi
}

# Main execution
select_device
verify_binaries_exist_in_local_folder
if [ "${TEST_GPU}" == "Y" ]; then
  evaluate ${ADGPU_GPU_BIN} ${RES_GPU_DIR}
fi
if [ "${TEST_CPU}" == "Y" ]; then
  evaluate ${ADGPU_CPU_BIN} ${RES_CPU_DIR}
fi
