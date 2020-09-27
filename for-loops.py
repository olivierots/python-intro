blog_posts = ["", "the 10 coolest math functions in python" , "", "how to make http requests in python" , "a tutorial about data types in python"]

for post in blog_posts:
    if post == "":
        continue
    else:
        print(post)

print('----------------------------')
myString = "This is a string"

for char in myString:
    print(char)

print('----------------------------')
for x in range(0,10):
    print(x)

print('----------------------------')

person = {'Name': 'karen smith', 'Age': 25, 'Gender': 'Female'}
for key in person:
    print(key, ":" , person[key])

print('----------------------------')
blog_posts = {"Python": ["the 10 coolest math functions in python" , "how to make http requests in python" , "a tutorial about data types in python"], "javascript": ["namespaces in javascript", "new functions available in ES6"]}
# print all the blog post by category

for category in blog_posts:
    print("posts about", category)
    for post in blog_posts[category]:
        print(post)


