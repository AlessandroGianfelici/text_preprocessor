from setuptools import setup, find_packages

setup(name='text_preprocessor',
      version='0.1.0',
      description='Utilities for text preprocessing',
      url='https://github.com/AlessandroGianfelici/text_preprocessor',
      author='Alessandro Gianfelici',
      author_email='alessandro.gianfelici@hotmail.com',
      license='MIT',
      packages=find_packages(),
      include_package_data=True,
      install_requires=[
          'langdetect',
          'spacy', 
          'textblob', 
          'pandas', 
          'nltk'
      ],
      zip_safe=False)