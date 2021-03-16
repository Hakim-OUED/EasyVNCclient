try:
    import setuptools
except ImportError:
    from distutils.core import setup

setuptools.setup(
    #nom de l'application
    name="EasyVNC",

    version="1.0.0",

    author="Hakim OUEDRAOGO& Andri RAMAROSON",
    author_email="contact@easy.com",

    #Packages
    packages = setuptools.find_packages(),


    include_package_data=True,

    #Details
    url="http://esaygroupe.net",


    license="LICENSE.txt",

    description="Programme de gestion déquipement à travers un réseau privé .",

    #long_description=open("README.txt").read(),

    #Dependent packages (distributions)
    install_requires=[
        "pyqt5",
    ],
)