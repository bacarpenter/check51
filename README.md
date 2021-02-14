# check51

A local focused, easy to use, testing program, built on top of [check50](https://github.com/cs50/check50).

1. [Installation](https://github.com/bacarpenter/check51/tree/main#installation)
2. [Writing Checks](https://github.com/bacarpenter/check51/tree/main#installation)
3. [Running Checks](https://github.com/bacarpenter/check51/tree/main#running-checks)
4. [License](https://github.com/bacarpenter/check51/tree/main#running-checks)

## Installation

Install the python package by:

 1. Cloning the repo onto your machine via the GitHub CLI `gh clone bacarpenter/check51` (or the old-fashioned way with `git clone https://github.com/bacarpenter/check51.git`)

2. Install the python package with `pip install {REPO_DIRECTORY}` where the `{REPO_DIRECTORY}` is where you have the repository cloned on your machine.

3.  Verify your installation with `check51 --v`. It should output: `check50 locally installed, no version information available`

## Writing checks

### Project Structure

I suggest the following project structure:
```
demoProject/
├── myCode.c
└── tests/
	├── .cs50.yaml
	└── outputs/
``` 

Under the tests directory, there are two items:
* `.cs50.yaml` --> this file is where you write your checks.
* `outputs/` --> this directory is where you will find the HTML outputs from `check51`.

The outer project structure does not matter. 

### .cs50.yaml

The `.cs50.yaml` file is where you will write the checks to run on your code base. Here's an example:
```
check50:
	checks:
		squareEachNumber:
			- run:  cd bin && java testSquareEachNumber
			  stdin:  1 2 3
			  stdout:  "{1.0, 4.0, 9.0}"

			- run:  cd bin && java testSquareEachNumber
			  stdin:  1.3 9 3.449
			  stdout:  "{1.6900000000000002, 81.0, 11.895601}"

		divisibleBy7:
			- run:  cd bin && java testDivisibleBy7
			  stdin:  7 5 14
			  stdout:  "{true, false, true}"
			  
			- run:  cd bin && java testDivisibleBy7
			  stdin:  41 12 56
			  stdout:  "{false, false, true}"
```

In this file, we run two checks: `squareEachNumber` && `divisibleBy7`. `- run: ` is followed by a shell command to run. For example, `python3 helloworld.py`. Then, we insert text into standard in with `stdin:` . Finally, we check for the expected output in the console with, `stdout: `. Notice that each "check" has more than one "runs". This is a subtle way to create structure. The outputted HTML file will show a ✅ if **all** of the "runs" succeed, and an ❌ if **one** or more of them fails. 

### outputs/

In this directory, you will find the `test{TIMESTAMP}.html` files the `check51` returns. Check them out in your browser!


## Running checks

To run your checks, use `check51 tests/` (assuming you used the project structure above). Then view the outputs in both the console, and the browser.

### Compiled Languages

Compiled lanuages, such as C or Java, need to be compiled before testing, or, each -run should include a compile statment. Becuase of the way tests are (some what) sand-boxed, writing a "compile test", will not work.

## License

Licensed under the [GNU General Public License v3.0](https://github.com/bacarpenter/check51/blob/main/LICENSE), as was the base project. This license is included in good faith and to the best of my ability. 

*Note: This project is still in progress, and some of the naming conventions will still show check50*
