# Collecting Results using a Python script

**Important**: _this step is not mandatory for reproducibility purposes._

Every program execution of AutoDock-Aurora and AutoDock-GPU produce a _*.dlg_ file.

Such file contains the predicted molecular poses as well the program's runtime information.

The Python script [collect_results_dlg.py](./collect_results_dlg.py):
* Automates the extraction of the _docking runtimes_ from all _*.dlg_ files within a given folder
* Collects and organizes these runtimes into excel files

## Instructions

Assuming that the resulting _*.dlg_ files from executing AutoDock-Aurora (following [the instructions given in this repository](./USAGE_AURORA.md))
are stored within a folder called `results_aurora`.

For collecting the _docking runtimes_, proceed as follows:

1. Make sure the `results_aurora` folder contains only _*.dlg_ files (otherwise the script fails)

2. Run the script specifying the folder containing the _*.dlg_ files: `python3 collect_results_dlg.py results_aurora/`

3. Proceed similarly when collecting results from AutoDock-GPU's executions
