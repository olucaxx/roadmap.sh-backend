package engine.models;

public enum Difficulty {
    EASY(10),
    MEDIUM(5),
    HARD(3);

    public final int chances;

    Difficulty(int chances) {
        this.chances = chances;
    }
}
