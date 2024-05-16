#Programming Project 10
#Family Playlist
#By Jessica Laubner

def main():
    
    print('Hello! Here is the Family Playlist\n')
    menu()
    
def menu():
    #print('you are in menu')#uncomment for debugging
    print('Main Menu:\n')
    print('Choose from the following options:\n')

    #while(True):
    print('1.) Add song to playlist\n')
    print('2.) View Playlist\n')
    print('3. Exit\n')
    choice = input("> ")

    if choice == "1":
        writeFile()
    elif choice == "2":
        viewFile()
    elif choice == "3":
        print('exiting...')
        end()
    else:
        print('Invalid choice. Type 1,2 or 3 ', choice)
            
#write file                        
def writeFile():
    #print('You are in songName')#uncomment for debugging
    #Get song Name
    songName = input('Enter the song you would like to add: ')

    #Open a file
    my_file = open('familyplaylist.txt','a')
    
    #Write to the file
    my_file.write(songName)

    #Close the file
    my_file.close()     
    print(songName,'Has been added to the Family Playlist\n')
    menu()
    
#read file
def viewFile():
    infile = open('familyplaylist.txt','r')

    #read line from file
    line = infile.readline()
    
    #strip the \n from each string
    line = line.rstrip('\n')
    
    #close the file
    infile.close()

    #print lines
    print('Here is what is on the playlist: ')
    print(line)
    menu()
    
def end():
    print('This is the end.')
    
#Call the main function
main()

