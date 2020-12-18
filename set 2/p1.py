def pad(string, block_length):
  length = len(string)
  padlength = block_length-length%block_length
  newlist = [padlength for i in range(padlength)]
  bytelist = bytes(newlist)
  string += (str(bytelist)[2:])
  return string


print(pad("YELLOW SUBMARINE", 20))