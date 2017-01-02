from __future__ import print_function  # Python 2 compatibility

# If pyperclip is available use it to paste to clipboard
try:
   pyperclip_present = True
   import pyperclip
except:
   pyperclip_present = False

from .errors import IssueLog
from .source import SourcePosition

def write_out(instructions, source_file_path, path, issues: IssueLog):
    """
    takes a collection of instructions and writes them out to a file
    as specified by the path argument
    """

    # TODO: compress label names to be single letters etc?
    content = []  # Contains all the code

    for _line_no, inst in enumerate(instructions):
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
        if len(line) > 18+1: # include CR in count
            issues.error(
                SourcePosition(source_file_path, _line_no+1),
                'line > 18 characters "{}" (it\'s {})',
                line.rstrip(),
                len(line)-1
            )
        content.append(line)

    if len(issues.errors):
        return

    _content = ''.join(content)
    # strip the last CR otherwise a program with the maximum
    # number of lines cannot be pasted:
    _content = _content.rstrip()  
    if path.lower() == 'clipboard':
      if pyperclip_present:
         pyperclip.copy(_content)
         print('%d lines of code pasted to clipboard' % len(content))
         return # all done.  Could write to file "clipboard" too??
      else:
         print('Pasting to clipboard not available, writing to file instead')
         # fall through to write to file "clipboard"

    with open(path, 'w') as output:
       output.write(_content)
    print('%d lines of code written to file "%s"' % (len(content), path))

def main():
  pass

if __name__ == "__main__":
    main()
