import httpx
class fetchdata:
    def __init__(self, url):
        self.url=url
    def fetchdata1(self):
        response=httpx.get(self.url, timeout=10)
        response.raise_for_status()
        data=response.json()   
        return data     
while True:
    print("enter 1 for data from posts")
    print("enter 2 for data from comments")
    print("enter 3 for data from albums")
    print("enter 4 for data from photos")
    print("enter 5 for data from todos")
    print("enter 6 for data from users")
    try:
        ch=int(input("enter your choice: "))
        if ch==1:
            obj=fetchdata("https://jsonplaceholder.typicode.com/posts")
            for item in obj.fetchdata1():
                print(f"{item['userId']} {item['id']} {item['title']} {item['body']}")
        elif ch==2:
            obj=fetchdata("https://jsonplaceholder.typicode.com/comments")
            for item in obj.fetchdata1():
                print(f"{item['postId']} {item['id']} {item['name']} {item['email']} {item['body']}")
        elif ch==3:
            obj=fetchdata("https://jsonplaceholder.typicode.com/albums")
            for item in obj.fetchdata1():
                print(f"{item['userId']} {item['id']} {item['title']}")
        elif ch==4:
            obj=fetchdata("https://jsonplaceholder.typicode.com/photos")
            for item in obj.fetchdata1():
                print(f"{item['albumId']} {item['id']} {item['title']} {item['url']} {item['thumbnailUrl']}")
        elif ch==5:
            obj=fetchdata("https://jsonplaceholder.typicode.com/todos")
            for item in obj.fetchdata1():
                print(f"{item['userId']} {item['id']} {item['title']} {item['completed']}")
        elif ch==6:
            obj=fetchdata("https://jsonplaceholder.typicode.com/users")        
            for item in obj.fetchdata1():
                print(f"{item['id']} {item['name']} {item['username']} {item['email']} {item['address']["city"]}")
        else:
            print("invalid input")
        str1=input("do you want to continue (y/n) ? : ")
        if str1.lower()=="n":
            break   
    except ValueError:
        print("enter a valid integer")
        







