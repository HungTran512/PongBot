#!/usr/bin/env bash
# generated from catkin/cmake/templates/setup.bash.in

CATKIN_SHELL=bash

# source setup.sh from same directory as this file
_CATKIN_SETUP_DIR=$(builtin cd "`dirname "${BASH_SOURCE[0]}"`" > /dev/null && pwd)
. "$_CATKIN_SETUP_DIR/setup.sh"


# source lab3ws setup file
export ROS_MASTER_URI=http://localhost:11311
export ROS_HOSTNAME=localhost
source ~/lab3_ws/devel/setup.bash