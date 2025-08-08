from setuptools import setup, find_packages

setup(
    name='autoupgrader',
    version='0.1.0',
    author='HaZaRd',
    author_email='police123456789ilia@gmail.com',
    description='A library for automatic Python updates',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Pytholearn/autoupgrader',
    packages=find_packages(),
    install_requires=[
        'gitpython'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
