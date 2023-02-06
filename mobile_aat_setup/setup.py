# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/02_setup.ipynb.

# %% auto 0
__all__ = ['MOBILE_AAT_URL', 'download_aat_package', 'get_middle_of_package_name', 'swap_google_services', 'setup_aat']

# %% ../nbs/02_setup.ipynb 4
from git.repo.base import Repo
from .change_id import change_package_name
import os
import shutil
import json 

# %% ../nbs/02_setup.ipynb 5
MOBILE_AAT_URL = "https://github.com/hgzech/mobile_aat"

# %% ../nbs/02_setup.ipynb 7
def download_aat_package(path_to_save):
    Repo.clone_from(MOBILE_AAT_URL, path_to_save)

# %% ../nbs/02_setup.ipynb 10
def get_middle_of_package_name(path_to_google_services):
    with open(path_to_google_services, 'r') as f:
        app_info = json.load(f)
    package_name = app_info\
          ['client'][0]['client_info']['android_client_info']['package_name']
    middle_of_package_name = package_name.split('.')[1]
    return middle_of_package_name

# %% ../nbs/02_setup.ipynb 13
def swap_google_services(path_to_mobile_aat, path_to_google_services):
    path_to_old_google_services = os.path.join(path_to_mobile_aat, 'app', 'google-services.json')
    shutil.move(path_to_google_services, path_to_old_google_services)
    

# %% ../nbs/02_setup.ipynb 15
def setup_aat(path_to_save_to,path_to_google_services):
    download_aat_package(path_to_save_to)
    middle_of_package_name = get_middle_of_package_name(path_to_google_services)
    change_package_name(path_to_save_to, middle_of_package_name)
    swap_google_services(path_to_save_to, path_to_google_services)
