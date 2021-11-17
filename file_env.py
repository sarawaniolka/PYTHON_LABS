import os
import platform
import tempfile

print(os.environ['HOMEPATH'])
print(platform.system())
print(platform.release())
print(platform.architecture())

print(os.path.expanduser('~'))
with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', delete=False) as my_temp_file:
    print(my_temp_file.name)
    my_temp_file.write("Bla\n")
    my_temp_file.write("abc")
    my_temp_file.close()
    print('closed')

out_file = 'out.txt'
with open(out_file, 'a') as f_out:
    f_out.write("Bla\n")
    f_out.write("ABC\n")
