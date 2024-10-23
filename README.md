
# MPCS 51042 Python Programming Final Project

## Overview

This project involves the implementation of a modeling system using Markov Models for speaker recognition. Additionally, it includes the creation of a custom hash table to efficiently store and retrieve data. The project aims to analyze text and assess the likelihood that a particular speaker uttered it by building and comparing Markov Models.

## Features

### Markov Model Implementation

- **Purpose**: To capture the statistical relationships present in text sequences and use them for speaker recognition.
- **Functionality**:
  - **Model Construction**: Built Markov Models of various orders (k) from given text data.
  - **Probability Calculation**: Computed the log probability of text sequences given a Markov Model.
  - **Speaker Identification**: Identified the most likely speaker of an unknown text by comparing probabilities from multiple Markov Models.

### Custom Hash Table

- **Purpose**: To efficiently store and retrieve data associated with the Markov Models.
- **Functionality**:
  - **Linear Probing**: Implemented a hash table using linear probing to handle collisions.
  - **Rehashing**: Dynamically resized the hash table when the load factor was exceeded to maintain efficiency.
  - **Logical Deletion**: Utilized logical deletion markers to handle deletions and maintain the integrity of the table.

## Components

### 1. Hash Table

Implemented in `hashtable.py`, the custom hash table supports:
- **Initialization**: Set up with initial capacity, load factor, growth factor, and default values.
- **Insertion**: Efficiently added key-value pairs with linear probing.
- **Lookup**: Retrieved values based on keys, including handling missing keys with a default value.
- **Rehashing**: Expanded and rehashed the table when necessary to maintain performance.
- **Deletion**: Marked entries as deleted and physically removed them during rehashing.

### 2. Markov Model

Implemented in `markov.py`, the Markov Model supports:
- **Initialization**: Created a Markov Model of order k from provided text.
- **Probability Calculation**: Calculated the log probability of a given sequence based on the model.
- **Using Hash Tables**: Allowed the option to use the custom hash table or Python's built-in dictionary for storing model data.

### 3. Speaker Recognition

Implemented in `driver.py` and `performance.py`:
- **Speaker Identification**: Compared text against multiple speaker models to identify the most likely speaker.
- **Performance Testing**: Measured the performance of using custom hash tables versus dictionaries for the Markov Model implementation.

## Running the Project

### Dependencies

Ensure you have the following installed:
- Python 3.x
- pytest
- pandas
- seaborn

### Running Tests

Use pytest to run the unit tests:
```sh
pytest test_markov.py
```

### Speaker Recognition

Run the speaker recognition driver:
```sh
python proj/driver.py proj/speeches/bush-kerry3/BUSH-0.txt proj/speeches/bush-kerry3/KERRY-2.txt proj/speeches/bush-kerry3/BUSH-12.txt 2 hashtable
```

Example output:
```
Speaker A: -3.321399706248773
Speaker B: -3.414859165373006

Conclusion: Speaker A is most likely
```

### Performance Testing

Run the performance testing script:
```sh
python proj/performance.py <speakerA_file> <speakerB_file> <unknown_speaker_file> <max_k> <num_runs>
```

## Conclusion

This project demonstrates the implementation of Markov Models for text analysis and speaker recognition, along with a custom hash table for efficient data storage and retrieval. The performance comparison between custom hash tables and built-in dictionaries provides insights into data structure efficiency in practical applications.

## Contact

For questions or feedback, please reach out to:

- **Name**: Josh Cox
- **Email**: [jdcox02@gmail.com](mailto:jdcox02@gmail.com)
- **GitHub**: [jdcox02](https://github.com/jdcox02)
- **LinkedIn**: [jdcox02](https://www.linkedin.com/in/jdcox02)
