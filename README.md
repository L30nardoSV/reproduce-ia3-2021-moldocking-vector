# Reproducing IA^3 2021 Paper: _Mapping Irregular Computations for Molecular Docking to the SX-Aurora TSUBASA Vector Engine_

This repository contains the scripts and configuration files used in the 
Artifact Appendix of the article submitted to [IA^3 2021](https://hpc.pnl.gov/IA3) **(currently in press)**.

These scripts automate the evaluation of two molecular docking programs on different platforms:
* [AutoDock-Aurora](https://github.com/esa-tu-darmstadt/AutoDock-Aurora) **(developed in this work)** on the SX-Aurora TSUBASA Vector Engine
* [AutoDock-GPU](https://github.com/ccsb-scripps/AutoDock-GPU) (state-of the art) on GPUs & CPUs

## Instructions

These are provided for each program:

1. [AutoDock-Aurora (instructions)](./USAGE_AURORA.md)
2. [AutoDock-GPU (instructions)](./USAGE_GPU.md)

## Optional

This step automates the collecting of runtimes used in the article's discussion:

* [Collecting results](./USAGE_COLLECT-RESULT-SCRIPT.md)

