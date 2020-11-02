import setuptools

# with open('requirements.txt') as f:
#     requirements = f.read().splitlines()
# with open('requirements_test.txt') as f:
#     test_requirements = f.read().splitlines()
with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    # Meta
    author='Steven Englehardt',
    description='Library for parsing ABP filter lists',
    long_description=long_description,
    long_description_content_type="text/markdown",
    name='abp-blocklist-parser',
    license='GPL v3',
    url='https://github.com/englehardt/abp-blocklist-parser',
    version='0.3',
    packages=['abp_blocklist_parser'],

    # Dependencies
    # install_requires=requirements,
    # tests_require=test_requirements,
    # setup_requires=['setuptools_scm', 'pytest-runner'],

    # Packaging
    include_package_data=True,
    use_scm_version=False,
    zip_safe=False,

    # Classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Scientific/Engineering :: Information Analysis'
    ],
)
