# Data-Processing
Data Processing Utilities

</br>

### Utilities.py


</br>


##### [addToList](https://github.com/soujanno3dot0/Data-Processing/blob/a0da390d71bde0e4c55deb667e2a595c76083c7d/Utilities.py#L10)

```
  Desc: Appends the formatted messages to the Message List

  Args:
     message(str): Message
     lst_msg(list) - list where message to be added       

  Returns: None

 ```
 
</br>

##### [writeToCsv](https://github.com/soujanno3dot0/Data-Processing/blob/a0da390d71bde0e4c55deb667e2a595c76083c7d/Utilities.py#L26)

```
  Desc: Exports Message List in to csv file. The function will create the file

  Args:
     msgList(list): Message List
     packagePath(str) - Path where file should be created
     fileName(str) - Name of the file       

  Returns: array of file names (full path)

 ```
 
</br>

##### [obtainValidFiles](https://github.com/soujanno3dot0/Data-Processing/blob/a0da390d71bde0e4c55deb667e2a595c76083c7d/Utilities.py#L46)

```
  Desc: Retrieves valid .xml file list from the specified Folder path

  Args:
    packagePath(str): vaid location path
    validFileList(list): valid File (Object) types       

  Returns: array of file names (full path)

 ```
 
</br>

##### [findStringByRegex](https://github.com/soujanno3dot0/Data-Processing/blob/a0da390d71bde0e4c55deb667e2a595c76083c7d/Utilities.py#L73)

```
  Desc: finds the text based on the regex pattern in the text

  Args:
     pattern(str): regular expression
     text(str): text that contains the pattern      

  Returns: text pattern if found, '' otherwise

 ```
 
</br>

##### [splitString](https://github.com/soujanno3dot0/Data-Processing/blob/a0da390d71bde0e4c55deb667e2a595c76083c7d/Utilities.py#L92)

```
  Desc: splits the text based on the separator passed as arg

  Args:
     separator(str): separator pattern
     text(str): text that contains the pattern      

  Returns(list): split list

 ```
 
</br>
