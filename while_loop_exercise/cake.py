width = int(input())
length = int(input())
size_of_cake = width * length  # this also means the number of pieces, because one piece size is 1*1
pieces_taken = 0
command_or_piece = input()  # we put it as string because it might includes the word (Stop)
while command_or_piece != "STOP":
    command_or_piece = int(command_or_piece)  # we convert the str into int
    pieces_taken += command_or_piece
    if pieces_taken >= size_of_cake:
        break
    command_or_piece = input()

if command_or_piece == "STOP":
    print(f"{size_of_cake - pieces_taken} pieces are left.")
else:
    print(f"No more cake left! You need {pieces_taken - size_of_cake} pieces more.")