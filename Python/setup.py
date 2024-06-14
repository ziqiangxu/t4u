import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='t4u',
    version='0.1.0',
    author='Daryl.Xu',
    author_email='ziqiang_xu@qq.com',
    description='Tools for you',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ziqiangxu/t4u',
    packages=setuptools.find_packages(),
    package_dir={'': '.'},
    install_requires=[],
    entry_points={},
    classifiers=(
        'Programming Language :: Python :: 3.6',
        'Operating System :: OS Independent',
    ),
)
