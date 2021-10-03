# Collecting Results using Python script

Every program execution of AutoDock-Aurora and AutoDock-GPU produce a `*.dlg` file.

Such file contains the predicted molecular poses as well runtime information.

The Python script [collect_results_dlg.py](./collect_results_dlg.py):
* Automates the extraction of the _docking runtimes_ from all `*.dlg` files within a given folder
* Collects these runtimes into excel files

## Instructions

Let us say the resulting `*.dlg` files from executing AutoDock-Aurora (following [the instructions given in this repository](./USAGE_AURORA.md))
are stored within a folder called `results_aurora`.

1. Make sure the `results_aurora` folder contains only `*.dlg` files.

Otherwise the script fails.

2. Run the script specifying the folder containing the `*.dlg` files.

`python3 collect_results_dlg.py results_aurora/`
