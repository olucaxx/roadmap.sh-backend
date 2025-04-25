package highscore;

import engine.models.Difficulty;
import engine.models.GameInfo;

import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

public class TextFileHandler {
    private static final Path path = Paths.get(System.getProperty("user.dir"),
            "number-guessing-game", "src", "highscore", "highscores.txt");

    public static void main(String[] args) {
        try {
            if (!Files.exists(path)) {
                Files.createFile(path);
                GameInfo blankEasy = new GameInfo(Difficulty.EASY, 0, 0, 0);
                GameInfo blankMedium = new GameInfo(Difficulty.MEDIUM, 0, 0, 0);
                GameInfo blankHard = new GameInfo(Difficulty.HARD, 0, 0, 0);
                String content = blankEasy.toString() + blankMedium.toString() + blankHard.toString();
                Files.write(path, content.getBytes());
            }

        }
        catch (java.io.IOException e) {
            System.out.println("Arquivo com problema.");
        }
    }
}
