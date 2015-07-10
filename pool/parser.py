

parser = parser.Parser()
tokens = "Set the volume to zero when I 'm in a meeting unless John 's school calls".split()
tags, heads = parser.parse(tokens)
print heads
