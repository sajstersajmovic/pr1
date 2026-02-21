#!/bin/python

with open("example.cimg","wb") as file:
    file.write(b"CMag")
    file.write((100).to_bytes(1, "little"))
