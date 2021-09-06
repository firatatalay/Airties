def StringRepeat(N):
     #The characters start with the "+" operator and the mod will be taken for each value.
     #If the mod 2 result is 0, that is, the "-" operator will be written if it is an odd number, and the "+" operator will be written if it is an even number.
     #"Join" joins all characters in the list.
     return ''.join(("+" if i%2==0 else "-" for i in range(N)))

print(StringRepeat(5)) 
