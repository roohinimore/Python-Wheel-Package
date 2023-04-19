import setuptools

setuptools.setup(
    name="myPackage",
    version="0.0.1",
    author="Rohini",
    author_email="test@test.com",
    description="Package to create",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
