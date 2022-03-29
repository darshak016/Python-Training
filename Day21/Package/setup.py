from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='dk_calc',
    version='1.0.0',
    description="This is python project",
    long_description=long_description,
    author='DARSHAK KAKANI',
    author_email="dk@gmail.com",
    keywords='sample,setuptools,development',
    packages=find_packages(where='dk_calc'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    python_requires='>=3.6, <4',
    entry_points={  # Optional
        'console_scripts': [
            'dk_calc=dk_calc:main',
        ],
    },
)
