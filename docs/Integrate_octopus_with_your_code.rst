Integrate Octopus with python code
=========================================

.. container:: cell markdown

   .. rubric:: (1) Install Octopus
      :name: 1-install-octopus

.. code-block:: console

      pip install git+https://github.com/UBC-NLP/octopus.git --q

.. container:: cell markdown

Initial octopus object
----------------------------
Import related packges 

.. code:: python

      import logging
      import os
      from octopus import octopus

Inital the logger and set ``cache_dir``

.. code:: python

      logging.basicConfig(
          format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
          datefmt="%Y-%m-%d %H:%M:%S",
          level=os.environ.get("LOGLEVEL", "INFO").upper(),
      )
      logger = logging.getLogger("octopus")
      cache_dir="./mycaoctopus_cacheche"

Create octopus object

.. code:: python

      oct_obj = octopus.octopus(logger, cache_dir)





Google Colab Link
-----------------

You can find the full examples on the Google Colab on the following link
https://colab.research.google.com/github/UBC-NLP/octopus/blob/main/examples/Integrate_octopus_with_your_code.ipynb
