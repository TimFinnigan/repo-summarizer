from setuptools import setup, find_packages

setup(
    name="tree-cli",
    version="1.0.0",
    description="A CLI tool to generate and copy directory trees to the clipboard",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),
    install_requires=[
    ],
    entry_points={
        "console_scripts": [
            "tree-cli=tree_cli.cli:main",  # `tree-cli` is the CLI command
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
