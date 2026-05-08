def robot_traversal (start_x, start_y, target_x, target_y):
    X = start_x
    Y = start_y
    print ("start Position: ", (X, Y))
    print ("Target position: ", (target_x, target_y))
    while (X != target_x) or (Y != target_y):
        if X < target_x:
            X += 1
            print(" Move Right -> (X,Y)")
        elif X > target_x:
            X -= 1
            print(" Move Left-> (X,Y)")
        if Y < target_y:
            Y += 1
            print(" Move Up -> (X,Y)")
        elif Y > target_y:
            Y -= 1
            print(" Move Down -> (X,Y)")
        print(" Robot reached the target position!")
start_x = int (input ("Enten starting x ponition:"))
start_y = int (input ("Enter starting y position: "))
target_x = int (input(" Enter target x position:"))
target_y = int (input ("Enter target y position: "))
robot_traversal (start_x, start_y, target_x, target_y)