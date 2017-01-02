# test various preprocessor directive edge cases
!fake
!

Label12chars: nop
# line that's not too long
  jmp Label12chars

# And finally, an error
Label13_chars: nop
# line that's too long
  jmp Label13_chars