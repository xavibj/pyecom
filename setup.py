import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='pyecom',
    author='Xavi Bolivar',
    author_email='xavi@xavi.net',
    description='ecommerce api',
    keywords='ecommerce, api',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/xavibj/pyecom',
    project_urls={
        'Documentation': 'https://github.com/xavibj/pyecom',
        'Bug Reports': 'https://github.com/xavibj/pyecom/issues',
        'Source Code': 'https://github.com/xavibj/pyecom',
        # 'Funding': '',
        # 'Say Thanks!': '',
    },
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    classifiers=[
        # see https://pypi.org/classifiers/
        'Development Status :: 1 - Planning',

        'Intended Audience :: Developers',
        'Topic :: Internet',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=['fastapi>=0.6.3,<0.7', 'uvicorn>=0.13.4,<0.14', 'mysql-connector-python>=8.0.0,<9','pyyaml>=5.4.1,<6'],
    extras_require={
        'dev': ['check-manifest'],
        # 'test': ['coverage'],
    },
    # entry_points={
    #     'console_scripts': [  # This can provide executable scripts
    #         'run=examplepy:main',
    # You can execute `run` in bash to run `main()` in src/examplepy/__init__.py
    #     ],
    # },
)
