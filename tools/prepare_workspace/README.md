My IDEs of choice for algorithm competitions are CLion IDE and Codeblocks 16. I use the [prepare_workspace.sh](prepare_workspace.sh) script to automate creation of projects that use my [templates](../../templates/).

prepare-workspace script install:
```bash
git clone https://github.com/adw1n/competitive-programming ~/bin/competitive-programming/
sudo ln -s ~/bin/competitive-programming/tools/prepare_workspace/prepare_workspace.sh /usr/local/bin/prepare-workspace
```

prepare-workspace script usage:
```bash
prepare-workspace --round 399 --codeforces # CMake project
prepare-workspace --round 273 --topcoder # CMake project
prepare-workspace --help
prepare-workspace --round 1111 --topcoder --codeblocks # CodeBlocks project
```

Script creates projects in `~/algo_competitions` directory - this path can by changed by modifying the `GENERIC_SOLUTIONS_DIR` variable at the top of the script.

Example - CMake project:
```bash
prepare-workspace --round 399 --codeforces
```
Result:
```bash
tree ~/algo_competitions/cf399
├── A
│   ├── CMakeLists.txt
│   ├── in1.txt
│   ├── in2.txt
│   ├── in3.txt
│   ├── ...
│   └── main.cpp
├── B
│   ├── CMakeLists.txt
│   ├── in1.txt
│   ├── in2.txt
│   ├── in3.txt
│   ├── ...
│   └── main.cpp
├── C
│   ├── ...
├── CMakeLists.txt
```

Example - CodeBlocks project:
```bash
prepare-workspace --round 399 --codeforces --codeblocks
```
Result:
```bash
tree ~/algo_competitions/cf399
├── A
│   ├── A.cbp
│   ├── in1.txt
│   ├── in2.txt
│   ├── in3.txt
│   ├── ...
│   └── main.cpp
├── B
│   ├── B.cbp
│   ├── in1.txt
│   ├── in2.txt
│   ├── in3.txt
│   ├── ...
│   └── main.cpp
├── C
...
```
I create the in*.txt files because it helps me with auto completion during the contest. Feel free to comment out the creation of those files.