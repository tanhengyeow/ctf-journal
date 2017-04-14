# Challenge

A friend was stacking dinner plates, and handed you this, saying something about a "stack". Can you find the difference between the value of esp at the end of the code, and the location of the saved return address? Assume a 32 bit system. Submit the answer as a hexidecimal number, with no extraneous 0s. For example, the decimal number 2015 would be submitted as 0x7df, not 0x000007df.

# Walkthrough/Solution

This problem involves understanding how the stack behaves. You can find a good source about it [here](http://flint.cs.yale.edu/cs421/papers/x86-asm/asm.html). </br>

Here is a detailed explanation of what each instruction does. </br>

```
#stores the stack frame of the calling function on the stack.
pushl %ebp 

#takes the current stack pointer and uses it as the frame for the called function.
mov %esp, %ebp

#These registers are preserved to avoid trashing them if they're not used for either data input or output. That way the caller doesn't have to preserve them by pushing and popping on every function call.
pushl %edi
pushl %esi
pushl %ebx

#This instruction allocates 292 bytes (0x124 is in hex) for local variables.
sub $0x124, %esp 

#All these instructions store values into the memory addresses starting from the esp followed by the next address and so on.
movl $0x1, (%esp)
movl $0x2, 0x4(%esp)
movl $0x3, 0x8(%esp)
movl $0x4, 0xc(%esp)
```

From the above, we can see that only the first 6 instructions affect the stack. Let us treat the esp with address value 0x0. </br>

The following 3 instructions causes the esp to point at 0xc:
```
pushl %edi
pushl %esi
pushl %ebx
```
This instruction causes the esp to point at 0x130:
```
sub $0x124, %esp
```

Referencing from the `Calling convention` section of the document, we know that the value of the return address is stored below the saved ebp. Therefore, the difference obtained is `0x130 + 0x04 = 0x134`

# Learning Outcome
1) Introduction to the stack

