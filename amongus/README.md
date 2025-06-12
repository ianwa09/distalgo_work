# Multiplayer Voting Game Implementation in DistAlgo

A distributed voting elimination "game" (simulation) built with DistAlgo, demonstrating Dr. Liu's incrementalization framework for efficient distributed computation.

## Overview

This project implements a multiplayer elimination game where players vote to remove others until only one remains. The system showcases incremental computing techniques to optimize distributed gaming scenarios by avoiding unnecessary recomputation and maintaining efficient state management across multiple processes.

## Installation

```bash
# Install DistAlgo
pip install pyDistAlgo

# Clone or download the project files
# amongus.da should be in your working directory
# Note that only Python versions 7, 8, and 9 are supported by DistAlgo.
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

**Player Process**: Manages individual player voting logic and state handling
**Coordinator Process**: Handles vote collection, tallying, and game coordination

### Message Types

- `('start_voting', round, alive_list)`: Coordinator signals start of voting round
- `('vote', round, target, voter)`: Player sends vote to coordinator
- `('elimination', round, eliminated_player)`: Coordinator announces elimination

## Incrementalization

Maintaining Loop Invariants as First-Class State

- **Persistent Game State**: The system maintains `alive_players` sets and `current_round` counters across voting rounds rather than recomputing from scratch
- **Incremental Updates**: Player elimination updates the living player set incrementally (`self.alive_players.remove(eliminated)`) instead of rebuilding the entire game state

Selective Message Processing (P2 Principle)

- **Change-Driven Processing**: Message handlers filter by round number (`if round == self.current_round`) to process only relevant updates
- **Avoid Reprocessing**: Each message is handled exactly once per round, preventing duplicate processing of old messages, as DistAlgo stores all previous messages when using `some()` and `setof()` syntax (without this, processes would be stuck in an infinite loop of processing old messages)
- **Event-Based Updates**: The simulation system will respond to specific events, like votes or eliminations, instead of performing full state analyses, which would be too expensive and inefficient
- **Incremental Vote Collection**: The Coordinator instance for each simulation will collect and tally votes as they arrive, rather than batch processing

### Benefits

- **Fault Tolerance**: Each process maintains independent state, reducing dependency on complete system state
- **Scalability**: Performance scales with actual game changes rather than player count
- **Consistency**: Round-based message filtering ensures consistent distributed state

## References

Thank you to Dr. Annie Liu for support and resources for learning more about her research in incrementalization and DistAlgo.

- DistAlgo Documentation: [https://github.com/DistAlgo/distalgo](https://github.com/DistAlgo/distalgo)
- Dr. Liu's framework and research: [Liu, Y. A. (2024). "Incremental Computation: What Is the Essence? (Invited Contribution)". In Proceedings of the 2024 ACM SIGPLAN International Workshop on Partial Evaluation and Program Manipulation (PEPM 2024), pp. 39-52.](https://dl.acm.org/doi/10.1145/3635800.3637447)
