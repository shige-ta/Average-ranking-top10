# Server-side Engineer Code Check Practice

This repository contains the solutions for the server-side engineer code check practice provided by Yumemi Inc.

## Table of Contents

1. [Description](#description)
2. [Requirements](#requirements)
3. [Setup](#setup)
4. [Implementation](#implementation)
5. [Usage](#usage)
6. [License](#license)

## Description

This project processes a large CSV file containing player game scores and calculates the average scores of players. The top 10 players by average score are then ranked and displayed.

## Requirements

- Python 3.7+
- pandas
- psutil

## Setup

1. Install the required dependencies:
    ```sh
    pip install pandas psutil
    ```

2. Place your CSV file in the appropriate directory. For example:
    ```sh
    mv /path/to/your/game_score_log.csv ./testcases/common/test-4/
    ```

## Implementation

The main script processes the CSV file in chunks to handle large files efficiently. It calculates the total scores and play counts for each player and then determines the average score for each player. Finally, it ranks the top 10 players by their average scores, resolving ties by player ID.

## Usage

1. Run the script:
    ```sh
    python main.py
    ```

2. The output will display the top 10 players, their IDs, and their average scores.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.