Activate the environment in the folder forDocumentation in cmd. 

1.	Paste the package with your new edits in the folder PyWinda, note to exclude __init__ from the original file when you copy all the modules. 
2.	Delete all rst files except index.rts
3.	Run sphinx-apidoc -o . .\PyWinda to create the relevant rst files
4.	Clean every modules rst file from capturing undocumented sections by deleting   :undoc-members:
5.	Run make html
6. 	The webpage is created automatically in folder _build/html/index.html
