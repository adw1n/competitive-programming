from setuptools import setup

#https://packaging.python.org/tutorials/distributing-packages/#setup-args
setup(
    name='fetch_codeforces_examples',
    version='1.0.0',
    url='https://github.com/adw1n/competitive-programming/tools/fetch_codeforces_examples',
    license='Unlicense',
    install_requires=['typing', 'requests', 'lxml', 'aiohttp'],
    python_requires=">=3",
    py_modules=['fetch_cf_examples'],
    entry_points={
        'console_scripts': [
            'fetch-cf-examples=fetch_cf_examples:main',
        ],
    }
)