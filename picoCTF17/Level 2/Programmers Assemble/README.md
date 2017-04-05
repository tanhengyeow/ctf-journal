# Challenge

You found a text file with some really low level code. Some value at the beginning has been X'ed out. Can you figure out what should be there, to make main return the value 0x1? Submit the answer as a hexidecimal number, with no extraneous 0s. For example, the decimal number 2015 would be submitted as 0x7df, not 0x000007df.

# Walkthrough/Solution

We are given the file with the following assembly code:
```
.global main

main:
    mov $0x1, %eax
    mov $0, %ebx
    mov $0x7, %ecx
loop:
    test %eax, %eax
    jz fin
    add %ecx, %ebx
    dec %eax
    jmp loop
fin:
    cmp $0x6f4a, %ebx
    je good
    mov $0, %eax
    jmp end
good:
    mov $1, %eax
end:
    ret
```
Notice that for the main function to return `0x1`, the code needs to reach `good` and so that 0x1 would be assigned to `eax` and then returned. </br>

Stepping through the program, notice that `cmp $0x6f4a, %ebx` needs to be true in order for `je good` to execute. This means that the value of `ebx` must be equals to `0x6f4a`. </br>

The only way this is achieveable through the code is from this instruction `add %ecx, %ebx`, where values are being added to `ebx`. The value stored in `ecx` is 0x7, and we shall keep that in mind. </br>

How do we add the value `0x7` up till `0x6f4a`? Thankfully, there's a loop that we can utilize. </br>

The test instruction in `test %eax, %eax` sets the zero flag, ZF, when the result of the AND operation is zero. This tells the next instruction `jz fin` to execute if the zero flag is set. </br>

Therefore, with all these information, we can figure out that the eax should be `0x6f4a/0x7`. It will skip `jz fin` and continue to add values to `ebx` until the value of `eax` reaches zero, which is achieved through `dec %eax`. </br>

Computing the results with the help of python gives us:

```
>>> "{0:b}".format(0x6f4a/0x7)
'111111100110'
>>> hex(int('111111100110', 2))
'0xfe6'
```

# Learning outcome
1) Introduction to Assembly Language



