import argparse
import os
import sys
import logging
from octopus.octopus import *
import regex
logging.basicConfig(
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=os.environ.get("LOGLEVEL", "INFO").upper(),
    stream=sys.stdout,
)
logger = logging.getLogger("octopus.interactive_cli")

def get_parser():
    parser = argparse.ArgumentParser(
        description="octopus Interactive CLI"
    )
    parser.add_argument('-c', '--cache_dir', default="./octopus_cache", type=str, help='The cache directory path, default vlaue is turjuman_cache directory')


    return parser



def interactive_cli():
    parser = get_parser()
    args = parser.parse_args()
    #-------------------------

    logger.info(args)
    oct_inter = octopus(logger, "./octopus_cache")
    tasks_str=""
    for idx, task in enumerate(oct_inter.tasks):
        tasks_str+=f"Prefix: [{task}] Task Name: {oct_inter.tasks[task]}\n"
    logger.info(f"Loading tasks\n{'-'*50}\nOCTOPUS's tasks:\n{'-'*50}\n{tasks_str}")

    source=""
    while source !='q':
        source = input("Type your <task_prefix> followed by <text> or (q) to STOP: ")
        if source !='q':
            if len(regex.sub('\s+','',source))<1:
                logger.info("Source should be at least 2 characters")
                continue
            l = source.split()
            try:
                task_prefix = regex.sub(":","",l[0])
                task_name = oct_inter.tasks[task_prefix]
            except:
                logger.error("Couldn't recognize the task_preix. Please write the task ID, followed by your text as follow:\n diacritize: this is my text.")
                continue
            source = f"{' '.join(l[1:])}"
            logger.info(f"Task: {task_name}")
            oct_inter.from_text (task_prefix, source, search_method="beam")



if __name__ == "__main__":
    interactive_cli()