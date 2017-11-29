#Written by Cadwallader01
#Cozmo tells the user that he is guessing a number from 1-10 and gives them three tries to pick the correct one.
#Cozmo's three cubes will start off blue but for every wrong answer one will turn red and Cozmo's face will also display
#an 'X'
#
#If the user picks the right answer the cubes will change colors multiple times while Cozmo does a celebratory dance
#in the form of a 720 degree spin with his face displaying a checkmark. At the end all the cubes will turn green and
#Cozmo raises his lift
#
#SETUP:
#cube1 on left, cube2 in middle, and cube3 farthest to the right
#Cozmo behind the cubes facing the user with enough space to spin in a circle
#Change directory for images to one that user's 'X' and checkmark png's are saved in


import sys
import time
try:
    from PIL import Image
except ImportError:
    sys.exit("Cannot import from PIL: Do `pip3 install --user Pillow` to install")

import cozmo

import cozmo
from cozmo.util import degrees, distance_mm, speed_mmps
from cozmo.objects import LightCube1Id, LightCube2Id, LightCube3Id

#Displays a check mark for Cozmo when the answer answered is correct
def rightAnswer(robot: cozmo.robot.Robot):
    #CODE GIVEN
    right_answer_image = Image.open("C:/Users/Cadwa/Desktop/Cozmo/cozmo_sdk_examples_1.1.0/face_images/check_rightAnswer.png")
    right_answer_image = right_answer_image.resize(cozmo.oled_face.dimensions(), Image.BICUBIC)
    right_answer_image = cozmo.oled_face.convert_image_to_screen_data(right_answer_image, invert_image=True)
    #display image for 2 seconds
    action = robot.display_oled_face_image(right_answer_image, 2000.0)
    action.wait_for_completed()

#Displays an X for Cozmo when the answer answered is wrong
def wrongAnswer(robot: cozmo.robot.Robot):
    #CODE GIVEN
    wrong_answer_image = Image.open("C:/Users/Cadwa/Desktop/Cozmo/cozmo_sdk_examples_1.1.0/face_images/x_wrongAnswer.png")
    wrong_answer_image = wrong_answer_image.resize(cozmo.oled_face.dimensions(), Image.BICUBIC)
    wrong_answer_image = cozmo.oled_face.convert_image_to_screen_data(wrong_answer_image, invert_image=True)
    #display image for 2 seconds
    action = robot.display_oled_face_image(wrong_answer_image, 1000.0)
    action.wait_for_completed()

def cozmo_program(robot: cozmo.robot.Robot):
    guess = 0
    #initialize Cozmo's head and lift positions
    lift_action = robot.set_lift_height(0.0, in_parallel=True)
    head_action = robot.set_head_angle(cozmo.robot.MAX_HEAD_ANGLE, in_parallel=True)
    lift_action.wait_for_completed()
    head_action.wait_for_completed()

    #initialize Cozmo's cubes to blue
    cube1 = robot.world.get_light_cube(LightCube1Id)  # looks like a paperclip
    cube2 = robot.world.get_light_cube(LightCube2Id)  # looks like a lamp / heart
    cube3 = robot.world.get_light_cube(LightCube3Id)  # looks like the letters 'ab' over 'T'
    if cube1 is not None:
        cube1.set_lights(cozmo.lights.blue_light)
    else:
        cozmo.logger.warning("Cozmo is not connected to a LightCube1Id cube - check the battery.")

    if cube2 is not None:
        cube2.set_lights(cozmo.lights.blue_light)
    else:
        cozmo.logger.warning("Cozmo is not connected to a LightCube2Id cube - check the battery.")

    if cube3 is not None:
        cube3.set_lights(cozmo.lights.blue_light)
    else:
        cozmo.logger.warning("Cozmo is not connected to a LightCube3Id cube - check the battery.")

    #get a random number from 1-5
    from random import randint
    number = randint(1, 5)
    print(number)

    #ask the user to try to guess the random number
    robot.say_text("Number").wait_for_completed()
    userInput = input()

    #give user three tries to get the answer correct
    while guess <= 3:
        if int(number) == int(userInput):
            robot.say_text("That's right!").wait_for_completed()

            #Spin 360 degrees
            robot.turn_in_place(degrees(720))
            # displays a check mark on Cozmo when answer is correct
            rightAnswer(robot)
            time.sleep(0.2)
            cube1.set_lights(cozmo.lights.blue_light)
            cube2.set_lights(cozmo.lights.red_light)
            cube3.set_lights(cozmo.lights.red_light)
            time.sleep(0.2)
            cube1.set_lights(cozmo.lights.red_light)
            cube2.set_lights(cozmo.lights.blue_light)
            cube3.set_lights(cozmo.lights.red_light)
            time.sleep(0.2)
            cube1.set_lights(cozmo.lights.red_light)
            cube2.set_lights(cozmo.lights.red_light)
            cube3.set_lights(cozmo.lights.blue_light)
            time.sleep(0.2)
            cube1.set_lights(cozmo.lights.red_light)
            cube2.set_lights(cozmo.lights.red_light)
            cube3.set_lights(cozmo.lights.red_light)
            time.sleep(0.2)
            cube1.set_lights(cozmo.lights.red_light)
            cube2.set_lights(cozmo.lights.red_light)
            cube3.set_lights(cozmo.lights.blue_light)
            time.sleep(0.2)
            cube1.set_lights(cozmo.lights.red_light)
            cube2.set_lights(cozmo.lights.blue_light)
            cube3.set_lights(cozmo.lights.red_light)
            time.sleep(0.2)
            cube1.set_lights(cozmo.lights.blue_light)
            cube2.set_lights(cozmo.lights.red_light)
            cube3.set_lights(cozmo.lights.red_light)

            time.sleep(0.2)
            cube1.set_lights(cozmo.lights.red_light)
            cube2.set_lights(cozmo.lights.blue_light)
            cube3.set_lights(cozmo.lights.blue_light)
            time.sleep(0.2)
            cube1.set_lights(cozmo.lights.blue_light)
            cube2.set_lights(cozmo.lights.red_light)
            cube3.set_lights(cozmo.lights.blue_light)
            time.sleep(0.2)
            cube1.set_lights(cozmo.lights.blue_light)
            cube2.set_lights(cozmo.lights.blue_light)
            cube3.set_lights(cozmo.lights.red_light)
            time.sleep(0.2)
            cube1.set_lights(cozmo.lights.blue_light)
            cube2.set_lights(cozmo.lights.blue_light)
            cube3.set_lights(cozmo.lights.blue_light)
            time.sleep(0.2)
            cube1.set_lights(cozmo.lights.blue_light)
            cube2.set_lights(cozmo.lights.blue_light)
            cube3.set_lights(cozmo.lights.red_light)
            time.sleep(0.2)
            cube1.set_lights(cozmo.lights.blue_light)
            cube2.set_lights(cozmo.lights.red_light)
            cube3.set_lights(cozmo.lights.blue_light)
            time.sleep(0.2)
            cube1.set_lights(cozmo.lights.red_light)
            cube2.set_lights(cozmo.lights.blue_light)
            cube3.set_lights(cozmo.lights.blue_light)
            time.sleep(0.2)
            cube1.set_lights(cozmo.lights.off_light)
            cube2.set_lights(cozmo.lights.off_light)
            cube3.set_lights(cozmo.lights.off_light)
            time.sleep(0.2)
            cube1.set_lights(cozmo.lights.green_light)
            cube2.set_lights(cozmo.lights.green_light)
            cube3.set_lights(cozmo.lights.green_light)
            robot.move_lift(5)
            time.sleep(2.0)

            guess = 4   #equals 4 to exit while loop
        else:
            guess = guess + 1
            # displays an X on Cozmo when answer is wrong
            wrongAnswer(robot)

            #change a cube color to red if user gets answer wrong
            if guess == 1:
                cube1.set_lights(cozmo.lights.red_light)
            if guess == 2:
                cube2.set_lights(cozmo.lights.red_light)
            if guess == 3:
                cube3.set_lights(cozmo.lights.red_light)

            #let user know how many guesses they have left
            guessesLeft = 3-guess
            if guessesLeft == 0:
                robot.say_text("Game Over").wait_for_completed()
                guess = 4 #equals 4 to exit while loop
                duration_s = 2.0
                time.sleep(duration_s)
                break
            elif guessesLeft == 1:
                robot.say_text("This is your last try! Make it count!").wait_for_completed()
            else:
                robot.say_text("Sorry that's wrong! You have " + str(guessesLeft) + " more tries. Try another number ").wait_for_completed()
            userInput = input()

cozmo.robot.Robot.drive_off_charger_on_connect = False
cozmo.run_program(cozmo_program)
