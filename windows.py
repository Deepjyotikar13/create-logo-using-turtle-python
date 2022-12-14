def windows_10(user_co,bg_co):
    import turtle as t
    root=t.Turtle()
    root.color(user_co)#color of the windows 
    root.begin_fill()
    t.bgcolor(bg_co)
    root.backward(200)
    root.right(90)
    root.forward(250)#left side stick
    root.left(80)
    root.forward(400)#down stick
    root.left(100)
    root.forward(389)#right side sick
    root.left(100)
    root.forward(400)
    root.left(80)
    root.end_fill()
    #this section will draw the gaps
    #After comming to the left stick moved it 125 pizel half of 150 pixel and set pensize t0 10 and color of pen blue and moved it 400 pixel left to right then set pen size at 1 and moved it towards the right stick top and again moved it 100 dig and moved it 240 pixel and so on 
    root.forward(125)
    root.left(90)
    root.pensize(10)#increases the size of pen
    root.pencolor(bg_co)
    root.forward(400)
    root.pensize(1)
    root.pencolor(bg_co)
    root.left(90)
    root.forward(200)
    root.left(100)
    root.forward(240)
    root.left(80)
    root.pensize(10)
    root.pencolor(bg_co)
    root.forward(400)
    t.done()	

windows_10("#197DE6","black")
	