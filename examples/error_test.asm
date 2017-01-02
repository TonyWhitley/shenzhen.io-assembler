# test various preprocessor directive edge cases
!include "fake"
!include fake
!include fake"
!include "fake
!include
!fake
!

# constant redefinition
const redef 4
const redef 4

# constants must be integers
const non_integer_const non_integer_value

# argument counts
  mov too many args
  gen test # too few args

# conditions without associated instructions
+
-
@

# fill up memory with too many instructions
  nop
  nop
  nop
  nop
  nop
  nop
  nop
  nop
  nop
  nop
  nop
  nop
  nop
  nop
  nop

# undefined aliases
  mov 0 xout
  mov xout 0

# jmp non-label
  jmp redef
  jmp 100

# use label as arg
label:
  mov label acc
  teq label 0
