#!/bin/bash

HOSTNAME=$1

fab -f fabfile.py -H $HOSTNAME update_and_configure_storm_node
