#!/usr/bin/env python
# orchestrator.py

import sys
import os

def main():
    print ("privide deploy as input") 
    
def load_scripts(client): 
    sftp = client.open_sftp()
    #init script to install needed libraries
    sftp.put("bootstrap.sh", '/tmp/bootstrap.sh')
    sftp.put("playbook.py", '/tmp/playbook.py')
    sftp.put("aptinstaller.py", '/tmp/aptinstaller.py')
    sftp.put("servicemanager.py", '/tmp/servicemanager.py')
    sftp.put("apps-to-install", '/tmp/apps-to-install')
    sftp.close()
    print ("scripts loaded")       

if __name__ == '__main__':
    try:
        if sys.argv[1] == 'deploy':
            import paramiko

            # Connect to remote host
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            client.connect('54.242.49.198', username='root', password='2VATSIIYPXWLL2C2WYAY3HZP')
            
            # 1- load the needed scripts
            load_scripts(client)
            
            # 2- run the init script to install needed dependecies for this program
            #make the bootstrap scrip executable
            stdin, stdout, stderr = client.exec_command("chmod +x /tmp/bootstrap.sh")
            print(stdout.read().decode())
            
            # # Run the bootstrap script( i ended run it manuanlly then contunie process for some reason that module has timeout and build and all take time but it works)
            stdin, stdout, stderr = client.exec_command('/tmp/bootstrap.sh')
            print("stderr: ", stderr.readlines())
            print("stdout: ", stdout.readlines())
            
            # 3 - run the playbook
            istdin, stdout, stderr  = client.exec_command('python /tmp/playbook.py')
            print("stderr: ", stderr.readlines())
            print("stdout: ", stdout.readlines())
            
            
            # 4 - change the apache.conf to use .htaccess
            istdin, stdout, stderr  = client.exec_command("sed '/<Directory \/var\/www\/>/,/<\/Directory>/ s/AllowOverride None/AllowOverride all/' /etc/apache2/apache2.conf > /etc/apache2/apache2.conf")
            print("stderr: ", stderr.readlines())
            print("stdout: ", stdout.readlines())
            
            # 5 - restart the service
            stdin, stdout, stderr = client.exec_command('systemctl restart apache2')
            print("stderr: ", stderr.readlines())
            print("stdout: ", stdout.readlines())
            
            # 6 - cleanup
            stdin, stdout, stderr = client.exec_command("rm /tmp/*")
            print("stderr: ", stderr.readlines())
            print("stdout: ", stdout.readlines())
            client.close()
            sys.exit(0)
            
    except IndexError:
        pass

    main()