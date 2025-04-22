package engine;
import engine.models.Difficulty;
import engine.models.GameInfo;
import utils.InputHandler;

import java.time.LocalTime;

public class Game {
    public static void play() {
        Difficulty difficulty = askDifficulty();

        System.out.println("I'm thinking of a number between 1 and 100");

        Game.start(difficulty);

        while (true) {
            System.out.println("Wanna play again? (yes/no)");
            String playAgain = InputHandler.string();
            switch (playAgain) {
                case "yes":
                    Game.start(difficulty);
                    break;
                case "no":
                    return;
                default:
                    System.out.println("Sorry, i didn't understand...");
            }
        }
    }

    private static Difficulty askDifficulty() {
        System.out.println("Select the difficulty:");
        System.out.println("1. Easy (10 chances)");
        System.out.println("2. Medium (5 chances)");
        System.out.println("3. Hard (3 chances)");

        while (true) {
            String input = InputHandler.string();
            switch (input) {
                case "1":
                    return Difficulty.EASY;
                case "2":
                    return Difficulty.MEDIUM;
                case "3":
                    return Difficulty.HARD;
                default:
                    System.out.println("Invalid option, try again.");
            }
        }
    }

    private static void start(Difficulty difficulty) {
        int randomNumber = (int)(Math.random() * 101);
        int chances = difficulty.chances;
        boolean hasGuessed = false;
        int timeStart = LocalTime.now().getHour() * 600 + LocalTime.now().getMinute() * 60 + LocalTime.now().getSecond();
        int timeEnd;

        while (chances > 0 && !hasGuessed) {
            System.out.printf("You have %s chances left\n", chances);
            System.out.print("What's your guess? ");
            int userGuess = InputHandler.integer();

            if (userGuess > 100 || userGuess < 1) {
                System.out.println("Number out of range, its from 1 to 100 only.");
                chances--;
                continue;
            }

            if (userGuess > randomNumber) {
                System.out.println("Too high, try again.");
                chances--;
                continue;
            }

            if (userGuess < randomNumber) {
                System.out.println("Too low, try again.");
                chances--;
                continue;
            }

            hasGuessed = true;
        }

        if (!hasGuessed) {
            System.out.println("You ran out of chances, better luck next time!");
            return;
        }
        System.out.println("Nice! You got it!");
        timeEnd = LocalTime.now().getHour() * 600 + LocalTime.now().getMinute() * 60 + LocalTime.now().getSecond();
        GameInfo gameInfo = new GameInfo(difficulty, chances, timeStart, timeEnd);
        System.out.printf("You guessed in %s tries and it took %s seconds!\n", gameInfo.totalGuesses, gameInfo.timeSpent);

    }
}
