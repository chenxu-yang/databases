Finally finished this homework.....
During this homework, I have learned what was database.
In CSVtable, I read CSV file into a list which contained lots of dictionaries, it was hard to start, because at first, I did not know what was template and key, thanks to professor's online OH, I finally understood what were they, I think maybe a guidance file may help a lot.
In RBDtable, to be honest, although I finished this table and the test result were good, I  was still confused about some code in this table, as I copied a lot of code in the lecture'jupyter notebook, I will go to the OH to figure it out but I do know how to connect the SQLworkbench and my python code, that is really cool!!
By the way, professor's OH and TA really help me a lot.

CSVDataTable:read csv file into list, use functions to find /add/delete information of this list.

add_row:add a row in the end of the list
Load:load data in the csv file
Save:write the list into another file
Match template:determine if some given information inside the list.for example: Template:{'lastname':'cy','firstname':'y'}
find_by_primary_key: find the row which contains the information about key.for example: key:['cy']. key can become a template combined with key_columns
find_by_template:find the row which contains the information about the given template.
delete_by_key:delete the row which contains the information about key
delete_by_template:delete the row which contains the information about the given template
update_by_key: find the key_fields in the key_columns, update key_fields into new_values
update_by_template: find the template, update the value into new_values
insert:add a row in the end of the list


RDBDataTable:use python to connect to the SQLworkbench,  use functions to find /add/delete information of this database(translate python language into the SQL language)
 
find_by_primary_key: translate key into template.translate python code into the select function in SQL
find_by_template:translate python code into the select function in SQL
delete_by_key:translate key into template. translate python code into the delete function in SQL
delete_by_template:translate python code into the delete function in SQL
update_by_key: translate key into template. translate python code into the update function in SQL
update_by_template: translate python code into the update function in SQL
insert:translate python code into the insert function in SQL