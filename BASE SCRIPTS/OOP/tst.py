#  Created by Bogdan Trif on 25-07-2018 , 10:47 AM.

class Robot():

    def __init__(self, name):
        print(name + " has been created!")

    def __del__(self):
        print ("Robot has been destroyed" )


x = Robot("Tik-Tok")
y = Robot("Jenkins")

#
# z = x
# print("Deleting x")
# del x
#
# print("Deleting z")
# del z
# del y