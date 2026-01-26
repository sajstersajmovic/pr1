#!/bin/python

with open("example.cimg","wb") as file:
    file.write(b"(Nnr")
    file.write((1).to_bytes(2,"little"))
    file.write((64).to_bytes(4,"little"))
    file.write((12).to_bytes(4,"little"))
    file.write(b"W" * (64*12))

