import os
import os.path

start_dir = os.getcwd()
print(f"Current working directory is {start_dir}")

target_dir = "./Code_Examples/Lecture4/mock_src"
os.chdir(target_dir)
print(f"Moving to {target_dir}")

# Open individiaul file
f = open("fib.py", "r", encoding="utf-8")
data = f.read()
f.close()

# Better way
with open("fib.py", "r", encoding="utf-8") as f:
    data = f.read()

files = os.listdir(".")
# files = list(filter(lambda f: True if os.path.isfile(f) else False, files))

license = ""
with open(start_dir + "/LICENSE") as f:
    for l in f:
        license += "# " + l
license += "\n"

print(f"Found files: {files}")
for file in files:
    with open(file, "r+", encoding="utf-8") as f:
        src = f.read()
        f.seek(0)
        f.write(license + src)