#!/usr/bin/env bash
GENERIC_SOLUTIONS_DIR=~/algo_competitions
SCRIPT_DIR="$(dirname "$(readlink -f "$0")")" #will follow symlink if need to

function print_help() {
  echo "This script creates Codeblocks projects that use my templates."
  echo "Usage: prepare_workspace.sh --round NUMBER --codeforces #or --topcoder instead"
  echo "Arguments:"
  echo "-r, --round"
  printf "\tround number\n"
  echo "-cf, --codeforces"
  printf "\tUse for codeforces rounds.\n"
  echo "-tc, --topcoder"
  printf "\tUse for topcoder rounds.\n"
  echo "-h, --help"
  printf "\tdisplay this help and exit\n"
}

while [[ $# -gt 0 ]]
do
key="$1"
case $key in
    -r|--round)
    ROUND="$2"
    shift
    ;;
    -cf|--codeforces)
    TYPE="cf"
    TEMPLATE="codeforces_template.cpp"
    ;;
    -tc|--topcoder)
    TYPE="tc"
    TEMPLATE="topcoder_template.cpp"
    ;;
    -h|--help)
    print_help
    exit
    ;;
esac
shift
done

if [ -z "$ROUND" ]
  then
    echo "ROUND not set"
    exit
else
  case $ROUND in
      ''|*[!0-9]*)
        echo "invalid round specified"
        exit
        ;;
  esac
fi

if [ -z "$TYPE" ]
  then
    echo "Round type not set - choose either topcoder or codeforces"
    exit
fi

NAME=$TYPE$ROUND
if [ -d $GENERIC_SOLUTIONS_DIR/$NAME/ ]; then
  echo "Directory $GENERIC_SOLUTIONS_DIR/$NAME/ already exists. ABORTING!"
  exit
fi
mkdir -p $GENERIC_SOLUTIONS_DIR/$NAME/
echo "$GENERIC_SOLUTIONS_DIR/$NAME/ created"


set -e

for task_name in {A..H}
do
  mkdir $GENERIC_SOLUTIONS_DIR/$NAME/$task_name
  cp $SCRIPT_DIR/$TEMPLATE $GENERIC_SOLUTIONS_DIR/$NAME/$task_name/main.cpp
  cp $SCRIPT_DIR/CodeblocksProjectFile.cbp $GENERIC_SOLUTIONS_DIR/$NAME/$task_name/$task_name.cbp
  sed -i "s/MyProjectName/$task_name/g" $GENERIC_SOLUTIONS_DIR/$NAME/$task_name/$task_name.cbp
  for i in {1..10}
  do
    touch $GENERIC_SOLUTIONS_DIR/$NAME/$task_name/in$i.txt
  done
done
