package utils;

import java.util.InputMismatchException;
import java.util.Scanner;

public class InputHandler {
    private static final Scanner scan = new Scanner(System.in);

    public static String string() {
        return scan.next().toLowerCase(); // já converte pra minúsculo
    }

    public static int integer() {
        while (true) {
            try {
                return scan.nextInt();
            } catch (InputMismatchException e) {
                System.out.print("Invalid number, try again: ");
                scan.next(); // limpa o buffer do scanner
            }
        }
    }
}
