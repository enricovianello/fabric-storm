#!/bin/bash

fab -f fabfile.py -H storm-be update_and_configure_be_node
fab -f fabfile.py -H storm-fe-1,storm-fe-2 reinstall_and_configure_fe_node
fab -f fabfile.py -H storm-tr-1,storm-tr-2 update_and_configure_tr_node
