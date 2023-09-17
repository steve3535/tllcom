## setup python venv
* `python3 -m venv env`  
* `source env/bin/activate`  
* change to python 3.10: `(env) ln -sf /usr/bin/python3.10 $(which python)` 
* set to 3.10 instead of 3.11 because i couldt get pip3.11  
* remember to set the right python interpreter in vscode under preferences > settings > python interpreter  
  otherwise libs installed in the venv wont be available in the editor  
