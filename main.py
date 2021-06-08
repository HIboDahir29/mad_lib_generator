from tkinter import *

root = Tk()
root.geometry('300x300')
root.title('DataFlair-Mad Libs Generator')
Label(root, text= 'Mad Libs Generator \n Have Fun!' , font = 'arial 20 bold').pack()
Label(root, text = 'Click Any One :', font = 'arial 15 bold').place(x=40, y=80)

#Madlib1 function
def madlib1():
    animals = input('Enter a animal name: ')
    profession = input('Enter a profession name : ')
    cloth = input('enter a piece of cloth name')
    things = input('Enter a thing name')
    name = input('Enter a name: ')
    place = input('Enter a place name: ')
    verb = input('Enter a verb in ing form: ')
    food = input('Enter a food name: ')
    print('say ' + food + ', the photographer said as the camera flashed! ' + name + ' and I had gone to ' + place +
        ' to get our photos taken on my birthday. The first photo we really wanted was a picture of us dressed as '
        + animals + ' pretending to be a ' + profession +
          '. when we saw the second photo, it was exactly what I wanted. We both looked like ' +
        things + ' wearing ' + cloth + ' and ' + verb + ' --exactly what I had in mind')

def mablib2():
    adjective = input('Enter ')