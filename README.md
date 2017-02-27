#### prepare-workspace script
My IDE of choice for algorithm competitions is Codeblocks 16. I use the [prepare_workspace.sh](prepare_workspace.sh) script to automate creation of projects with my templates that I later use during competitions.

prepare-workspace script install:
```bash
git clone https://github.com/adw1n/competitive-programming ~/bin/competitive-programming/
sudo ln -s ~/bin/competitive-programming/prepare_workspace.sh /usr/local/bin/prepare-workspace
```

prepare-workspace script usage:
```bash
prepare-workspace --round 399 --codeforces
prepare-workspace --round 273 --topcoder
prepare-workspace --help
```

#### fetch-cf-examples (fetching codeforces input & output for each problem)
Another tool that I use is the [fetch_cf_examples.sh](fetch_cf_examples.py) script that downloads examples (testcases - pairs of input & output for each problem) from [codeforces](http://codeforces.com) contests.

fetch_cf_examples.sh install:
```bash
sudo ln -s ~/bin/competitive-programming/prepare_workspace.sh /usr/local/bin/fetch-cf-examples
#python3 required
#if your default python3 verison is older than 3.5 you will need to install typing module
#sudo pip3 install typing
```
fetch-cf-examples usage:
```bash
fetch-cf-examples --help
fetch-cf-examples --demo --link http://codeforces.com/contest/777 #will save to /tmp/codeforces
```
real usage:
```bash
#examples saved to ~/algo_competitions/cf404/A/... ~/algo_competitions/cf404/B/...
#after 3 seconds all examples are downloaded - much faster than copy pasting by hand
fetch-cf-examples -l http://codeforces.com/contest/777 -n cf404
```
PROGRAM OUTPUT:
```bash
Downloading examples from: http://codeforces.com/contest/777 to /home/username/algo_competitions/cf404
```
Providing explicitly directory to save to:
```bash
#examples saved to /tmp/yolo
fetch-cf-examples --link http://codeforces.com/contest/777 --contest-dir /tmp/yolo
```
I'm also working on making it able to not specify a contest - fetch-cf-examples will use the current contest that you are participating in.


[stl_cheat_sheet](stl_cheat_sheet) and [additional_algorithms](additional_algorithms) is what I have printed out and sometimes take to offline competitions.

#### Links - my online profiles
topcoder handle: [adwin_](https://www.topcoder.com/members/adwin_/details/?track=DATA_SCIENCE&subTrack=SRM)

codeforces handle: [adwin_](http://codeforces.com/profile/adwin_)

spoj handle (I'm not active there anymore): [adwin_](http://www.spoj.com/users/adwin_/)

polish spoj (I'm not active there anymore): [adwin_](http://pl.spoj.com/users/adwin_/)