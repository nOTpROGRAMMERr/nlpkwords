from setuptools import setup, find_packages

setup(
    name='nlpkwords',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'nltk',
        'textblob',
        'scikit-learn',
    ],
    author='Rish Dias',
    author_email='rishrdias672004@gmail.com',
    description='A package containing AI/ML codes',
    include_package_data=True,
    python_requires='>=3.6',
)
