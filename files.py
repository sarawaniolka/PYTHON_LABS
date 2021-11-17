import os

print(os.getcwd())
out_file = 'PYTHON_LABS/out.txt'

print(__file__)
proj_folder = os.path.dirname(__file__)
out_file = os.path.join(proj_folder, 'PYTHON_LABS', 'out.txt')
print(out_file)