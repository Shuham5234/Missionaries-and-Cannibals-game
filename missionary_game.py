boat_side="Right"
missionaries_on_right=3
cannibals_on_right=3

missionaries_on_left=0
cannibals_on_left=0
print( '\U0001f482'*missionaries_on_left, '\U0001f479'*cannibals_on_left,"|",'\U0001f30a'*5,'\U0001f6A2',"|", '\U0001f482'*missionaries_on_right, '\U0001f479'*cannibals_on_right )

while True:
  missionaries=int(input("Enter Missionaries:"))
  cannibals=int(input("Enter Cannibals:"))
  if missionaries+cannibals<1 or missionaries + cannibals > 2:
    print("Invalid move 1")
    continue
  if boat_side=="Right":
    print("Boat is on Right side")
    if missionaries>missionaries_on_right or cannibals>cannibals_on_right:

      print("Invalid move 2")
      continue
    else:
       missionaries_on_right=missionaries_on_right-missionaries
       cannibals_on_right=cannibals_on_right-cannibals
       missionaries_on_left=missionaries_on_left+missionaries
       cannibals_on_left=cannibals_on_left+cannibals
       boat_side = "Left"

    print( '\U0001f482'*missionaries_on_left, '\U0001f479'*cannibals_on_left,"|",'\U0001f6A2','\U0001f30a'*5,"|", '\U0001f482'*missionaries_on_right, '\U0001f479'*cannibals_on_right )


  elif boat_side=="Left":
    print("Boat is on Left side")
    if missionaries>missionaries_on_left or cannibals>cannibals_on_left:
      print("Invalid move 2")
      continue
    else:
      missionaries_on_left=missionaries_on_left-missionaries
      cannibals_on_left=cannibals_on_left-cannibals
      missionaries_on_right=missionaries_on_right+missionaries
      cannibals_on_right=cannibals_on_right+cannibals
    print( '\U0001f482'*missionaries_on_left, '\U0001f479'*cannibals_on_left,"|",'\U0001f30a'*5,'\U0001f6A2',"|", '\U0001f482'*missionaries_on_right, '\U0001f479'*cannibals_on_right )



if (missionaries_on_right<cannibals_on_right and missionaries_on_right>0) or (missionaries_on_left<cannibals_on_left and missionaries_on_left>0):
  print("YOU LOSE")
  
elif missionaries_on_left==3 and cannibals_on_left==3:
    print("YOU WIN")
else:
  print("YOU WIN")















