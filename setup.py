#
import os, re, setuptools
from proxypay import __version__ as VERSION

# Long Description
with open("README.md", "r") as readme_file:
    readme = readme_file.read()

setuptools.setup(
    name="django-proxypay",
    version=VERSION,
    description=(
        "Django Proxypay is a django library to interact with the proxypay in a simple way."
        "Useful for generating referrals and processing payments"
    ),
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Ageu Matheus",
    author_email="ageumatheus1@gmail.com",
    maintainer="Ageu Matheus",
    maintainer_email="ageumatheus1@gmail.com",
    url="https://github.com/AgeuMatheus/django-proxypay",
    project_urls={
        "Changelog": (
            "https://github.com/AgeuMatheus/django-proxypay"
            + "/blob/master/HISTORY.md"
        )
    },
    packages=setuptools.find_packages(),
    license="MIT License",
    keywords=["django", "payments", "proxypay" ],
    install_requires=["Django>=2"],
    python_requires=">=3.6",
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)