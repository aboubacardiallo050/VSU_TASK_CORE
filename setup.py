import os

from setuptools import setup, find_packages

import vsu_task_core

# команды для создания установочного дистрибутива (тек. директория - проект, результат см. в ./dist):
# 1) python setup.py sdist [--dist-dir=<...>]
# или
# 2) python setup.py bdist_wheel [--dist-dir=<...>] [--plat-name=<...>]

build_version = os.environ.get("build_version", vsu_task_core.__version__)
platform = os.environ.get("platform", "any")


def get_long_description() -> str:
    with open("README.txt", encoding="UTF-8") as file:
        result = file.read()
    return result


def install_requires():
    with open("requirements.txt") as file:
        requirements = file.read().splitlines()
    return requirements


setup(
    name="vsu_task_core",
    maintainer="VSU",
    maintainer_email="support@vsu.com",
    version=build_version,
    description='vsu_task_core - AI-модуль',
    long_description=get_long_description(),
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires(),
    python_requires=">=3.9",
    options={"bdist_wheel": {"plat_name": platform}}
)
