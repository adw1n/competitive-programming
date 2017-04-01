This script relies on the [checker](https://github.com/akrasuski1/checker) tool - assumes that `checker` command is systemwide available (if you want to name it differently or use using full path change the second line of the script). For install steps of that tool go to it's webpage.

Install:
```bash
git clone https://github.com/adw1n/competitive-programming ~/bin/competitive-programming/
sudo ln -s ~/bin/competitive-programming/tools/check_correctness/check_correctness.sh /usr/local/bin/check-correctness
```

Usage:
```bash
cd ~/algo_competitions/cf407/A #wherever you store your solution source code
check-correctness #assumes your source file is named main.cpp
```
Output:
```bash
Testing in1.txt:
Time: 0.00s
Memory: 3204kB
Correct

Testing in2.txt:
Time: 0.00s
Memory: 3188kB
Correct

Statistics:
========================
2 x Correct
0 x Wrong Answer
0 x Time Limit Exceeded
========================
```