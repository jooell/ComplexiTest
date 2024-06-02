# ComplexiTest

A tool for analyzing the complexity and readability score of Java test files.
The readability score is calculated utilizing the [Scalabrino et al. 2021 tool](https://dibt.unimol.it/report/readability/), which is wrapped into the ComplexiTest program.

## Usage

### Dependencies
- Python >= 3.9
- JDK >= 11

### Run
1. Clone the repository to a local directory and open it..
2. Run the tool with the command `python main.py --directory <path-to-directory-containing-test-files>`.
3. Two *xlsx* files are generated, *complexity_results.xlsx* and *scalabrino.xlsx*, and placed in the *_results* directory.
