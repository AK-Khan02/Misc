import java.io.*;
import java.util.*;

class Main {
  public static void main(String[] args) {
    
  
  ArrayList <String> arrayWords = new ArrayList<String>();
  arrayWords.add("dog");
  arrayWords.add("cat");
  arrayWords.add("zebra");
  arrayWords.add("lion");
  arrayWords.add("tiger");
  arrayWords.add("crocodile");
  arrayWords.add("cheetah");
  arrayWords.add("puma");
  arrayWords.add("flamingo");
  arrayWords.add("hyena");

  ArrayList wordsAchieved = new ArrayList();

Random randNum = new Random();
int randomNum = randNum.nextInt(10);


String wordChosen = arrayWords.get(randomNum);
String copyWordChosen = wordChosen;
Scanner input = new Scanner(System.in);
String letter;
int counter;
int numCorrect = 0;
int numTries = 10; 

for (int i = 0; i < wordChosen.length(); i++){
  wordsAchieved.add("▲  ");
  System.out.print( wordsAchieved.get(i) );

}


System.out.println("\nFind the hidden "+wordChosen.length() + " letter word");
for (int i = 1; i < numTries; i++){
  counter=0; //Counter is automatically equated ot 0 once a new letter is chosen
  System.out.println(""); 
  System.out.println("Enter a letter you think is in the word");
  letter = input.nextLine(); 
  int indexPosition = copyWordChosen.indexOf(letter); //Find position of where letter is in word

   if (indexPosition == -1){
     //If letter  is not in word
     System.out.println("This letter was not in the word");
   }

  while (indexPosition != -1){
    //Find how many times letter is in word, and remove all instances of that word 
    numCorrect+=1;
    counter+=1;
    wordsAchieved.set(indexPosition," "+letter+" ");
    copyWordChosen = copyWordChosen.substring(0,indexPosition) + " " + copyWordChosen.substring(indexPosition+1);
  
    indexPosition = copyWordChosen.indexOf(letter);
    
    if (indexPosition == -1){
      System.out.println("This letter was in the word "+counter+"  times");
    }
  }
  for (int j=0; j < wordChosen.length(); j++){
    System.out.print( wordsAchieved.get(j) );
  }
 
  System.out.println("");

  if (numCorrect == wordChosen.length()){
      System.out.println("You Found the word!");
      break;
    }
    System.out.println("");
  System.out.println ( (numTries-i ) + " tries left");
  


}

}

}
