from setuptools import setup, find_packages

setup(
    name="usc-core",
    version="0.1.0",
    description="Universal Structured Container (USC) - Reference Implementation",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="USC Project",
    author_email="dev@example.com",
    url="https://github.com/yourusername/usc-core",
    packages=find_packages(),
    py_modules=["cli"],
    entry_points={
        "console_scripts": [
            "usc=cli:main",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Text Processing :: Markup",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.8",
)
