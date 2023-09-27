# Quantum Key Distribution Repository

## Description

Welcome to the Quantum Key Distribution (QKD) Repository. This repository hosts an array of resources, including codes, algorithms, and documentation for implementing quantum key distribution protocols. QKD allows two parties to produce a shared, secret random key, which can be used to encrypt and decrypt messages, ensuring secure communication.

The main protocols implemented in this repository include BB84, B92, and E91, among others. (B92 and E91 coming soon!)

## Table of Contents

- [Background](#background)
- [Installation](#installation)
- [Usage](#usage)
- [Contribute](#contribute)
- [License](#license)

## Background

Quantum Key Distribution (QKD) is a technique that uses quantum mechanics to securely exchange cryptographic keys between two parties (typically referred to as Alice and Bob). The security of QKD is guaranteed by the fundamental principles of quantum mechanics, rather than computational complexity as in classical cryptographic systems.

## Installation

To clone and run this repository, you'll need [Git](https://git-scm.com) and Python3 installed on your computer. From your command line:

```bash
# Clone this repository
$ git clone https://github.com/delanoyoder/QuantumKeyDistribution

# Go into the repository
$ cd QuantumKeyDistribution

# Create venv
python3 -m venv venv

# Activate venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Usage

After installing, you can run the example programs for each protocol and language to see QKD in action. See the README files in each subdirectory for instructions on running the examples.

For example, to run the BB84 protocol implementation in Python:

```bash
# Run the example program
$ python src/BB84.py
```

## Contribute

We encourage contributions from the community to improve and expand the QKD repository.

- Fork the repository
- Create a feature branch (`git checkout -b feature_branch`)
- Commit your changes (`git commit -am 'Add some feature'`)
- Push to the branch (`git push origin feature_branch`)
- Create a new Pull Request

Before contributing, please read our [Contributing Guidelines](CONTRIBUTING.md).

## License

This project is licensed under the MIT License. See the [LICENSE.md](LICENSE.md) file for details.

## Contact

For any questions or concerns, please open an issue or contact the maintainers directly at dayoder4@example.com.

Thank you for exploring the QKD Repository, and happy quantum coding!
