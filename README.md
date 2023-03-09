## Configuration File Parser
***

To run this program you need to have Python 3.10 or above installed.
Program to parse configuration files made up of white space separated words and
sections delimited by curly braces. 

Here is an example of the configuration file:

```
runtime {
    key1 value1
    key2 value2
    flag1
    
    system1 {
        prop1 value1
        prop2 value2
        ports 1234 5678 9102
        
        subsystem1 {
            prop3 value1 value2 value3
            flag2
        }
    }
    
    more stuff here
}
```

To start the program you have to go to the route of the folder and type the following command:

```
python3 Main.py
```

Then enter the path to the configuration file.

The program will print the tree structure of the configuration file,
then it will ask you to enter a path for a specific section of the file.

Example:

```
runtime.system1.subsystem1
```

Then you can search for a specific key, flag or subsection 
embedded in the section path provided.

To exit the program type 'exit' when asked for a path.