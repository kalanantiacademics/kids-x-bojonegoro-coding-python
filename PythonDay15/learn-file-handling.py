file_name = "study-notes.txt"

#get data
print("=== File Handling Learning Program ===")
user_text = input("Enter a sentence you want to save: ")

#write
print("\n-> Saving data to the file...")
with open(file_name, "w") as file:
    file.write(user_text)
print("-> Data saved successfully!")

#read
print("\n-> Reading file contents...")
with open(file_name, "r") as file:
    file_content = file.read()

print("\n=== Your File Content ===")
print(file_content)
print("=========================")