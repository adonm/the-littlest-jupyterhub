"""
Simplest plugin that exercises all the hooks defined in tljh/hooks.py.
"""

from tljh.hooks import hookimpl


@hookimpl
def tljh_extra_user_conda_packages():
    # tqdm installs from the conda-forge channel (https://conda-forge.org/packages/)
    # csvtk installs from the bioconda channel (https://bioconda.github.io/conda-package_index.html)
    return ["tqdm", "csvtk"]


@hookimpl
def tljh_extra_user_conda_channels():
    return ["conda-forge", "bioconda"]


@hookimpl
def tljh_extra_user_pip_packages():
    return ["simplejson"]


@hookimpl
def tljh_extra_hub_pip_packages():
    return ["there"]


@hookimpl
def tljh_extra_apt_packages():
    return ["sl"]


@hookimpl
def tljh_custom_jupyterhub_config(c):
    c.Test.jupyterhub_config_set_by_simplest_plugin = True


@hookimpl
def tljh_config_post_install(config):
    config["Test"] = {"tljh_config_set_by_simplest_plugin": True}


@hookimpl
def tljh_post_install():
    with open("test_tljh_post_install", "w") as f:
        f.write("file_written_by_simplest_plugin")


@hookimpl
def tljh_new_user_create(username):
    with open("test_new_user_create", "w") as f:
        f.write("file_written_by_simplest_plugin")
        f.write(username)
