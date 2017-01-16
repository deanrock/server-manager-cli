from setuptools import setup

setup(
    name="smcli",
    version="0.0.1",
    py_modules=["smcli.py"],
    install_requires=[
        "click==6.7",
        "requests==2.12.4",
        "robobrowser==0.5.3"
    ],

    entry_points="""
        [console_scripts]
        smcli=smcli:myCli
    """
)
