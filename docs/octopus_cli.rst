Octopus Command Line
=====================

Usage and Arguments
-------------------

.. code-block:: console

       octopus -h

Octopus Command Line Interface (CLI) ``octopus_cli`` support two types of inputs:

   -  ``-t`` or ``--text``: Write you input text directly on the command line. The generation will display directly on the terminal.
   -  ``-f`` or ``--input_file``: import the text from file. The generation will saved on the JSON format file.

``octopus_cli`` has the following optional arguments.

.. code-block:: console

         usage: octopus [-h] -x PREFIX [-t TEXT] [-f INPUT_FILE] [-m SEARCH_METHOD]
               [-s SEQ_LENGTH] [-o MAX_OUTPUTS] [-b NUM_BEAMS]
               [-n NO_REPEAT_NGRAM_SIZE] [-k TOP_K] [-p TOP_P] [-c CACHE_DIR]
               [-l LOGGING_FILE] [-bs BATCH_SIZE]

         Octopus Command Line Interface (CLI)

            options:
            -h, --help            show this help message and exit
            -x PREFIX, --prefix PREFIX
                                    task prefix [diacritize, correct_grammar, paraphrase,
                                    ,answer_question,generate_question,summarize,
                                    generate_title,
                                    translitrate_ar2en,translitrate_en2ar]
            -t TEXT, --text TEXT  translate the input text into Arabic
            -f INPUT_FILE, --input_file INPUT_FILE
                                    path of input file
           -m SEARCH_METHOD, --search_method SEARCH_METHOD
                                 Turjuman translation search method should be one of
                                 the follows ['greedy', 'beam', 'sampling'], default
                                 value is beam search
           -s SEQ_LENGTH, --seq_length SEQ_LENGTH
                                 The maximum sequence length value, default value is
                                 300
           -o MAX_OUTPUTS, --max_outputs MAX_OUTPUTS
                                 The maxmuim of the output tanslations, default value
                                 is 1
           -b NUM_BEAMS, --num_beams NUM_BEAMS
                                 Number of beams, default value is 5
           -n NO_REPEAT_NGRAM_SIZE, --no_repeat_ngram_size NO_REPEAT_NGRAM_SIZE
                                 Number of n-gram that doesn't appears twice, default
                                 value is 2
           -k TOP_K, --top_k TOP_K
                                 Sample from top K likely next words instead of all
                                 words, default value is 50
           -p TOP_P, --top_p TOP_P
                                 Sample from the smallest set whose cumulative
                                 probability mass exceeds p for next words, default
                                 value is 0.95
           -c CACHE_DIR, --cache_dir CACHE_DIR
                                 The cache directory path, default value is
                                 octopus_cache directory
           -l LOGGING_FILE, --logging_file LOGGING_FILE
                                 The logging file path, default value is None
           -bs BATCH_SIZE, --batch_size BATCH_SIZE
                                 The maximum number of source examples utilized in one
                                 iteration


Google Colab Link
-----------------

You can find the full examples on the Google Colab on the following link
https://colab.research.google.com/github/UBC-NLP/octopus/blob/main/examples/octopus_cli.ipynb
