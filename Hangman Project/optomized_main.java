import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Random;
import java.util.Scanner;

public class WordGuessingGame {

    public static void main(String[] args) {
        // Read words from the external file
        List<String> words = readWordsFromFile("words_alpha.txt");

        if (words == null || words.isEmpty()) {
            System.out.println("Word list is empty or could not be read. Make sure 'words_alpha.txt' is in the correct location.");
            return;
        }

        Random rand = new Random();
        String chosenWord = words.get(rand.nextInt(words.size()));
        List<String> wordsAchieved = new ArrayList<>(Collections.nCopies(chosenWord.length(), "▲"));

        int numCorrect = 0;
        int numTries = 10;

        System.out.println(String.join(" ", wordsAchieved) + "\nFind the hidden " + chosenWord.length() + " letter word");

        try (Scanner input = new Scanner(System.in)) {
            for (int i = 0; i < numTries; i++) {
                System.out.println("\nEnter a letter you think is in the word:");
                String letter = input.nextLine().toLowerCase();

                int occurrences = 0;
                for (int j = 0; j < chosenWord.length(); j++) {
                    if (chosenWord.charAt(j) == letter.charAt(0) && wordsAchieved.get(j).equals("▲")) {
                        wordsAchieved.set(j, letter);
                        occurrences++;
                        numCorrect++;
                    }
                }

                if (occurrences == 0) {
                    System.out.println("This letter was not in the word");
                } else {
                    System.out.println("The letter '" + letter + "' appears " + occurrences + " times.");
                }

                System.out.println(String.join(" ", wordsAchieved));
                if (numCorrect == chosenWord.length()) {
                    System.out.println("Congratulations! You found the word: " + chosenWord);
                    break;
                }

                System.out.println((numTries - i - 1) + " tries left");
            }
        }

        if (numCorrect != chosenWord.length()) {
            System.out.println("Sorry, you didn't find the word. It was '" + chosenWord + "'.");
        }
    }

    private static List<String> readWordsFromFile(String fileName) {
        try {
            return Files.readAllLines(Paths.get(fileName));
        } catch (IOException e) {
            e.printStackTrace();
            return null;
        }
    }
}
