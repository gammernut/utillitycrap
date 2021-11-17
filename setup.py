import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='utillity_crap',
    version='0.0.1',
    author='Jacob A Henson',
    author_email='gammernut@aol.com',
    description='Testing installation of Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/mike-huls/toolbox',  # my git hub url goes here
    project_urls=None,
    license='MIT',
    packages=['utillity_crap'],
    install_requires=None,
)
