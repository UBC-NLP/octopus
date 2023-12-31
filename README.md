<p align="center">
    <br>
    <img src="https://github.com/UBC-NLP/octopus/raw/main/images/octopus.jpg" width="70%" height="70%"/>
    <br>
<p>

<p align="center">
<a href="https://github.com/UBC-NLP/octopus/releases">
        <img alt="GitHub release" src="https://img.shields.io/github/release/UBC-NLP/octopus.svg">
    </a>

<a href="https://demos.dlnlp.ai/octopus">
        <img alt="Documentation" src="https://img.shields.io/website.svg?down_color=red&down_message=offline&up_message=online&url=https://demos.dlnlp.ai/octopus">
    </a>
<a href="https://github.com/UBC-NLP/octopus/blob/main/LICENSE"><img alt="GitHub license" src="https://img.shields.io/github/license/UBC-NLP/octopus?logoColor=blue"></a>
<a href='https://octopus-benchmark.readthedocs.io/en/latest/?badge=latest'><img src='https://readthedocs.org/projects/octopus-benchmark/badge/?version=latest' alt='Documentation Status' /></a>
<a href="https://github.com/UBC-NLP/octopus/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/UBC-NLP/octopus"></a>
<a href="https://github.com/UBC-NLP/octopus/network"><img alt="GitHub forks" src="https://img.shields.io/github/forks/UBC-NLP/octopus"></a>

</p>
 

<img src="https://github.com/UBC-NLP/octopus/raw/main/images/octopus_tasks.png" alt="OCTOPUS" width="55%" height="55%" align="right"/>

Octopus is a neural machine generation toolkit for Arabic Natural Lnagauge Generation (NLG) that described in our ArabiNLP 2023 paper: [**OCTOPUS: A Multitask Model and Toolkit for Arabic Natural Language Generation**](https://arxiv.org/abs/2310.16127v1). 

Octopus designed for eight machine generation tasks, encompassing diacritization, grammatical error correction, news headlines generation, paraphrasing, question answering, question generation, and
transliteration. This comprehensive package includes a Python library along with associated command-line scripts.

<br>

## Requirements and Installation

- To install octopus and develop directly GitHub repo using pip:
```shell
    pip install -U git+https://github.com/UBC-NLP/octopus.git
```
- To install octopus and develop locally:
```shell
    git clone https://github.com/UBC-NLP/octopus.git
    cd octopus
    pip install .
```
## Getting Started
The [full documentation](https://octopus.readthedocs.io/en/latest/) contains instructions for getting started, translation using diffrent methods, intergrate OCTOPUS with your code, and provides more examples.

## Colab Examples
### (1) Command Line Interface
<table style='border:1px red;' width='100%'>
<tr><td><b>Command</b></td><td> <b>Content</b></td><td><b>Colab link</b></td></tr>
<tr>
<td>octopus</td>
<td>
    <ul>
        <li> Usage and Arguments </li>
        <li> Using greedy search</li>
        <li> Using beam search (default)</li>
        <li> Using sampling search</li>
        <li> Read text from file</li>
    </ul>
</td>
<td>
<a href="https://colab.research.google.com/github/UBC-NLP/octopus/blob/main/examples/octopus_cli.ipynb"><img alt="colab" src="https://colab.research.google.com/assets/colab-badge.svg"></a>

 </td>
</tr>
<tr>
<td>octopus_interactive</td>
<td>
    <ul>
        <li> Usage and Arguments </li>
        <li> Examples</li>
    </ul>
</td>
<td> <a href="https://colab.research.google.com/github/UBC-NLP/octopus/blob/main/examples/octopus_interactive_cli.ipynb"><img alt="colab" src="https://colab.research.google.com/assets/colab-badge.svg"></td>
</tr>

</table>

### (2) Integrate Octopus with your python code
<table style='border:1px red;' width='100%'>
<tr><td><b>Functions</b></td><td> <b>Content</b></td><td><b>Colab link</b></td></tr>
<td>generate <br> generate_from_file</td>
<td>
    <ul>
        <li> Install Octopus </li>
        <li> Initial octopus object </li>
        <li> Using greedy search</li>
        <li> Using beam search (default)</li>
        <li> Using sampling search</li>
        <li> Read text from file</li>
    </ul>
</td>
<td> <a href="https://colab.research.google.com/github/UBC-NLP/octopus/blob/main/examples/Integrate_octopus_with_your_code.ipynb"><img alt="colab" src="https://colab.research.google.com/assets/colab-badge.svg"></td>
</tr>
</table>

## License
octopus(-py) is Apache-2.0 licensed. The license applies to the pre-trained models as well.

## Citation
If you use OCTOPUS toolkit or the pre-trained models for your scientific publication, or if you find the resources in this repository useful, please cite our paper as follows (to be updated):
```
 @misc{elmadany2023octopus,
      title={Octopus: A Multitask Model and Toolkit for Arabic Natural Language Generation}, 
      author={AbdelRahim Elmadany and El Moatez Billah Nagoudi and Muhammad Abdul-Mageed},
      year={2023},
      eprint={2310.16127},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}

```



## Acknowledgments
We gratefully acknowledge support from the Natural Sciences and Engineering Research Council of Canada (NSERC; RGPIN-2018-04267), the Social Sciences and Humanities Research Council of Canada (SSHRC; 435-2018-0576; 895-2020-1004; 895-2021-1008), Canadian Foundation for Innovation (CFI; 37771), [ComputeCanada (CC)](www.computecanada.ca),   [UBC ARC-Sockeye](https://doi.org/10.14288/SOCKEYE) and Advanced Micro Devices, Inc. (AMD). Any opinions, conclusions or recommendations expressed in this material are those of the author(s) and do not necessarily reflect the views of NSERC, SSHRC, CFI, CC, AMD, or UBC ARC-Sockeye. 
