if __import__("os").name == "nt":
    raise RuntimeError(
        "check50 does not support Windows directly. Instead, you should install the Windows Subsystem for Linux (https://docs.microsoft.com/en-us/windows/wsl/install-win10) and then install check50 within that."
    )

from setuptools import setup

setup(
    author="Ben Carpenter",
    author_email="bacarpenter04@gmail.ocm",
    classifiers=[
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
        "Topic :: Education",
        "Topic :: Utilities",
    ],
    description="This is check501, built on top of check50 (https://github.com/cs50/check50)",
    license="GPLv3",
    message_extractors={
        "check50": [
            ("**.py", "python", None),
        ],
    },
    install_requires=[
        "attrs>=18",
        "beautifulsoup4>=0",
        "pexpect>=4.6",
        "lib50>=2,<4",
        "pyyaml>=3.10",
        "requests>=2.19",
        "termcolor>=1.1",
        "jinja2>=2.10",
    ],
    extras_require={"develop": ["sphinx", "sphinx-autobuild", "sphinx_rtd_theme"]},
    keywords=["check", "check51"],
    name="check51",
    packages=["check50", "check50.renderer"],
    python_requires=">= 3.6",
    entry_points={"console_scripts": ["check51=check50.__main__:main"]},
    url="https://github.com/bacarpenter/check51",
    version="3.2.0",
    include_package_data=True,
)
