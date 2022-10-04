print(r'''
******************************************************************************
           .-.---------------------------------.-.
          ((o))                                   )
           \U/_______          _____         ____/
             |                                  |
             |                                  |
             |                                  |
             | The secret to the 2077 ML Exam   |
             |                                  |
             |                                  |
             |                                  |
             |                                  |
             |                                  |
             |                                  |
             |                                  |
             |____    _______    __  ____    ___|
            /A\                                  \
           ((o))                                  )
            '-'----------------------------------'
*******************************************************************************
''')
print("Welcome to Somapah Island.")
print("Your mission is to find last years Machine Learning exam papers.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
c1 = input("""You are at a crossroad. A sign points left to the renowned Somapah University, while the right points to Somapah Beach.\n
Type "left" to head to the university. Type "right" to head to the beach.
""").lower()
if c1 == "left":
    c2 = input('''You've entered via the back gate and reached the Swimming Pool. There is a bunch of people blocking the path.\nType "wait" to wait for the crowd to clear. Type "swim" to cross via the pool. \n''').lower()
    if c2 == "wait":
        c3 = input("You have arrived at the Somapah Labs. Which lab do you choose? Biology, Physics or Chemistry?\n").lower()
        if c3 == "biology":
            print("You open the door and are attacked by mutant lab rats. Game Over.")
        if c3 == "physics":
            print("You found the Machine Learning papers! Your GPA is saved.")
        if c3 == "chemistry":
            print("You open the door and a bucket of conc. Hydrochloric Acid falls on you. Game Over.")
            
    else:
        print("You dive into the pool. People start cheering and dive into the pool too. You get swarmed by Sarahs, Ryans and Bryans. Game Over.")
else:
    print("You head to the beach and plop down on a bench to chill. Who needs those papers, anyway? Game Over.")
