# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define PC = Character("You")
define H  = Character("Holly")

# background images (currently 1024 x 768)
image classroom = "classroom.jpg"
image testchar  = "testchar.png"
image interior  = "interior.png"

# The game starts here.

label start:

    scene interior with dissolve

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show testchar

    # These display lines of dialogue.
    H "Hey there buddy! {w} where ya headed?"

    H "Ha!{w} Ha!{w} Ha!{w} I’m just messing with ya!" 

    H "Hope you don’t mind a bit of taxi driver humour!"

    show black with fade

    hide testchar

    show testchar

    #"{color=#0000ffff}"

    PC "{color=#3399ff}{i} This is Holly Furyde {/color}{/i}" 

    PC "{color=#3399ff}{i} We’re in our graduating year of high school {/color}{/i}"

    PC "{color=#3399ff}{i} Holly and I have been friends since, well,{w} forever {/color}{/i}"

    PC "{color=#3399ff}{i} He has a second job as a taxi driver {/color}{/i}"

    PC "{color=#3399ff}{i} Of course,{w} I’m not here as a customer... {/color}{/i}"

    hide black with fade

    H "Alright!{w} Let’s get this show on the road!" 

    H "Hah!{w} No pun intended!"

    PC "Er…{w} Holly?"

    H "Yeah bud?"

    PC "I don’t want to tell you your business but…"

    PC "...maybe you should start the taxi?"

    H "…?"

    H "Ack!{w} We haven’t so much as moved an inch!" 

    H "And I call myself a taxi driver!"

    #(Engine starts)

    PC "{color=#3399ff}{i} Why is Holly so flustered? {/color}{/i}" 

    PC "{color=#3399ff}{i} Well...{w} more flustered than usual? {/color}{/i}"

    # This ends the game.

    return
