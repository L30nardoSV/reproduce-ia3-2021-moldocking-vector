# Benchmarking AutoDock-Aurora

## 1. Clone AutoDock-Aurora and scripts

```bash
git clone --single-branch --branch sx-aurora --recursive https://github.com/esa-tu-darmstadt/AutoDock-Aurora.git
cd AutoDock-Aurora

git clone https://github.com/L30nardoSV/reproduce-ia3-2021-moldocking-vector.git
```

## 2. Compile and copy binaries into main folder

The compilation command below is a general one, so make sure to e.g., enable multiple processes, if desired.

```bash
mkdir bin && make CONFIG=RELEASE OMP=YES
cp bin/autodock-aurora reproduce-ia3-2021-moldocking-vector/
mkdir reproduce-ia3-2021-moldocking-vector/bin && cp bin/libkernel_ga.so reproduce-ia3-2021-moldocking-vector/bin
```

## 3. Run benchmarks

```bash
cd reproduce-ia3-2021-moldocking-vector
cp -rf ../ad-gpu_miniset_20 .
./evaluate_autodock_aurora.sh
```
