# Voltair (Your Configurations Poet)

<!--- These are examples. See https://shields.io for others or to customize this set of shields. You might want to include dependencies, project status and licence info here --->
![GitHub repo size](https://img.shields.io/github/repo-size/scottydocs/README-template.md)
![GitHub contributors](https://img.shields.io/github/contributors/scottydocs/README-template.md))

Project name is a `Voltair that allows `ops admins` to do 
- Install and remove pakages from any debian/ubuntu server, which can also be added to the config file
- Start and restart a service list of services can be added into config or used inside a playbook
- Create files and assign mode, user and group
- Includes and run bootstrap what all needed to run this program
- Playbook for a sample Apache webserver is provided


## Prequisities
you need to have python3 and install requirments.txt
```
pip3 install -r requirments.txt
```

## Run Voltaire

to run it you need to exceute ( you need to provide ip username and password inside script
```
sudo ./orchestrator.py deploy
```




### File Struture

    .
    ├── apps-to-install                   # list of packages that needed to be installed config file
    ├── apps-to-remove                    # list of packages that needed to be removed config file
    ├── appsinstaller.py                  # The model that handles installing and removing the packages
    ├── bootstrap.sh                      # A file to install python requirements and build packages on host to run this program
    ├── orchestrator.py                   # this is the orschestator that handle sshing into the remote host and run the bootstrap and playbook also does clean       |                                     #  up and varios extra tasks
    ├── playbook.py                       # A playbook to bootstrap an Apache server
    ├── servicemanager.py                 # Handles services managmenet and file managment
    ├── services                          # List of services can be used as config for services to be started or restarted
    └── README.md


### Playbook output

playbook output example

![playbook output](https://github.com/lightbiaggi/Voltaire/blob/main/img/playbook.png?raw=true)

### Apache server cur output

here are the curls

![server1](https://github.com/lightbiaggi/Voltaire/blob/main/img/server1.png?raw=true)

![server2](https://github.com/lightbiaggi/Voltaire/blob/main/img/server2.png?raw=true)


### Future implementation and nice to add
- Get server info and authentication from pass managment like vault or PASS store
- Manage different linux distrubution such REHL 
- Create lookup mechanisim to identify services based on the packages install automatically without put it on config or playbook


