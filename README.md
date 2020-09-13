# logParser
-  Requirements
    - python3.7 or greater should be present in your system

# Start Process and commands
Go to logParser directory

```
source env/bin/activate
```

```
python3 app.py 'file_path' (file_path is optional)
``` 

# Sample output
************ Throughput Result **************
<html>
  <head>
  <table>
    <tr>
        <th>Method</th>
        <th>URL</th>
        <th>Frequency</th>
    </tr>
    <tr>
        <td>PUT</td>
        <td>/book/{id}</td>
        <td>7</td>
    </tr>
    <tr>
        <td>GET</td>
        <td>/book/{id}</td>
        <td>5</td>
    </tr>
    <tr>
        <td>POST</td>
        <td>/person/add</td>
        <td>4</td>
    </tr>
    <tr>
        <td>GET</td>
        <td>/book/{id}/return</td>
        <td>4</td>
    </tr>
    <tr>
        <td>GET</td>
        <td>/person/all</td>
        <td>3</td>
    </tr>
  </table>
  
  </head>
</html>



********* Statistic Result ************

<html>
  <head>
  <table>
    <tr>
        <th>Method</th>
        <th>URL</th>
        <th>Min Time</th>
        <th>Max Time</th>
        <th>Average Time</th>
    </tr>
    <tr>
        <td>GET</td>
        <td>/book/{id}/return</td>
        <td>45.0</td>
        <td>78.0</td>
        <td>63.0</td>
    </tr>
    <tr>
        <td>GET</td>
        <td>/book/{id}</td>
        <td>37</td>
        <td>110</td>
        <td>65.40</td>
    </tr>
    <tr>
        <td>PUT</td>
        <td>/book/{id}</td>
        <td>20</td>
        <td>234</td>
        <td>98.57</td>
    </tr>
    <tr>
        <td>GET</td>
        <td>/person/{id}/details</td>
        <td>35</td>
        <td>87</td>
        <td>66.67</td>
    </tr>
    <tr>
        <td>GET</td>
        <td>/person/all</td>
        <td>60.0</td>
        <td>102.0</td>
        <td>86.67</td>
    </tr>
    <tr>
        <td>POSt</td>
        <td>/person/add</td>
        <td>60.0</td>
        <td>140.0</td>
        <td>97.25</td>
    </tr>
  </table>
  
  </head>
</html>