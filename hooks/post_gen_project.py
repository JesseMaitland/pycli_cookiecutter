import os
os.system('make init-dev')
os.system('make install')
print('{{ cookiecutter.repo_name }} is now avaialable on your local cli. Try it out "{{ cookiecutter.repo_name }}" debug')
