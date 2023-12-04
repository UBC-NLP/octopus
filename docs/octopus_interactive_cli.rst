Interactive Command Line
=====================
   -  Octopus interactive cli ``octopus_interactive`` support only beam search with the following default setting:

      -  ``-s`` or ``--seq_length``: The maximum sequence length value, (``default value is 300``)
      -  ``-o`` or ``--max_outputs``: The maximum of the output tanslations (``default value is 1``)
      -  ``-b`` or ``--num_beams NUM_BEAMS``: Number of beams (``default value is 1``)
      -  ``-n`` or ``--no_repeat_ngram_size``: Number of n-gram that doesn't appears twice (``default value is 2``)

   -  ``octopus_interactive`` command asks you you to input translate your input text. Moreover, you can write q to exsit as shown in the following image.



Usage and Arguments
-------------------
.. code-block:: console

      octopus_interactive -h

.. code-block:: console
         usage: octopus_interactive [-h] [-c CACHE_DIR]

         Octopus Interactive CLI

         optional arguments:
           -h, --help            show this help message and exit
           -c CACHE_DIR, --cache_dir CACHE_DIR
                                 The cache directory path, default value is
                                 octopus_cache directory

(2) Octopus Interactive
---------------------------
      :name: 2-octopus-interactive

.. code-block:: console

      !octopus_interactive

.. code-block:: console

            2023-12-04 02:53:29 | INFO | octopus.interactive_cli | Namespace(cache_dir='./octopus_cache')
            2023-12-04 02:53:29 | INFO | octopus.interactive_cli | Loading model from UBC-NLP/octopus
            2023-12-04 02:53:34 | INFO | octopus.interactive_cli | Run the model with CPU
            2023-12-04 02:53:34 | INFO | octopus.interactive_cli | Loading tasks
            --------------------------------------------------
            OCTOPUS's tasks:
            --------------------------------------------------
            Prefix: [diacritize] Task Name: Diartization
            Prefix: [correct_grammar] Task Name: Grammatical Error Correction
            Prefix: [paraphrase] Task Name: Paraphrase
            Prefix: [answer_question] Task Name: Question Answering
            Prefix: [generate_question] Task Name: Question Generation
            Prefix: [summarize] Task Name: Summarization
            Prefix: [generate_title] Task Name: Title Generation
            Prefix: [translitrate_ar2en] Task Name: Translitration Arabic-to-English
            Prefix: [translitrate_en2ar] Task Name: Translitration English-to-Arabic

            Type your <task_prefix> followed by <text> or (q) to STOP: 

