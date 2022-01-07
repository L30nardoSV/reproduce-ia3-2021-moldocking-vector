# Reproducing IA^3 2021 paper: _Mapping Irregular Computations for Molecular Docking to the SX-Aurora TSUBASA Vector Engine_

This repository contains the scripts and configuration files used in the 
_Artifact Appendix_ of the article accepted at the [11th Workshop on Irregular Applications: Architectures and Algorithms (IA^3), 2021](https://hpc.pnl.gov/IA3):

The paper has been published on IEEExplore:: https://doi.org/10.1109/IA354616.2021.00008.

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

