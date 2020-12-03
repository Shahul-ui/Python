import re
task_list=['umar','babu','0829','0456','jamm']
pattern="[a-zA-Z0-9]"
for i in task_list:
    print(re.findall(pattern,i))
