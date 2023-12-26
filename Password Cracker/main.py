from time import sleep as delay
import time as timer
import sys
import pyfiglet
from os import system as terminal

STYLE_BOLD = "\033[1m"
STYLE_END = "\033[0m"

def display_slow(message, speed=0.037):
  for character in message:
    sys.stdout.write(character)
    sys.stdout.flush()
    timer.sleep(speed)

def display_quickly(message, speed=0.0007):
  for character in message:
    sys.stdout.write(character)
    sys.stdout.flush()
    timer.sleep(speed)

class PasswordHacker:

  def __init__(self):
    self.start_char = ' '
    self.end_char = '~'
    self.max_length = 6
    self.attempts_count = 0
    self.is_found = False
    self.target_password = "Waterloo"

  def generate_passwords(self, current_combo, show_progress):
    if current_combo == self.target_password:
      self.is_found = True
    if len(current_combo) == self.max_length or self.is_found:
      return
    for char_code in range(ord(self.start_char), ord(self.end_char) + 1):
      new_combo = current_combo + chr(char_code)
      if show_progress:
        print(new_combo)
      self.attempts_count += 1
      self.generate_passwords(new_combo, show_progress)

if __name__ == "__main__":
  hacker = PasswordHacker()
  display_slow("Skip intro? (y/n): ")
  skip_intro = input("").lower()
  terminal('clear')
  if skip_intro != "y":
    banner_title = "Password Cracker (Python)"
    banner_art = pyfiglet.figlet_format(banner_title, font='rounded')
    display_quickly(banner_art)
    print()
    delay(1)
    display_slow("Reminder: Your input is not stored.")
    print()
    delay(1)
    print()

  display_slow(f"Enter your {STYLE_BOLD}password{STYLE_END}: ")
  user_password = input("")

  with open("commonPasswords.txt", "r") as file:
    common_pwds = [line.strip() for line in file.readlines()]
    if user_password in common_pwds:
      rank = common_pwds.index(user_password) + 1
      hacker.target_password = user_password
      hacker.max_length = len(hacker.target_password)
      print("\nPassword located in common list!")
      delay(1.5)
      print(f"\nPosition in common passwords: {rank}")
      delay(1.5)
      print("\nIf you use this password, consider changing it.")
      delay(1.5)
      print("----------------------------------")
      print(f"Password: {STYLE_BOLD}{hacker.target_password}{STYLE_END}")
      print(f"Length: {STYLE_BOLD}{hacker.max_length}{STYLE_END}")
      print(f"Attempts: {STYLE_BOLD}1{STYLE_END}")
      print(f"Crack Time: {STYLE_BOLD}0 Seconds{STYLE_END}")
    else:
      view_attempts = input("\nWatch the process? (y/n): ").lower() == 'y'
      hacker.target_password = user_password
      print("\nAttempting to crack password...")
      start = timer.time()
      hacker.max_length = len(hacker.target_password)
      hacker.generate_passwords("", view_attempts)
      time_taken = timer.time() - start
      print("\nPassword cracked!")
      print("----------------------------------")
      print(f"Password: {STYLE_BOLD}{hacker.target_password}{STYLE_END}")
      print(f"Length: {STYLE_BOLD}{hacker.max_length}{STYLE_END}")
      print(f"Attempts: {STYLE_BOLD}{hacker.attempts_count}{STYLE_END}")
      time_label = "Seconds" if time_taken != 1 else "Second"
      print(f"Crack Time: {STYLE_BOLD}{time_taken:.2f} {time_label}{STYLE_END}")
      print(f"Rate: {STYLE_BOLD}{int(hacker.attempts_count / time_taken)} per second{STYLE_END}")
