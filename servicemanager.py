# servicemanager.py

import sys
import subprocess
import os
import stat
import pwd
import grp


def is_running(service_name):
    cmd = '/bin/systemctl status %s.service' % service_name
    proc = subprocess.Popen(cmd, shell=True,stdout=subprocess.PIPE)
    stdout_list = proc.communicate()[0].split('\n')
    for line in stdout_list:
        if 'Active:' in line:
            if '(running)' in line:
                return True
    return False

def restart_service(service_name):
    cmd = '/bin/systemctl restart %s.service' % service_name
    proc = subprocess.Popen(cmd, shell=True,stdout=subprocess.PIPE)
    proc.communicate()

def enable_service(service_name):
    cmd = '/bin/systemctl enable %s.service' % service_name
    proc = subprocess.Popen(cmd, shell=True,stdout=subprocess.PIPE)
    proc.communicate()


def start_service(service_name):
     if not is_running(service_name):
            cmd = '/bin/systemctl start %s.service' % service_name
            proc = subprocess.Popen(cmd, shell=True,stdout=subprocess.PIPE)
            proc.communicate()
     else: 
            print(service_name + " is already running")

#start_service("apache2")
def set_file_content(file, content): 
       with open(file, 'w+') as f:
        f.write(content)

def set_file_content_metadata(file, content, user, group, mod):
    user = "root"
    group = "apache"
    '''
    w  write mode
    r  read mode
    a  append mode

    w+  create file if it doesn't exist and open it in (over)write mode
        [it overwrites the file if it already exists]
    r+  open an existing file in read+write mode
    a+  create file if it doesn't exist and open it in append mode
    '''
    set_file_content(file, content)
        
    uid = pwd.getpwnam("root").pw_uid
    gid = grp.getgrnam("root").gr_gid
    os.chown(file, uid, gid)


    os.chmod(file, mod)
    


    # st = os.stat(file)
    # os.chmod(file, st.st_mode | stat.S_IEXEC)
    
    
index_content = """<?php header("Content-Type: text/plain");echo "hello world\n";?>"""
set_file_content("/var/www/html/index.php", index_content)
htaccess_content = """DirectoryIndex index.php
                        Allow Override All"""
set_file_content_metadata("/var/www/html/index.php", htaccess_content, "root", "apache", 664)