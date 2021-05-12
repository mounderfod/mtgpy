import setuptools

setuptools.setup(
    name="mtg",
    version="1.0",
    author="mounderfod",
    description="Looks up Magic: The Gathering cards and returns info about them.",
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': [
            'mtg = mtg.mtg:main'
        ]
    },
    classifiers=[ 
        'Programming Language :: Python :: 3', 
        'License :: OSI Approved :: MIT License', 
        'Operating System :: OS Independent', 
    ], 
)