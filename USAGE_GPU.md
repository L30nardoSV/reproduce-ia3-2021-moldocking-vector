# Benchmarking AutoDock-GPU

## 1. Clone AutoDock-GPU and scripts

```bash
git clone --depth 1 --branch v1.1 https://github.com/ccsb-scripps/AutoDock-GPU.git
cd AutoDock-GPU

git clone https://github.com/L30nardoSV/reproduce-ia3-2021-moldocking-vector.git
```

## 2. Apply git patch to AutoDock-GPU v1.1

Regarding execution times, AutoDock-GPU v1.1 only prints full program run-time.

In order to additionally print _docking run-times_, apply the following git patch:

```
cp reproduce-ia3-2021-moldocking-vector/adgpu_v1.1_runtimes.patch .
git apply --verbose --ignore-whitespace adgpu_v1.1_runtimes.patch
```

Expected output once patching:

```
Checking patch host/src/performdocking.cpp...
Applied patch host/src/performdocking.cpp cleanly.
```

## 3. Set environment variables for AutoDock-GPU

Key ideas:

* Include path: contains "CL" folder, which in turn contains OpenCL header files (e.g., `cl.h`, `opencl.h`, etc)
* Library path: contains the `libOpenCL.so` file

Example for GPU:

```bash
export GPU_INCLUDE_PATH=/usr/local/cuda/include
export GPU_LIBRARY_PATH=/usr/local/cuda/lib64
```

Example for CPU:

```bash
export CPU_INCLUDE_PATH=/opt/intel/opencl/include
export CPU_LIBRARY_PATH=/opt/intel/opencl
```

## 4. Compile and copy binaries into main folder

For GPU:

```bash
make DEVICE=GPU
cp bin/autodock_gpu_64wi reproduce-ia3-2021-moldocking-vector/
```

For CPU:

```bash
make DEVICE=CPU
cp bin/autodock_cpu_16wi reproduce-ia3-2021-moldocking-vector/
```

## 5. Run benchmarks

```bash
cd reproduce-ia3-2021-moldocking-vector
./prepare_inputs.sh
./evaluate_autodock_gpu.sh
```
