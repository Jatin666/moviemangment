def movie():
    userinput1=  input("enter the movie :")
    userinput2 = input("enter the release date :")
    userinput3 = input("enter the rating : ")
    return [userinput1,userinput2,userinput3]
def add():
    movielist=[]
    movielist.extend(movie())
    while True:
        print("Press a to add more movies \nPress v to view movies \nPress q to quit \n")
        a=input("enter your choice : ")
        if a=='a' or a=='A':
            movielist.extend(movie())
            data(movielist)
        elif a=='v' or a=='V':
            movielist=data1()
        elif a=='q' or a=='Q':
            print("thank you")
            break
    return movielist
def data(movielist):
    fopen =open("movielist.txt",'a')
    data =fopen.write(str(movielist))
    fopen.close()
    return data
def data1():
    fopen =open("movielist.txt",'r')
    data =fopen.read()
    fopen.close()
    return data