package engine.models;

import java.time.LocalDate;

public class GameInfo {
    public Difficulty difficulty;
    public int totalGuesses;
    public int timeSpent;
    public LocalDate date;

    public GameInfo(Difficulty difficulty, int chancesLeft, int timeStart, int timeEnd) {
        this.difficulty = difficulty;
        this.totalGuesses = this.difficulty.chances - chancesLeft;
        this.timeSpent = Math.abs(timeStart - timeEnd);
        this.date = LocalDate.now();
    }

    @Override
    public String toString() {
        return String.format("%s,%s,%s,%s\n", this.difficulty, this.totalGuesses, this.timeSpent, this.date);
    }
}
