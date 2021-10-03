# Benchmarking AutoDock-Aurora

## 1. Clone AutoDock-Aurora and scripts

```bash
git clone --single-branch --branch sx-aurora --recursive https://gitlab.com/postdoc_tud/molecular-docking/autodock-aurora/autodock-aurora-2.git
cd autodock-aurora-2

git clone https://gitlab.com/postdoc_tud/molecular-docking/autodock-aurora/autodock-aurora-2-benchmarks-ia3-2021.git
```

## 2. Compile and copy binaries into main folder

The compilation command below is a general one, so make sure to e.g., enable multiple processes, if desired.

```bash
mkdir bin && make CONFIG=RELEASE OMP=YES
cp bin/autodock-aurora-2 autodock-aurora-2-benchmarks-ia3-2021/
mkdir autodock-aurora-2-benchmarks-ia3-2021/bin && cp bin/libkernel_ga.so autodock-aurora-2-benchmarks-ia3-2021/bin
```

## 3. Run benchmarks

```bash
cd autodock-aurora-2-benchmarks-ia3-2021
cp -rf ../ad-gpu_miniset_20 .
./evaluate_autodock_aurora.sh
```
