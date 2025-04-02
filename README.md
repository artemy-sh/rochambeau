### Rochambeau (Rock-Paper-Scissors) Game

[![Lang: RU](https://img.shields.io/badge/lang-RU-blue)](README_RU.md)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue)](#зависимости-для-запуска)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Tests](https://img.shields.io/badge/tests-pytest-blue)](#тестирование)
[![Clean Architecture](https://img.shields.io/badge/architecture-clean%20architecture-orange)](#архитектура)

#### Task description:

- [EN](/TASK_EN.md)
- [RU](/TASK_RU.md)

#### Table of Contents:

- [Description](#description)
- [Requirements](#requirements)
- [Run instructions](#run-instructions)
- [Testing](#testing)
- [Architecture](#architecture)
- [Issue reporting](#issue-reporting)
- [License](#license)

---

#### Description:

**Rochambeau** is a console-based implementation of the classic Rock-Paper-Scissors game, built following Clean Architecture principles ([see below](#architecture)).

The game supports 3 modes:
- Human vs Human (both players enter their moves manually)  
- Human vs AI (one move is entered manually, the other is randomly generated)  
- AI vs AI (both moves are generated randomly)

The game continues until one of the players reaches the required number of wins.  
Each round displays the moves and result (win/loss/draw), and the final score is shown upon completion.  
Logging is included — all actions and errors are written to a log file.

---

#### Requirements:

- Python 3.12 recommended, compatible with Python 3.10+
- No external libraries required
- No installation needed

---

### Run instructions

1. Clone the repository:

   ```bash
   git clone https://github.com/artemy-sh/rochambeau.git
   cd rochambeau
   ```

2. Start the game:

   ```bash
   python3 src/main.py
   ```

---

#### Run examples:

- Set game mode and number of rounds:

  ```bash
  python3 src/main.py --mode ha --rounds 3
  ```

- Enable DEBUG logging:

  ```bash
  python3 src/main.py --log-level debug
  ```

- Show help:

  ```bash
  python3 src/main.py --help
  ```

---

#### Testing:

1. Install `pytest`:

  ```bash
  pip install pytest
  ```

2. Set the source path:

  - On Unix / macOS:
    ```bash
    export PYTHONPATH=src:tests
    ```
  - On Windows (cmd):
    ```cmd
    set PYTHONPATH=src;tests
    ```

3. Run the tests from the project root:

  ```bash
  pytest
  ```

---

#### Architecture:

The project is designed using **Clean Architecture**, which ensures that business logic is isolated from external concerns.  
All dependencies point **inward**, from outer to inner layers.

#### Layer structure:

```
entrypoints
    │
    └── adapters
            │
            └── application
                    │
                    └── domain
```

#### Layer descriptions:

- **domain**  
  Core of the application. Contains business entities (`Game`, `Player`, `Move`, `Result`, `GameSettings`) and key interfaces (`IGame`, `IPlayer`).  
  Does not depend on any other layer and does not interact with infrastructure.

- **application**  
  Contains use cases (interactors) based on domain logic. Includes:
  - `ports`: interface for move providers (`IMoveProvider`)
  - `services`: logging interface (`ILogger`)
  - Interactors (`StartGame`, `PlayRound`) depend on abstractions, not concrete implementations.

- **adapters**  
  Adapters that implement external interfaces:
  - `controllers`: game control logic (`CliController`)
  - `presenters`: result formatting and display (`CliPresenter`)
  - `providers`: move generators for AI (`RandomMoveProvider`)
  - `loggers`: logger implementation (`Logger`) and handlers (`get_console_handler`, `get_file_handler`)

  All adapters implement interfaces from `application` or `domain`.

- **entrypoints**  
  Application entry point.  
  Responsible for:
  - Parsing CLI arguments (`parse_args`)
  - Setting up dependencies (`DIContainer`)
  - Running the game (`entrypoint`, `main.py`)

---

#### Highlights:

- Architecture allows for easy:
  - Switching from CLI to API or web interface
  - Replacing AI move generator with a smarter one
  - Extending functionality without changing business logic
- All dependencies are inverted — `application` depends on interfaces, not implementations
- Logging, input/output, and move generation are adapters, not part of the core logic

---

### Contact

- **Author**: Artemy Shalygin  
- **Email**: [artemy.sh@gmail.com](mailto:artemy.sh@gmail.com)  
- **Telegram**: [@artemy_sh](https://t.me/artemy_sh)

---

#### Issue reporting:

If you find a bug or have a suggestion, feel free to open an issue in the repository.

---

#### License:

[MIT License](/LICENSE)