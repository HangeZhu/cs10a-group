# answers to templates 1-10
# for numbers that have both verticle and horizontal directions, first have answers for verticle then horizontal

p1_ans = ['lava', 'vulcan', 'mantle', 'eruption', 'tectonic', 'mars', 'core', 'geyser', 'conduit','dormant', 'ringoffire', 'flank','magma', 'ash', 'vent']
p2_ans = ['cupcake', 'prize', 'punch', 'partyhat', 'icecream', 'candy', 'candle', 'fireworks', 'balloon', 'magic', 'games', 'music', 'clown','chocolate', 'cake', 'popcorn']
p3_ans = ['france', 'celebration', 'maracas', 'mayfifth', 'chiles', 'red', 'cactus', 'sombrero', 'tacos', 'flowers', 'mariachi', 'salsa', 'battle', 'enchiladas', 'guitar', 'green', 'mexico', 'pinata', 'guacamole']
p4_ans = ['unicycle', 'icecream', 'horse', 'popcorn', 'cannon', 'bear', 'hotdog', 'balloons', 'lion', 'strongman','bicycle', 'ticket', 'tiger', 'clown', 'elephant', 'juggler', 'seal', 'cottoncandy', 'bigtop']
p5_ans = ['mouthwash', 'floss', 'sugar', 'xray', 'toothfairy', 'openwide', 'toothbrush', 'bacteria','cavity', 'checkup','root','hygienist','gargle','dentist','braces','plaque', 'dentures','teeth','gums']
p6_ans = ['soda','drivethrough','milkshake','pizza','taco','onion','straw','pretzel','donuts','nuggets','sandwich','hamburger','bacon','napkin','pickle','ketchup','icecream','frenchfries','egg','forhere','cheeseburger','togo','hotdog','mustard','burrito','tomato']
p7_ans = ['pineapple','watermelon','kiwi','grapefruit','strawberry','pear','apricot','raspberry','blackberry','bananas','coconut','orange','lemon','apple','avocado','grapes','cheeries']
p8_ans = ['trumpet','maracas','violin','xylophone','guitar','accordion','tambourine','trombone','harp','piano','drum','harmonica']
p9_ans = ['judo','tennis','hiking','volleyball','wrestling','karate','lacrosse','skiing','basketball','boxing','swimming','icehockey','gymnastics','bowling','badminton','soccer','cycling','skating','cricket','tabletennis','rugby','golf','football']
p10_ans = ['broccoli','cucumber','onion','cabbage','corn','mushroom','brusselsprout','pumpkin','potato','bellpepper','eggplant','beet','artichoke','radish','garlic','carrot']

from PIL import Image
p1 = Image.open("p1.jpg")
p2 = Image.open("p2.jpg")
p3 = Image.open("p3.jpg")
p4 = Image.open("p4.jpg")
p5 = Image.open("p5.jpg")
p6 = Image.open("p6.jpg")
p7 = Image.open("p7.jpg")
p8 = Image.open("p8.jpg")
p9 = Image.open("p9.jpg")
p10 = Image.open("p10.jpg")
picture_list = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]
answer_list = [p1_ans, p2_ans, p3_ans, p4_ans, p5_ans, p6_ans, p7_ans, p8_ans, p9_ans, p10_ans]



import random
def playcrossword():
    correct = 0

    yesorno = input("Want to play a crossword game? [y/n]")
    while yesorno == "y":
        #randomly generate a picture from picture list
        picture = random.choice(picture_list)

        #get the position of the picture in the picture list
        sequence = picture_list.index(picture)

        #get the answer for the randomly generated picture
        answer = answer_list[sequence]

        showpic = picture.show()
        for i in range(len(answer)):
            user_answer = input("What is the answer for space "+ str(i+1) + "?")
            if user_answer == answer[i]:
                correct += 1
                print("Congrats! You got it right.")
                print("Your current score is ", str(correct), "/", str(i+1))
                print()
            else:
                print("Sorry, you got it wrong...")
                print("Your current score is ", str(correct), "/", str(i+1))
                print()

        print("You finished all!")

        yesorno = input("Want to play a crossword game? [y/n]")

    return("Goodbye!")

playcrossword()
