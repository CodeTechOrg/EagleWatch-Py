import re
import setuptools

with open("eaglewatch/__init__.py", encoding="utf-8") as x:
    version = re.findall(r"__version__ = \"(.+)\"", x.read())[0]

with open("README.md", "r") as k:
    long_description = k.read()

setuptools.setup(
    name="eaglewatch",
    version=version,
    author="moezilla",
    author_email="pranavajay74@gmail.com",
    description="Eaglewatch Antispam Wrapper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CodeTechOrg/eaglewatch-py",    
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    install_requires=["requests"],
    packages=['eaglewatch'],
    python_requires=">=3.6",
)
