#!/usr/bin/env bash
GENERIC_SOLUTIONS_DIR=~/algo_competitions
SCRIPT_DIR="$(dirname "$(readlink -f "$0")")" #will follow symlink if it needs to
TEMPLATES_DIR=$SCRIPT_DIR/../../templates
PROJECT_TYPE="cmake"
TASK_NAMES=(A B C D E F G H) # TODO {A..H}
NUMBER_OF_INPUT_FILES_TO_CREATE=10

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
  echo "-cm, --cmake"
  printf "\tCreate CMake project (default).\n"
  echo "-cb, --codeblocks"
  printf "\tCreate CodeBlocks project.\n"
  echo "-h, --help"
  printf "\tdisplay this help and exit\n"
}

# TODO function handle_command_line_args
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
    TEMPLATE=codeforces_template.cpp
    ;;
    -tc|--topcoder)
    TYPE="tc"
    TEMPLATE=topcoder_template.cpp
    ;;
    -cm|--cmake)
    PROJECT_TYPE="cmake"
    ;;
    -cb|--codeblocks)
    PROJECT_TYPE="codeblocks"
    ;;
    -h|--help)
    print_help
    exit
    ;;
esac
shift
done


# TODO function validate_command_line_args
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

function create_project_structure {
    for task_name in ${TASK_NAMES[@]}
    do
      mkdir $GENERIC_SOLUTIONS_DIR/$NAME/$task_name
      cp $TEMPLATES_DIR/$TEMPLATE $GENERIC_SOLUTIONS_DIR/$NAME/$task_name/main.cpp
      for i in {1..10} # {1..$TODO NUMBER_OF_INPUT_FILES_TO_CREATE} or something like that
      do
        touch $GENERIC_SOLUTIONS_DIR/$NAME/$task_name/in$i.txt
      done
    done
}

function set_cmake_project {
    cp $SCRIPT_DIR/CMake/CMakeLists_all_solutions.txt $GENERIC_SOLUTIONS_DIR/$NAME/CMakeLists.txt
    for task_name in ${TASK_NAMES[@]}
    do
      local TASK_CMAKE_FILE_PATH="$GENERIC_SOLUTIONS_DIR/$NAME/$task_name/CMakeLists.txt"
      cp $SCRIPT_DIR/CMake/CMakeLists_solution.txt $TASK_CMAKE_FILE_PATH
      sed -i "s/PROJECT_NAME/$task_name/g" $TASK_CMAKE_FILE_PATH
      for i in {1..10}
      do
        touch $GENERIC_SOLUTIONS_DIR/$NAME/$task_name/in$i.txt
      done
    done
}

function set_code_blocks_project {
    for task_name in ${TASK_NAMES[@]}
    do
      cp $SCRIPT_DIR/CodeBlocks/CodeblocksProjectFile.cbp $GENERIC_SOLUTIONS_DIR/$NAME/$task_name/$task_name.cbp
      sed -i "s/MyProjectName/$task_name/g" $GENERIC_SOLUTIONS_DIR/$NAME/$task_name/$task_name.cbp
    done
}

create_project_structure
if [ "$PROJECT_TYPE" == "cmake" ]; then
    set_cmake_project
else
    set_code_blocks_project
fi
