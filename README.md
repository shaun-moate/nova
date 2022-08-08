# Nova
My own effort to create stack-based (& compiled) language.  Simply an excuse to learn more about how languages work!

IT IS heavily inspired by Porth (tsoding)! 

## Getting Started
You can either simulate the code OR compile to an executable (output).  The executable is written in Assembly.  The simulation is done using python3.
``` sh
./nova.py --help
./nova.py --simulate (-s)      <file>
./nova.py --compile  (-c) (-r) <file>
     note: adding optional -r to compile script will run build/output immediately
```

## Simple Examples
Some quick and easy examples to demonstrate the language of Nova. It's not perfect (yet) but it can get the job done!

 - Implement an 'if' and 'else' statement
    ``` forth
    10 10 == if
        69 dump
    else 
        96 dump
    end
    ```

 - Count down from 10 with a 'while' loop
    ``` forth
    10 
    do dup 0 < while
        dup dump
        1 -
    end
    ```

## Types Allowed
 - int : any integer that is found program is pushed to the stack
    ```python
    stack.append(a)
    ```

## Memory
TODO -> adding mem keyword that will enable access to memory (** storing data to memory)
 - mem : pushes the address of the beginning of the memory allocation where you can write to and read from onto the stack 
    ```python
    stack.append(mem)
    ```

 - store8 : stores 8bits of memory at the allocated memory address
    ```python
    a = stack.pop(store_value)
    b = stack.pop(mem)
    mem = store_value
    ```

 - load8 : loads 8bits of memory at the allocated memory address to the stack
    ```python
    a = stack.pop(mem)
    store_value = mem
    stack.append(store_value)
    ```
## Conditionals
 - if : will take the top item from the stack (expecting 1 or 0), where if value is 1 it will continue to execute, however if value is 0 is will skip to 'else' or 'end' 
    ```python
    a = stack.pop()
    if a == 0:
        // move into the 'else' block (passing by the 'else' statement) or skips to 'end'
    else:
        // continue into the block of code
    ```

 - else : else acts as a marker to simply skip to the 'end', noting an 'if' moving towards the 'else' is skipping to the 1st instruction in the 'else' block
    ```python
       // skip to the 'end' of the if statement
    ```

 - do : acts as a marker for the 'end' of a 'while' loop, indicating where the 'end' should iterate back to if the 'while' condition remains true
    ```python
       // a marker only for the 'while' loop
    ```

 - while : will take the top item from the stack (expecting 1 or 0), where if value is 1 it will continue to execute, however if value is 0 is will skip to 1 instruction past the 'end' statement
    ```python
    a = stack.pop()
    if a == 0:
        // move into the 1 instruction past the 'end'
    else:
        // continue into the block of code
    ```
    
 - end : acts as a marker to the conclusion of the 'if' or 'while' blocks, depnding on which block it takes seperate actions
    ```python
    if loop_type == 'if':
        pass
    elif loop_type == 'while':
        // move back to the 'do' statement to re-evaluate whether 'while' condition remains to be true
    ```

## Mathematical Operators
 - + : will take the top 2 items from the stack and add them, placing the result back on top of the stack
    ```python
    a = stack.pop()
    b = stack.pop()
    stack.append(a + b)
    ```
 
 - - : will take the top 2 items from the stack and subtract them, placing the result back on top of the stack
    ```python
    a = stack.pop()
    b = stack.pop()
    stack.append(b + a)
    ```
 
 - * : will take the top 2 items from the stack and multiply them, placing the result back on top of the stack
    ```python
    a = stack.pop()
    b = stack.pop()
    stack.append(b * a)
    ```

 - == : will take the top 2 items from the stack and check if they are equal, placing the result back on top of the stack
    ```python
    a = stack.pop()
    b = stack.pop()
    stack.append(int(b == a))
    ```

 - != : will take the top 2 items from the stack and check if they are NOT equal, placing the result back on top of the stack
    ```python
    a = stack.pop()
    b = stack.pop()
    stack.append(int(b != a))
    ```

 - > : will take the top 2 items from the stack and check if b is greater than a, placing the result back on top of the stack
    ```python
    a = stack.pop()
    b = stack.pop()
    stack.append(int(b > a))
    ```

 - >= : will take the top 2 items from the stack and check if b is greater than or equal to a, placing the result back on top of the stack
    ```python
    a = stack.pop()
    b = stack.pop()
    stack.append(int(b >= a))
    ```

 - < : will take the top 2 items from the stack and check if b is less than a, placing the result back on top of the stack
    ```python
    a = stack.pop()
    b = stack.pop()
    stack.append(int(b < a))
    ```

 - <= : will take the top 2 items from the stack and check if b is less than or equal to a, placing the result back on top of the stack
    ```python
    a = stack.pop()
    b = stack.pop()
    stack.append(int(b <= a))
    ```

## Stack Helpers
 - dup : this key word will duplicate the value at the top of the stack
    ```python
    a = stack.pop()
    stack.append(a)
    stack.append(a)
    ```
    
