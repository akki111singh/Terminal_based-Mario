# SUPER MARIO GAME:

# Introduction
    A python application (terminal-based) that simulates a basic
    version of Mario.Concepts of Object oriented programming
    must be present within your code.
    
#  Prerequisites
    pip3
    python3
    colorama
    tox
# Installations
    Install colorama by pip3 install -r requirements.txt OR pip3 install colorama
    Install tox by sudo apt-get install tox

# Features

### Code exhibit OO concepts:
      – Inheritance: You could have one person class and have both the
      enemies and player inherit from it.

      – Polymorphism: Have one obstacle class and override various charac-
      teristics to exhibit different properties.

    – Encapsulation: Class and object based approach for all the function-
      ality implemented.

    – Abstraction: Intuitive functionality like move(), attack(), etc, stow-
      ing away inner details from the end user.
      
### Movements
      w: jump upwards
      a: move left
      d: move right
      q: to quit the game
### Obstacles (30 marks):
    – Enemies will move left, right automatically
    – Additionally, you can have enemies with different speed, different
      behaviour (chase the player, etc).
      – Boss enemies with extra lives and additional powerups
### Score (10 marks):
    – Score for duration of the game
    – Bonus score for coins and gems collected
    – Score increments for killing enemies and boss
    – Display the score and life on the screen
### Background & Scenery (10 marks):
    – when moving out of the window, change the scenery
    – Have different scenes in the background, underground, underwater,
      bridges, etc
 # Bonus
      • Color: Have different colors for various objects in the scene
      • Sound: Sound effects on bonus collection and/or enemy kills.
      • Smart enemies: Enemies that show non-random directed behaviour with
      jump and different speed characteristics.
 # Tests
      Written test cases using Pytest for each of the classes I have.
      Test cases for all the classes implemented along with tests for
      functionality. It is Ensured that each functionality is tested.We will then automate the
      testing process using Tox.
    
     Ex. Expected behavior is that when Mario jumps, he will come down after 2 seconds.
      However, when he stands next to a block, he doesn’t come back
      down. So you would write a test that checks whether or not Mario
      comes down, and that would fail in this instance

  # How to run Tests:
      cd tests
      run tox
    
