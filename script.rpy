﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define B = Character("Bunny", color="#c8ffc8")

image bg home = 'home.png'
image farm = 'farmOverview.png'
image farm1 = 'farm1.png'
image farm2 = 'farm2-01.png'
image farm3 = 'farm3-01.png'
image farmer1 = 'farmer1.png'
image farmer2 = 'farmer2.png'
image farmer3 = 'farmer3.png'
image river = 'river-01.png'
image bunny flip = im.Flip("bunny.png", horizontal=True)

# The game starts here.
transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0
    # This is to fade the bar in and out, and is only required once in your script

screen countdown:
    timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('countdown'), Jump(timer_jump)])
    bar value time range timer_range xalign 0.5 yalign 0.9 xmaximum 300 at alpha_dissolve # This is the timer bar.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    $ day=0
    $ water=15
    $ food=15
    $ strength=0

    scene bg forest:
        zoom 0.59
        xalign 0.5
        yalign 0.5

    show bunny:
        zoom 0.3
        xalign 0.5
        yalign 0.7

    B "I got lost in the forest..."

    show bunny:
        linear 1.0 xalign .8 yalign .7

    B "I cannot find my family..."

    show bunny:
        linear .5 xalign .8 yalign .6
        linear 0.5 xalign .8 yalign .7

    B "Ah, here is a cave!"

    scene bg home:
        zoom 0.59
        xalign 0.5
        yalign 0.5

    show bunny:
        zoom 0.3
        xalign 0.8
        yalign 0.7

    B "So, this is going to be my new home."
    "Goal: survive 10 days"
    jump daily

label daily:

    $day += 1
    $water -= 5
    $food -= 5

    if food <=0:
        jump starve

    if water <= 0:
        jump dehydrate

    if day > 10:
        jump success

    scene bg home:
        zoom 0.59
        xalign 0.5
        yalign 0.5

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show bunny:
        zoom 0.3
        xalign 0.8
        yalign 0.7

    # These display lines of dialogue.

    "Day [day]:\n
        water [water]\n
        food [food]\n
        strength [strength]"
    B "Today I'm going to..."

    menu:

        "get water":
            jump water

        "get food":
            jump farm

        "exercise":
            jump exercise

label water:

    scene river:
        zoom 0.59
        xalign 0.5
        yalign 0.5

    show bunny flip:
        zoom 0.2
        xalign 0.6
        yalign 0.8

    B "I should be careful of predetors."
    #drinking minigame here
    pause .5
    $ snake = renpy.random.random()
    if snake <=0.3:
        show snake:
            zoom 0.3
            xalign 0.9
            yalign 0.6

        $ time = 2
        $ timer_range = 2
        $ timer_jump = 'eaten'
        show screen countdown
        menu:
            'HIDE':
                hide screen countdown
                hide snake

    pause .5
    $ eagle = renpy.random.random()
    if eagle <=0.2:
        show eagle:
            zoom 0.3
            xalign 0.2
            yalign 0.2

        $ time = 3
        $ timer_range = 3
        $ timer_jump = 'eaten'
        show screen countdown
        menu:
            'HIDE':
                hide screen countdown
                hide eagle

    pause .5
    $ snake = renpy.random.random()
    if snake <=0.3:
        show snake:
            zoom 0.3
            xalign 1.1
            yalign 0.6

        $ time = 2
        $ timer_range = 2
        $ timer_jump = 'eaten'
        show screen countdown
        menu:
            'HIDE':
                hide screen countdown
                hide snake

    $ water += 13
    'water +13'
    jump daily

label farm:

    scene farm:
        zoom 0.59
        xalign 0.5
        yalign 0.5

    show bunny:
        zoom 0.3
        xalign 0.5
        yalign 0.9

    B "I should go to..."

    menu:

        "farm 1 (easy, low food)":
            jump farm1
        "farm 2 (medium, moderate food)":
            jump farm2
        "farm 3 (hard, high food)":
            jump farm3

    jump daily

label farm1:
    scene farm1:
        zoom 0.59
        xalign 0.5
        yalign 0.5

    show bunny:
        zoom 0.2
        xalign 0.4
        yalign 0.7

    $ caught = renpy.random.random()
    if caught <= .2:
        show farmer1:
            xalign 0.1
            yalign 1.2
            zoom 0.5

        #run minigame here
        $ time = 1
        $ timer_range = 1
        $ timer_jump = 'caught'
        if strength >= 5:
            $ time = 2
            $ timer_range = 2
        if strength > 10:
            $ time = 3
            $ timer_range = 3
        show screen countdown
        menu:
            'RUN!!':
                hide screen countdown
                hide farmer1

    'food +7'
    $ food+=7

    jump daily

label farm2:
    scene farm2:
        zoom 0.59
        xalign 0.5
        yalign 0.5

    show bunny:
        zoom 0.15
        xalign 0.4
        yalign 0.5

    $ caught = renpy.random.random()
    if caught <= .3:
        show farmer2:
            xalign 0.1
            yalign 1.2
            zoom 0.5
        #run minigame here
        $ time = 1
        $ timer_range = 1
        $ timer_jump = 'caught'
        if strength >= 5:
            $ time = 2
            $ timer_range = 2
        if strength > 10:
            $ time = 3
            $ timer_range = 3
        show screen countdown
        menu:
            'RUN!':
                hide screen countdown
                show bunny:
                    linear .5 xalign .7 yalign .7

        $ time = 1
        $ timer_range = 1
        if strength >= 5:
            $ time = 2
            $ timer_range = 2
        if strength > 10:
            $ time = 3
            $ timer_range = 3
        show screen countdown
        menu:
            'RUN!!!':
                hide screen countdown
                show bunny:
                    linear .5 xalign 1.5 yalign .5
                hide farmer2

    'food +10'
    $food+=10

    jump daily

label farm3:
    scene farm3:
        zoom 0.59
        xalign 0.5
        yalign 0.5

    show bunny:
        zoom 0.1
        xalign 0.5
        yalign 0.7

    $ caught = renpy.random.random()
    if caught <= .5:
        show farmer3:
            xalign 0.1
            yalign 1.2
            zoom 0.5
        #run minigame here
        $ time = 1
        $ timer_range = 1
        $ timer_jump = 'caught'
        if strength >= 5:
            $ time = 2
            $ timer_range = 2
        if strength > 10:
            $ time = 3
            $ timer_range = 3
        show screen countdown
        menu:
            'RUN!':
                hide screen countdown
                show bunny:
                    linear .5 xalign .6 yalign .5
        $ time = 1
        $ timer_range = 1
        if strength >= 5:
            $ time = 2
            $ timer_range = 2
        if strength > 10:
            $ time = 3
            $ timer_range = 3
        show screen countdown
        menu:
            'RUN!!':
                hide screen countdown
                show bunny:
                    linear .5 xalign .8 yalign .5
        $ time = 1
        $ timer_range = 1
        if strength >= 5:
            $ time = 2
            $ timer_range = 2
        if strength > 10:
            $ time = 3
            $ timer_range = 3
        show screen countdown
        menu:
            'RUN!!!':
                hide screen countdown
                show bunny:
                    linear .5 xalign 1.5 yalign .5
                hide farmer2

    'food +15'
    $food+=15

    jump daily

label exercise:
    scene bg forest:
        zoom 0.59
        xalign 0.5
        yalign 0.5

    show bunny:
        zoom 0.3
        xalign 0 yalign .7
        block:
            linear 1. xalign 1.0 yalign .7
            linear 1. xalign 0.0 yalign .7
            repeat
        time 5

    'strength +5'
    $strength+=5

    jump daily

label eaten:

        # ... the game continues here.
    scene river:
        zoom 0.59
        xalign 0.5
        yalign 0.5

    show eaten:
        zoom 0.3
        xalign 0.8
        yalign 0.7

    "You have been eaten!"

    # This ends the game.

return

label caught:

    scene bg forest:
        zoom 0.59
        xalign 0.5
        yalign 0.5

    show caught:
        zoom 0.5
        xalign 0.5
        yalign 0.5

    "You have been caught!"

return

label starve:
    scene bg forest:
        zoom 0.59
        xalign 0.5
        yalign 0.5

    show starve:
        zoom 0.3
        xalign 0.5
        yalign 0.7

    'You starved to death!'

return

label dehydrate:
    scene bg forest:
        zoom 0.59
        xalign 0.5
        yalign 0.5

    show dehydrate:
        zoom 0.3
        xalign 0.5
        yalign 0.7

    'You dehydrated to death!'

return

label success:
    scene bg forest:
        zoom 0.59
        xalign 0.5
        yalign 0.5

    show bunny:
        zoom 0.3
        xalign 0.5
        yalign 0.7

    'You survived!'

return
