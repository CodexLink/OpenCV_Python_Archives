<h1 align="center">OpenCV Python Application Archives</h1>
<h4 align="center">A set of Python Applications with OpenCV-Python, NumPy and matplotlib, to be archived during Modular Group 3 Progression of CPE102 - Machine Perception.

<br>Archived for **Post**-Educational Purposes.

</h4>

<div align="center">

![Codacy Grade](https://img.shields.io/codacy/grade/946158dd205b4e86b0f9cb39563d3912?label=Codacy%20Grade&logo=codacy)
[![CodeFactor Grade](https://img.shields.io/codefactor/grade/github/CodexLink/opencv_python_archives?label=CodeFactor%20Grade&logo=codefactor)](https://www.codefactor.io/repository/github/codexlink/opencv_python_archives)
[![Repository License](https://img.shields.io/badge/Repo%20License-MIT-blueviolet)](https://github.com/CodexLink/discord-rich-presence-activity-badge/blob/main/LICENSE)

</div>

## Installation

In this section, you will learn how to get up and running with the scripts for each folder.

### Pre-requisites

Before you start, you should have the following:

1.  **Python 3.8 x64** in your system.
2.  Has `poetry` package installed in your python.
3.  Any IDE with Integrated Terminal, just like [Visual Studio Code](https://code.visualstudio.com/).

> Be aware that `virtualenvs` of poetry is not detected by default by Visual Studio Code. Please refer to the [StackOverflow Issue](https://stackoverflow.com/questions/59882884/vscode-doesnt-show-poetry-virtualenvs-in-select-interpreter-option) or [Github Issue](https://github.com/microsoft/vscode-python/issues/8372).

### Instructions

1.  **Clone** (_If you want to only have a copy of this repo_) or **Fork** (_If you want to commit your own changes_) this repository.

2.  Open the repository folder in your IDE or path your Terminal / Command Prompt to the repository folder that you just cloned / forked.

3.  Type the following:

```text
poetry install
poetry run env python
poetry shell
```

In poetry, if you `poetry install` , all of the `--dev` and `main-dependencies` will be **installed**. If you don't want linting and formatting that is in `dev-dependencies` .

You might wanna opt-out by installing it in a way as this:

> poetry install --no-dev

4.  Choose any **entry point script** file and run it.

## Issues and Contribution

WIP.

## Technicals: Code Quality Exclusions

The assignments I put here were not a type of system that's usually deployed on the hardware. So using **Shell with Popen** does not concern me at this point. The following code pattern checking rules has been excluded:

1.  **B602** — _subprocess_popen_with_shell_equals_true_
2.  **B603** — _subprocess_without_shell_equals_true_
3.  **B604** — _any_other_function_with_shell_equals_true_
4.  **B605** — _start_process_with_a_shell_
5.  **B606** — _start_process_with_no_shell_
6.  **B607** — _start_process_with_partial_path_

## Credits

???

## License

This repository is licensed under [**MIT License**](https://github.com/CodexLink/OpenCV_Python_Archives/blob/main/LICENSE). Please check the file for more information regarding licensing.
