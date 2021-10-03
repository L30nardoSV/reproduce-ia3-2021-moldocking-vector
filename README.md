# Reproducing IA^3 2021 Paper: Mapping Irregular Computations for Molecular Docking to the SX-Aurora TSUBASA Vector Engine

This repository contains the scripts and configuration files used in the 
Artifact Appendix of the aforementioned article submitted to IA^3 2021 **(currently under revision)**.

These scripts automate the evaluation of two molecular docking programs:
* AutoDock-Aurora on SX-Aurora TSUBASA (developed in this work)
* AutoDock-GPU on GPUs/CPUs (state-of the art)

## Instructions

Detailed instructions are provided for each program:

1. [AutoDock-Aurora](./USAGE_AURORA.md)
2. [AutoDock-GPU](./USAGE_GPU.md)

## Optional

This step automates the collecting of runtimes used in the article's discussion:

* [Collecting results](./USAGE_COLLECT-RESULT-SCRIPT.md)

