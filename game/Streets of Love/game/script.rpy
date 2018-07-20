# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define c = Character("Character")

# background images
image classroom = "classroom.jpg"
image testchar  = "testchar.png"


# The game starts here.

label start:

    scene classroom with dissolve

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show testchar

    # These display lines of dialogue.

    c "Good Morning Crono"

    c "You'll be late for your first day of school"

    # This ends the game.

    return
