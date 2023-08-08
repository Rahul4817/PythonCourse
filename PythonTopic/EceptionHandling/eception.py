try:
    file=open("a_file.txt")
    a_dictionary={"key":"value"}
    print(a_dictionary["key"])
except FileNotFoundError:
    file=open("a_file.txt","w")
    file.write("My name is Naurangi lal from RD Engineering College Ghaziabad")
except KeyError as error_message:
    print(f"the key{error_message} does not found")
else:
    content=file.read()
    print(content)
finally:
    file.close()
    print("Fi le was closed")