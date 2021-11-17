import os
import platform
import tempfile

print(os.environ['HOMEPATH'])
print(platform.system())
print(platform.release())
print(platform.architecture())

print(os.path.expanduser('~'))
#my_temp_file = tempfile.TemporaryFile()
#my_temp_file.write("Bla\n")
#my_temp_file.write("abc")

out_file = 'out.txt'
with open(out_file, 'a') as f_out:
    f_out.write("Bla\n")
    f_out.write("ABC\n")