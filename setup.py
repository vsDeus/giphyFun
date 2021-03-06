from setuptools import setup, find_packages

with open("README.md") as fh:
    readme_description = fh.read()

setup(
    name             = 'giphyfun',
    version          = '0.2',
    description      = 'Command line program that play random giphy.',
    url              = 'https://github.com/vsDeus/giphyFun',
    download_url     = 'https://github.com/vsDeus/giphyFun/archive/0.1.tar.gz',
    author           = 'Goia Ciprian',
    author_email     = 'goia.ciprian14@gamil.com',
    long_description =  readme_description,
    long_description_content_type = "text/markdown",
    keywords         = ['giphy', 'terminal', 'giphyfun'],
    packages         = find_packages(),
    install_requires = ['opencv-python', 'appdirs', 'clipboard'],
    entry_points     = {
        'console_scripts': [
            'giphyfun=giphyFun.giphyFun:main',
        ],
    },
    classifiers      = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ]
)