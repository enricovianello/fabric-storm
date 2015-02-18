#!/usr/bin/env python
from fabric.api import * 

def uptime():
  local('uptime')

def yum_clean():
  sudo('yum clean all')

def yum_update_all():
  sudo('yum update -y')

def update_storm_webdav():
  sudo('yum -y update storm-webdav')

def update_storm_gridhttps():
  sudo('yum -y update storm-gridhttps-server')

def restart_storm_webdav():
  sudo('service storm-webdav restart')

def restart_storm_gridhttps():
  sudo('service storm-gridhttps-server restart')

def update_storm_frontend():
  sudo('yum -y update storm-frontend-server')

def reinstall_storm_frontend():
  sudo('yum -y reinstall storm-frontend-server')

def restart_fe():
  sudo('service storm-frontend-server restart')

def update_storm_backend():
  sudo('yum -y update storm-backend-server')

def restart_be():
  sudo('service storm-backend-server restart')

def configure_tr_node():
  sudo('/opt/glite/yaim/bin/yaim -c -s /etc/storm/siteinfo/storm.def -n se_storm_gridftp -n se_storm_webdav -n se_storm_gridhttps')

def configure_fe_node():
  sudo('/opt/glite/yaim/bin/yaim -c -s /etc/storm/siteinfo/storm.def -n se_storm_frontend')

def configure_be_node():
  sudo('/opt/glite/yaim/bin/yaim -c -s /etc/storm/siteinfo/storm.def -n se_storm_backend')

def configure_storm_node():
  sudo('/opt/glite/yaim/bin/yaim -c -s /etc/storm/siteinfo/storm.def -n se_storm_backend -n se_storm_frontend -n se_storm_gridftp -n se_storm_webdav -n se_storm_gridhttps')

def update_tr_node():
  yum_clean()
  update_storm_webdav()
  restart_storm_webdav()
  update_storm_gridhttps()
  restart_storm_gridhttps()

def update_and_configure_tr_node():
  yum_clean()
  update_storm_webdav()
  update_storm_gridhttps()
  configure_tr_node()

def update_fe_node():
  yum_clean()
  update_storm_frontend()
  restart_fe()

def reinstall_fe_node():
  yum_clean()
  reinstall_storm_frontend()
  restart_fe()

def update_and_configure_fe_node():
  yum_clean()
  update_storm_frontend()
  configure_fe_node()

def reinstall_and_configure_fe_node():
  yum_clean()
  reinstall_storm_frontend()
  configure_fe_node()

def update_be_node():
  yum_clean()
  update_storm_backend()
  restart_be()

def update_and_configure_be_node():
  yum_clean()
  update_storm_backend()
  configure_be_node()

def update_and_configure_storm_node():
  yum_clean()
  yum_update_all()
  reinstall_storm_frontend()
  configure_storm_node() 
