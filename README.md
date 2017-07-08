[fetch-codeforces-examples](tools/fetch_codeforces_examples) - neat script for downloading all examples (input, expected output pairs) for each problem in a codeforces contest. 

[prepare-workspace](tools/prepare_workspace) - script that automates creation of CMake (e.g. CLion IDE)/CodeBlocks C++ projects with my [templates](templates). Useful for competitions, since for each competition you probably want to create 5++ projects/solution directories. 

[check-correctness](tools/check_correctness) - script that compiles solution to the problem in current working directory with appropriate flags and then runs tests on it (using another tool [checker](https://github.com/akrasuski1/checker)). Number of passed and failed tests is displayed in a summary at the end.

[templates](templates/) - the templates that I use during [topcoder SRM](https://topcoder.com) and [codeforces](http://codeforces.com) contests that speed up the process of writing solutions.

[Random stuff](random_stuff/) - stuff that I couldn't be bothered to properly name / describe (probably of no use to you).

All tools in the [tools](tools/) directory are licensed under [WTFPL v2](tools/LICENSE.txt). 
The rest of the stuff probably doesn't even need a license.