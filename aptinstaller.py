# aptinstaller.py

import apt
import sys

######## packages managment

def santisize_string(pkg_name): 
    pkg_name = pkg_name.strip().strip('\n')
    return pkg_name
def get_cache(): 
    cache = apt.cache.Cache()
    cache.update()
    cache.open()
    return cache

def install_package(pkg_name): 
        
    cache = get_cache()

    pkg = cache[pkg_name]
    if pkg.is_installed:
        print ( pkg_name + " already installed")
    else:
        pkg.mark_install()

        try:
            cache.commit()
            cache.close()
        except Exception:
            print ("Sorry, package installation failed")

def remove_package(pkg_name): 
        
    cache = get_cache()

    pkg = cache[pkg_name]
    if pkg.is_installed:
        pkg.mark_delete(True, purge=True)

        try:
            cache.commit()
            cache.close()
        except Exception:
            print ("Sorry, package installation failed")


def install_packages_from_config_file(): 
    cache = get_cache()
    with open("/tmp/apps-to-install") as input:
        for pkg_name in input:
            pkg_name = santisize_string(pkg_name)
            if pkg_name: 
                print("p: " + pkg_name)
                install_package(pkg_name)
    input.close()

def remove_packages_from_config_file(): 
    cache = get_cache()
    with open("apps-to-remove") as input:
        for pkg_name in input:
            pkg_name = santisize_string(pkg_name)
            if pkg_name: 
                remove_package(pkg_name)
    input.close()

install_packages_from_config_file()

#remove_packages_from_config_file()
