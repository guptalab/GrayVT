# Helberg Theorem Analyzer

## Description

The Helberg Theorem Analyzer is a collection of Python scripts for analyzing Helberg's Theorem 1. It includes utilities for generating strings, calculating moments, and analyzing deletion spheres. Additionally, it provides scripts for calculating asymptotic bounds and generating HTML reports from CSV data.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Credits](#credits)
- [Contact](#contact)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/helberg-theorem-analyzer.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Theorem
   py main.py
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Analysis Functions for Helberg's Theorem (helbergUtility.py)

This module contains utility functions for Helberg's Theorem calculations.

- **generateStrings**: Generate all possible strings of a given length and alphabet size.
- **generateVArray**: Generate the V array required for calculations.
- **calculateMoment**: Calculate the moment for a given number.
- **calculateDeletionSphere**: Calculate the deletion sphere for a given list of strings.

### Theorem 1 Analyzer (analyzeTheorem1.py)

This script analyzes Helberg's Theorem 1 and generates results in a CSV file.

- **analyzeTheorem1**: Analyze Helberg's Theorem 1 for given parameters (n, q, s).

## Contributing

1. Fork the repository on GitHub.
2. Clone your forked repository.
3. Create a new branch for your feature or bug fix.
4. Make changes and commit them to your branch.
5. Push your changes to your fork on GitHub.
6. Submit a pull request to the original repository.


## Credits

- The utility functions in `helbergUtility.py` were developed by Devdeep.js.
- The asymptotic bounds calculation script (`calculate_asymptotic_bounds.py`) was developed by Devdeep.js.
- The HTML loader script (`html_loader.py`) was developed by Devdeep.js.