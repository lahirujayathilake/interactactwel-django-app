import distutils
import os
import subprocess

import setuptools
from setuptools.command.develop import develop
from setuptools.command.install import install

def build_js():
    subprocess.check_call(["npm", "install"], cwd=os.path.join(os.getcwd(), "interactwel"))
    subprocess.check_call(["npm", "run", "build"], cwd=os.path.join(os.getcwd(), "interactwel"))

# Build JS code when this package is installed in virtual env
# https://stackoverflow.com/a/36902139
class BuildJSDevelopCommand(develop):
    def run(self):
        self.announce("Building JS code", level=distutils.log.INFO)
        build_js()
        super().run()

class BuildJSInstallCommand(install):
    def run(self):
        self.announce("Building JS code", level=distutils.log.INFO)
        build_js()
        super().run()

setuptools.setup(
    name="interactwel-django-app",
    version="0.0.1",
    description="InterACTWEL plugin to Airavata Django Portal",
    packages=setuptools.find_packages(),
    install_requires=[
        'django>=1.11.16',
        'django-filter>=2.1.0, <3.0',
        'markdown',
        'jsonfield',
    ],
    entry_points="""
[airavata.djangoapp]
interactwel = interactwel.apps:InteractwelAppConfig
""",
    cmdclass={
        'develop': BuildJSDevelopCommand,
        'install': BuildJSInstallCommand,
    }
)
