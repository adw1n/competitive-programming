My IDE of choice for algorithm competitions is Codeblocks 16. I use the [prepare_workspace.sh](prepare_workspace.sh) script to automate creation of projects that use my [templates](../../templates/).

prepare-workspace script install:
```bash
git clone https://github.com/adw1n/competitive-programming ~/bin/competitive-programming/
sudo ln -s ~/bin/competitive-programming/tools/prepare_workspace/prepare_workspace.sh /usr/local/bin/prepare-workspace
```

prepare-workspace script usage:
```bash
prepare-workspace --round 399 --codeforces
prepare-workspace --round 273 --topcoder
prepare-workspace --help
```

Example:
```bash
prepare-workspace --round 399 --codeforces
```
Result:
```bash
tree ~/algo_competitions/cf399
├── A
│   ├── A.cbp
│   ├── in10.txt
│   ├── in1.txt
│   ├── in2.txt
│   ├── in3.txt
│   ├── in4.txt
│   ├── in5.txt
│   ├── in6.txt
│   ├── in7.txt
│   ├── in8.txt
│   ├── in9.txt
│   └── main.cpp
├── B
│   ├── B.cbp
│   ├── in10.txt
│   ├── in1.txt
│   ├── in2.txt
│   ├── in3.txt
│   ├── in4.txt
│   ├── in5.txt
│   ├── in6.txt
│   ├── in7.txt
│   ├── in8.txt
│   ├── in9.txt
│   └── main.cpp
├── C
...
```
I create the in*.txt files because it helps me with auto completion during the contest. Feel free to comment out the creation of those files.