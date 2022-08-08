"""
Name: Min Min Tun
Date started: 4/8/2022
GitHub URL: https://github.com/JCUS-CP1404/assignment-1---songs-minnminn22
"""
from operator import itemgetter
import csv
def main():
    """Songs to Learn 1.0 - by Lindsay War"""
    print("Songs to Learn 1.0 - by Lindsay Ward")
    print("6 songs loaded")
    print("Menu:")
    print("{} - List songs \n{} - Add new song \n{} - Complete a song \n{} - Quit".format('L', 'A', 'C', 'Q'))
    choose_menu = menu()
    list_of_song =[]
    text = open("songs.csv",'r')
    for number in text:

        parts = number.strip().split(',')
        number_1 = [parts[0],parts[1],int(parts[2]),parts[3]]
        list_of_song.append(number_1)
        list_of_song.sort(key=itemgetter(1,0))

    while choose_menu != "Q":
        unlearned = 0
        learned = 0

        if choose_menu == "L":
            number_of_song = len(list_of_song)

            for line,number in enumerate(list_of_song):
                if number[3] == "u":
                    string = "*"
                    unlearned += 1
                else:
                    string = " "
                    learned += 1

                print("{:2}. {} {:34} -{:25} ({}) ".format(line,string, number[0], number[1], number[2]))
            print("{} songs learned {} songs still to learn ".format(learned, unlearned))

        elif choose_menu == "C":
            more_song=False
            for i in range(len(list_of_song)):
                if list_of_song[i][3]=='u':
                    more_song=True

            if more_song==False:
                print('No more songs to learn!')
            else:
                print("Enter the number of a song to mark as learned")
                while True:
                    try: # try code that may give an error
                        song = int(input(">>>>> "))
                        if song < 0 or song > number_of_song:
                            raise ValueError
                            print("Number must be greater than 0  or available in song list")
                        elif list_of_song[song][3]=='1':
                            print("You already learned the song {}".format(list_of_song[song]))
                        else:
                            list_of_song[song][3]='1'
                            print("{} by {} ({}) is leaned".format(list_of_song[song][0],list_of_song[song][1],list_of_song[song][2]))
                            break

                    except: # will catch error
                        print("Invalid song number")

        elif choose_menu == "A":
            while True:
                title = input("Title:  ")
                if title=='':
                    print('Input can not be blank')
                else:
                    break

            while True:
                artist = input("Artist: ")
                if artist=='':
                    print('Input can not be blank')
                else:
                    break

            while True:
                year = input("Year: ")
                try:
                    year=int(year)
                    if year<=0:
                        print('Number must be >= 0')
                    else:
                        break
                except:
                    print('Invalid input; enter a valid number')

            print("{} by {} ({}) added to the song list".format(title,artist,year))
            list_of_song.append([title,artist,year,'u'])
            list_of_song.sort(key=itemgetter(1,0))
        else:
            print('Invalid menu choice.')
        print("Menu:")
        print("{} - List songs \n{} - Add new song \n{} - Complete a song \n{} - Quit".format('L', 'A', 'C', 'Q'))
        choose_menu = menu()
        if choose_menu.lower()=='q':
            print(len(list_of_song),'songs saved to songs.csv')
            with open("songs.csv", "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerows(list_of_song)
            print('Have a nice day. :)')


def menu():
    choose_menu = str.upper((input(">>>> ")))
    return choose_menu


if __name__ == '__main__':
    main()
