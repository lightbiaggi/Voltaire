# playbook.py
from aptinstaller import install_packages_from_config_file
from servicemanager import *
def webapp_playbook():
    print("################## Web-app Playbook ################################################################################") 
    # step 1 : install apache2 package 
    print("################## step 1 : install apache2 package #################################################################") 
    install_packages_from_config_file()
    # step 2 : check if apache2 process is started if no start the service
    print("################## step 2 : check if apache2 process is started/enabled if no start/enable the service ##############")
    start_service("apache2")
    enable_service("apache2")
    # step 3 : change the root page to index.php and add .htacceess
    print("################## step 3 : add index.php and .htaccess and set mode and owner ######################################") 
    #index File
    index_content = """<?php header("Content-Type: text/plain");echo "hello world\n";?>"""
    set_file_content_metadata("/var/www/html/index.php", index_content, "root", "apache", 775)
    # .htaccess with correct perms
    htaccess_content = "DirectoryIndex index.php"
    set_file_content_metadata("/var/www/html/.htaccess", htaccess_content, "root", "apache", 775)

webapp_playbook()
