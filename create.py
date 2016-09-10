#!/usr/bin/env python

file = open("questions.txt",'w')

for i in range(50):
    file.write("Pop,Pop Question %s,True\n" % i)
    file.write("Science,Science Question %s,True\n" % i)
    file.write("Sports,Sports Question %s,True\n" % i)
    file.write("Rock,Rock Question %s,True\n" % i)

file.close()
