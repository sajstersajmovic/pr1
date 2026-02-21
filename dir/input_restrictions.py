#!/bin/python

with open("example.cimg", "wb") as file:
    file.write(b"cIMG")
    file.write((1).to_bytes(4, "little"))
    file.write((68).to_bytes(4, "little"))
    file.write((15).to_bytes(1, "little"))
    file.write((68*15)*b"x")
