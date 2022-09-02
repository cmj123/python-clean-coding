 # Two line spaces between functions /lines
 # 79 characters per line

 # Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
 # Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
 #  when an unknown printer took a galley of type and scrambled it to make a type 
 # specimen book. It has survived not only five centuries, but also the leap into 
 # electronic typesetting, remaining essentially unchanged. It was popularised 
 # in the 1960s with the release of Letraset sheets containing Lorem Ipsum 
 # passages, and more recently with desktop publishing software like Aldus 
 # PageMaker including versions of Lorem Ipsum.

hello_everyone_how_are_you_are_are_you_ok_i_am_good = 1
hello_everyone_how_are_you_are_are_you_ok_i_am_good1 = 2

if hello_everyone_how_are_you_are_are_you_ok_i_am_good1 == 2 or \
    hello_everyone_how_are_you_are_are_you_ok_i_am_good == 1:
    pass

with open('path/to/some/file/you/want/to/read') as file1, \
    open('/path/tosome/file/being/written', 'w') as file2:
    file2.write(file1.read())