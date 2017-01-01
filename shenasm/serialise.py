from __future__ import print_function  # Python 2 compatibility

# If pyperclip is available use it to paste to clipboard
try:
   pyperclip_present = True
   import pyperclip
except:
   pyperclip_present = False

def write_out(instructions, path):
    """
    takes a collection of instructions and writes them out to a file
    as specified by the path argument
    """

    # TODO: compress label names to be single letters etc?
    content = ''  # Contains all the code

    for inst in instructions:
        tokens = [
            piece
            for piece in [inst.label, inst.condition, inst.mneumonic] + (inst.args if inst.args is not None else [])
            if piece is not None
            ]
        spacing = ""
        if inst.label is None and inst.condition is None:
            spacing = "  "
        line = "{}{}\n".format(
            spacing,
            " ".join(tokens)
        )
        content += line

    if path.lower() == 'clipboard':
      if pyperclip_present:
         pyperclip.copy(content)
         return # all done.  Could write to file "clipboard" too??
      else:
         print('Pasting to clipboard not available, writing to file "clipboard" instead')
         # fall through to write to file "clipboard"

    with open(path, 'w') as output:
       output.write(content)

