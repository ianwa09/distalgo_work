# Multiplayer Voting Game Implementation in DistAlgo

A distributed voting elimination game simulation built with DistAlgo, demonstrating basic distributed systems concepts including centralized coordination and state management.

## Overview

This project implements a multiplayer elimination game where players vote to remove others until only one remains. The system uses a centralized coordinator pattern and showcases basic distributed programming techniques in DistAlgo.

## Installation

```bash
# Install DistAlgo
pip install pyDistAlgo

# Clone or download the project files
# amongus.da should be in your working directory
# Note that DistAlgo supports Python versions 3.7, 3.8, and 3.9.
```

## Usage

```bash
# Run with default 5 players
python -m da amongus.da

# Run with custom number of players (ex: 3)
python -m da amongus.da 3
```

## Game Rules

1. Players vote to eliminate one player each round
2. The player with the most votes is eliminated
3. Game continues until only one player remains
4. The last surviving player wins

## Architecture

### Components

- **Player Process**: Manages individual player voting logic and state
- **Coordinator Process**: Centralized vote collection, tallying, and game coordination (single point of coordination)

### Message Types

- `('start_voting', round, alive_list)`: Coordinator signals start of voting round
- `('vote', round, target, voter)`: Player sends vote to coordinator
- `('elimination', round, eliminated_player)`: Coordinator announces elimination

## Implementation Features

### State Management

- **Round-based Processing**: Messages filtered by round number for consistency
- **Distributed State**: Each player maintains local game state
- **Centralized Coordination**: Coordinator manages global game logic

### Optimizations

- **Selective Message Processing**: Handlers filter by round to avoid reprocessing
- **Batch Vote Collection**: Coordinator processes all votes per round together
- **State Synchronization**: Round-based updates keep all processes synchronized

### Limitations

- The algorithm could be optimized using Incrementalization, and the algorithm could be written as a consensus algorithm, where there is no coordinator process. This would improve fault tolerance, as there will be no reliance on a central coordinator. The algorithm also utilizes rather simple state updates, which could be improved with the incrementalization framework by performing incremental vote collection. For the future I will work on an implementation that follows the incrementalization framework described by Liu et al.

## References

Thank you to Dr. Annie Liu for support and resources for learning more about her research in incrementalization and DistAlgo.

- DistAlgo Documentation: [https://github.com/DistAlgo/distalgo](https://github.com/DistAlgo/distalgo)
- Dr. Liu's framework and research: [Liu, Y. A. (2024). "Incremental Computation: What Is the Essence? (Invited Contribution)". In Proceedings of the 2024 ACM SIGPLAN International Workshop on Partial Evaluation and Program Manipulation (PEPM 2024), pp. 39-52.](https://dl.acm.org/doi/10.1145/3635800.3637447)
