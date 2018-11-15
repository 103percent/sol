# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define c = Character("Character")

# background images (currently 1024 x 768)
image classroom = "classroom.jpg"
image testchar  = "testchar.png"
image interior  = "interior.png"

# The game starts here.

label start:

    scene classroom with dissolve

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show testchar

    # These display lines of dialogue.

    c "Hey there hot stuff"

    c "Let's go to the car"

    scene interior with dissolve

    show testchar

    c "Cool! We went to the car!"

    c "Time to get down! Vroom! Vroom!"

    # This ends the game.

    return
