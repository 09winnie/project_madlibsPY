loop=1
while(loop<10):
    def intro(*args,**kwargs):
        name=input("Enter a name: ")
        nationality=input("Enter a country: ")
        age=input("Enter an integer: ")
        like=input("Enter a verb: ")
        like1=input("Enter another verb: ")
        like3=input("Enter a verb: ")
        number=input("Enter a number")
        name1=input("Enter a name: ")
        siblings=input("enter a number: ")
        school=input("enter a noun: ")
        value=input("enter a noun: ")
        value1=input("enter a noun: ")
        value2=input("enter a noun: ")
        value3=input("enter a noun: ")
        dream=input("enter a noun: ")
        keys=kwargs.keys()
        course=kwargs["course"]
        course1=kwargs["course1"]
        course2=kwargs["course2"]
        hobbies=[]
        hobbies.append([like,like1,like3])
        values=[]
        values.append([value,value1,value2,value3])

        print("My name is {} from {}.I am {} and my hobbies are: {}.I am the first born in a family of {}.My role model is {}.I have {} siblings.I study at {} where we study different units like: {}I am majoring in {}.The values that i stand for are {}.My dream is to become a {}".format(name,nationality,age,hobbies,number,name1,siblings,school,args,kwargs,values,dream)) 
    loop+=loop 

intro("Mobile dev","Front-end web dev","Back-end dev","IOT","Hardware electronics and design","UI.UX Design","UI/UX development",course="Back-end dev",course1="UI/UX Design",course2="Mobile dev")
