from setuptools import find_packages, setup
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setup(
    name='PyWinda',
    packages=find_packages(),
    version='1.2.11',
    description='PyWinda provides an extensive range of tools for power and load analysis at a wind farm level.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='PyWinda Authors',
    author_email='',
    url="https://github.com/PyWinda/pywinda",
    project_urls={
        "Bug Tracker": "https://github.com/PyWinda/pywinda/issues",
    },
    license='MIT',
    install_requires=['pandas','numpy'],
        classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
#   setup_requires=['pytest-runner'], #Ignoring the recommended tests
#   tests_require=['pytest'], #Ignoring the recommended tests
#    test_suite='tests', #Ignoring the recommended tests
)