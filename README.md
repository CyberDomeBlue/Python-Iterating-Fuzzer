# Python-Iterating-Fuzzer
This Fuzzer is designed to allow the user to fire off a test case they desire easily and test it rapidly while
also allowing the user to understand whether or not the application crashed and at what time the application crashed.
The fuzzer was developed in a template like fashion and is made for python 3. The code is designed to be easy to understand and easily able to fuzz a system and let the user sit back and let the test run. When the test is complete on python it will currently ask the user if they want to continue. When the system is crashed successfully it will attempt to give you the time, the size of the string it believes is likely to cause the crash and the date and time the crash occured. This data can be used to verify this is not a false positive regarding the code stating the application crashed. If changes like possible test cases, or even character sets or an actual engine for mutating the data are suggested they can be implemented. But currently this is just a proof of concept for a fairly automated and thoughtless fuzzer with not alot of code in python. 
