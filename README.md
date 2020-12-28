<h1 align="center">OpenCV Python Application Archives</h1>
<h4 align="center">A set of Python Applications with OpenCV-Python, NumPy and potentially matplotlib, to be archived during Modular Group 3 Semester Progression of CPE102 - Machine Perception.

<br>Archived for **Post**-Educational Purposes.

</h4>

<div align="center">

![Codacy Grade](https://img.shields.io/codacy/grade/946158dd205b4e86b0f9cb39563d3912?label=Codacy%20Grade&logo=codacy)
[![CodeFactor Grade](https://img.shields.io/codefactor/grade/github/CodexLink/opencv_python_archives?label=CodeFactor%20Grade&logo=codefactor)](https://www.codefactor.io/repository/github/codexlink/opencv_python_archives)
[![Repository License](https://img.shields.io/badge/Repo%20License-MIT-blueviolet)](https://github.com/CodexLink/discord-rich-presence-activity-badge/blob/main/LICENSE)

</div>

## Welcome

Hello! This repository contains of all examples that were in my **CPE 102 Modules**. They were actually based from **Geek4Geeks Examples** but I managed to make modifications to my liking, to the point that, I make them more usable and runnable without any relative imports and other such issues that may occur some problems in the future.

## TL;DR of Repository

In this repository, you will get the following:

1.  **Class-Based Script Assignments.**
2.  **Examples were purely separated from one another.**
3.  **Contains Annotations that may resolve future confusions.**
4.  **Black Formatted Python Scripts**
5.  **Consistent Filenames (entrypoint.py) along with Image Outputs (Mostly in PNG Format)**
6.  **Easy To Use and Explorable Examples**
7.  **Uses Tkinter for File Location Pathfinder**
8.  **Contains Bonus [...] (*)***
9.  **Contains Utilities for Basic Examples (Such as Importing of Script to Use File Explorer instead of Static Path Management) (*)**

These should give you the whole context and benefits of this repository.

## Installation

In this section, you will learn how to get up and running with the scripts for each folder.

### Pre-requisites

Before you start, you should have the following:

1.  **Python 3.8.6 x64 (*)** in your system.
2.  Has installed `poetry` package from the pip of your python.
3.  Has an IDE even without Integrated Terminal. The most flexible one is [Visual Studio Code](https://code.visualstudio.com/).

> ⚠️ Be aware that `virtualenvs` of poetry is not detected by default by Visual Studio Code. Please refer to this [StackOverflow Issue](https://stackoverflow.com/questions/59882884/vscode-doesnt-show-poetry-virtualenvs-in-select-interpreter-option) or this [Github Issue](https://github.com/microsoft/vscode-python/issues/8372) for further information.

**Final Reminder:**

> ❗ Also keep in mind that, the `pyproject.toml` accepts **Python 3.8 and above**! But the packages installed were designed for **Python 3.8.X.** So,please check again if you run to an issue before making an **Issue** or **Pull Requests**.

### Instructions

1.  **Clone** (_If you want to only have a copy of this repo_) or **Fork** (_If you want to commit your own changes_) this repository.
2.  Open the repository folder in your IDE or path your Terminal / Command Prompt to the repository folder that you just cloned / forked.
3.  Type the following:

```text
poetry install
poetry shell
```

In poetry, if you `poetry install` , all of the `-dev-dependencies` and `main-dependencies` will be **installed**. If you don't want linting and formatting that is in `dev-dependencies` . You might wanna opt-out by installing it in a way as this:

> poetry install --no-dev

4.  After setup and environment detection, choose any **entry point script** file and run it.

## Issues and Contribution

Casting an Issue or making a contribution is free. There will be no contribution template or issue template in this repository. Just be formal with your changes / PR and we will get to it.

## Technical: Code Quality Exclusions

The assignments I put here were not a type of system that's usually deployed on the hardware. So using **Shell with Popen** does not concern me at this point. The following code pattern checking rules has been excluded:

1.  **B602** — _subprocess_popen_with_shell_equals_true_ (Bandit)
2.  **B603** — _subprocess_without_shell_equals_true_ (Bandit)
3.  **B604** — _any_other_function_with_shell_equals_true_ (Bandit)
4.  **B605** — _start_process_with_a_shell_ (Bandit)
5.  **B606** — _start_process_with_no_shell_ (Bandit)
6.  **B607** — _start_process_with_partial_path_ (Bandit)
7.  **W0105** — _pointless-string-statement_ (Pylint)

## Credits

WIP.

## License

This repository is licensed under [**MIT License**](https://github.com/CodexLink/OpenCV_Python_Archives/blob/main/LICENSE). Please check the file for more information regarding licensing.
