# Voltair ( your Configurations Poet)

<!--- These are examples. See https://shields.io for others or to customize this set of shields. You might want to include dependencies, project status and licence info here --->
![GitHub repo size](https://img.shields.io/github/repo-size/scottydocs/README-template.md)
![GitHub contributors](https://img.shields.io/github/contributors/scottydocs/README-template.md)l)

Project name is a `Voltair that allows `ops admins` to do 
- install and remove pakages from any debian/ubuntu server, which can also be added to the config file
- start and restart a service list of services can be added into config or used inside a playbook
- Create files and assign mode, user and grouo
- includes and run bootstrap what all needed to run this program
- playbook for a sample Apache webserver is provided



## Run Voltaire

to run it you need to exceute 
```
sudo ./orchestrator.py deploy
```




### File Struture

    .
    ├── apps-to-install                   # list of packages that needed to be installed config file
    ├── apps-to-remove                    # list of packages that needed to be removed config file
    ├── appsinstaller.py                  # The model that handles installing and removing the packages
    ├── bootstrap.sh                      # A file to install python requirements and build packages on host to run this program
    ├── orchestrator.py                   #  this is the orschestator that handle sshing into the remote host and run the bootstrap and playbook also does clean       |                                     #  up and varios extra tasks
    ├── playbook.py                       # A playbook to bootstrap an Apache server
    ├── servicemanager.py                 # Handles services managmenet and file managment
    ├── services                          # List of services can be used as config for services to be started or restarted
    └── README.md





