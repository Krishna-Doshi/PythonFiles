from tkinter import *

root = Tk()
root.geometry('450x350')
root.title('DataFlair-Mad Libs Generator')
Label(root, text= 'Mad Libs Generator \n Have Fun!' , font = 'timesnewroman 20 bold ').pack()
Label(root, text = 'Click Any One :', font = 'timesnewroman 15 bold ').place(x=40, y=80)

def madlib1():

	animal1= input('Enter an animal name')
	animal2= input('Enter a name of animal')
	place = input('Enter a name of place')
	name1 = input('Enter a name')
	name2 = input('Enter a name')
	thing = input('Enter a name of thing')
	fruit = input('Enter a name of fruit')
	flower = input('Enter a name of flower')
	pulses= input('Enter a name of pulse')
	verb = input('Enter a verb in ing form')
	cloth = input('Enter a name of cloth')
	print(animal1+ 'and' +animal2+ 'were staying at' +place+ ' were named as' +name1+ 'and' +name2+ '. They enjoy being together and having' +fruit+ 'everyday. But they do not like' +pulses+ 'they even pluck' +flowers+ 'sometimes from garden when they are' +verb+ 'wearing'+cloth)


def madlib2():
	actor = input('Enter the actor name')
	actress = input('Enter the actress name')
	movie = input('Enter the name of a movie')
	song = input('Enter the song lyrics')
	duration = input('Enter the time')
	print('I like the' +movie+ 'having' +actor+ 'and' +actress+ '. I really enjoyed the' +song+ 'of the' +movie+ 'yet the duration of song is' +duration+ 'long. I enjoyed its happy ending')


Button(root, text= 'The Movie', font ='timesnewroman 15 italic', command= madlib1, bg = 'ghost white').place(x=60, y=120)
Button(root, text= 'The Jungle', font ='timesnewroman 15 italic', command = madlib2 , bg = 'ghost white').place(x=70, y=180)

root.mainloop()
