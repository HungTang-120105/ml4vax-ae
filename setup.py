from setuptools import setup, find_packages
from os import path

# Phiên bản package
__version__ = '0.1.0'

# Thư mục hiện tại
here = path.abspath(path.dirname(__file__))

# Đọc nội dung README.md nếu có
try:
    with open(path.join(here, 'README.md'), encoding='UTF-16 LE') as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = ''

# Đọc requirements.txt
with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().splitlines()

install_requires = [x.strip() for x in all_reqs if x and not x.startswith('#') and 'git+' not in x]
dependency_links = [x.strip().replace('git+', '') for x in all_reqs if x.startswith('git+')]

setup(
    name='vaxae_predictor',
    version=__version__,
    description='ML project to predict adverse events after mRNA-based COVID-19 vaccination',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Hưng Tăng',
    author_email='hung.ttm230037@sis.hust.edu.vn',
    url='https://github.com/HungTang-120105/ml4vax-ae',
    license='MIT',
    packages=find_packages(exclude=["tests*", "notebooks*"]),
    include_package_data=True,
    install_requires=install_requires,
    dependency_links=dependency_links,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Scientific/Engineering :: Artificial Intelligence'
    ],
    python_requires='>=3.8',
)
