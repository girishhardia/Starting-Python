# dict = {
#     "name" : "nikhil",
#     "age" : "22",
#     "age" : "19",
#     "nerd percent" : "40%"
# }
# print(dict)
# age = dict.get("age")
# keys = dict.keys()
# values = dict.values()
# items = dict.items()
# print(age)
# print(keys)
# print(values)
# print(items)
# # ordered
# # changeable
# # does not allow dublicate value
# dict["roll number"] = 11
# dict["age"] = 33
# dict.update({"age":"23"})
# dict.pop("nerd percent")
# print(dict)
# dict.popitem()
# print(dict)


# dict1 = {"one":1, "two":2, "three":3}
# dict2 = {"four":4, "five":5, "six":6}

# dict1.update(dict2)
# print(dict1)

dict1 = {
    "class":{
        "student":{
            "name":"xyz",
            "marks":{
                "python":100,
                "web":90
            }
        }
    }
}
mark = dict1.get("class").get("student").get("marks").get("web")
print(mark)