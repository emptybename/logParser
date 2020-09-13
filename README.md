# logParser
-  Requirements
    - python3.7 or greater is required
    - file absolute path should be given while asking in console otherwise
        - file should be present in the current directory with name database.csv and
        - press enter in console when asked for file path 

# Start 
python3 app.py

# Sample output
Method  URL    Frequency

GET    /book/{id}    1

POST    /person/add    1

GET    /person/all    1


<br/>

Method  &nbsp; URL &nbsp;  Min Time &nbsp;  Max Time &nbsp;  Average Time

GET  &nbsp; /person/all &nbsp;  124 &nbsp; &nbsp; &nbsp;&nbsp;&nbsp;&nbsp; 124 &nbsp; &nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 124

POST   /person/add &nbsp;  283 &nbsp; &nbsp; &nbsp;&nbsp;&nbsp;&nbsp;   283 &nbsp; &nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  283

GET &nbsp; /book/{id} &nbsp;  90 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;&nbsp;&nbsp;  90 &nbsp; &nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  90
