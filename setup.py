from octopus.copyright import *
from setuptools import setup, find_packages

with open("README.rst", "r") as readme_file:
    readme = readme_file.read()

from setuptools import setup

setup(name='octopus',
      version=version,
      description=description,
      long_description=readme,
      url='https://github.com/UBC-NLP/octopus',
      author=author,
      author_email=email,
      license=license,
      packages=find_packages(),
      install_requires=[
          'regex',
          'torch',
          'protobuf',
          'sentencepiece',
          'transformers',
          'psutil',
          'pandas',
          'tqdm',
          'sacrebleu',
          'accelerate',
          'datasets'
        ],
      entry_points={
            "console_scripts": [
                "octopus_translate = octopus_cli.translate:translate_cli",
                "octopus_score = octopus_cli.score:score_cli",
                "octopus_interactive = octopus_cli.interactive:interactive_cli",
            ],
        },
      
      )
