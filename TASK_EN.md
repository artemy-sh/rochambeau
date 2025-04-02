## Rochambeau (Rock-Paper-Scissors) Game

### Goal
Implement a console-based Rochambeau (Rock-Paper-Scissors) game.

---

### Functional Requirements

1. **Game Modes**  
   - Player vs. Player (both moves are entered manually).  
   - Player vs. AI (one move is entered manually, the other is generated automatically).  
   - AI vs. AI (both moves are generated randomly).

2. **Game Management via CLI**  
   - Start the game with the option to select a mode (default: Player vs. AI).  
   - Allow input of player names (if necessary).  
   - Set the number of wins required to end the game (default: 5).

3. **Gameplay**  
   - If the player is human, they enter their move manually through the CLI.  
   - If the player is AI, the move is generated (by default using `random`, but the architecture should allow for easy **replacement** or **extension** of the implementation).  
   - After each round, information about the moves played and the result (win or draw) is displayed. The round winner receives +1 point; a draw gives 0 points.

4. **Game Conclusion**  
   - The game ends when one of the players reaches the required number of wins.  
   - At the end, the winner’s name and the final score are shown.

5. **Logging**
   - The game’s main actions are logged.  
   - Error messages are displayed in the console (stderr).  
   - Logs at the specified level (DEBUG, INFO, WARNING, ERROR) may be written to a file.

6. **Testing**  
   - The game logic and all components involved in the process must be tested.  
   - Use `pytest` for testing.

7. **README.md**  
   - Contains instructions on how to run the game, configure parameters (number of wins, game mode), and run tests.  
   - Briefly describes the architecture and its key principles.

---

### Evaluation Criteria

1. **Functionality Implementation**  
   Completeness and correctness in meeting all requirements.

2. **Architecture**  
   Application of suitable architectural principles, ease of making changes and extending functionality.

3. **Code Quality and Readability**  
   Consistency of style, meaningful entity names, availability of comments, and clear structure.

4. **Testing Presence and Coverage**  
   Do the tests cover the main scenarios, and is the depth of testing sufficient?

5. **Maintainability and Extensibility**  
   How simple it is to adapt the game to new requirements.