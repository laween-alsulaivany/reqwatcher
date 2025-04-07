from setuptools import setup

setup(
    name="reqwatcher",
    version="0.1",
    py_modules=["reqwatcher"],
    entry_points={
        "console_scripts": [
            "reqwatcher=reqwatcher:main",
        ],
    },
    install_requires=[],
)
