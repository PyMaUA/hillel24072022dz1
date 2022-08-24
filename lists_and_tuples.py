our_song = input("Please enter the words of your favorite song ").split()

print("every_third_word --> ", our_song[2::3])

incoming_list = [1, 2.1, "f", "2", 3, "1", 18, "df"]

exit_list = [element if (type(element) == float)
    else element if (type(element) == int and element %2 == 0)
    else element ** 2 if (type(element) == int and element %2 !=0)
    else str(int(element) * 3) if (type(element) == str and element.isdigit())
    else -1 for element in incoming_list]

print(exit_list)

# # Ой у лузі червона калина похилилася, чогось наша славна Україна зажурилася

