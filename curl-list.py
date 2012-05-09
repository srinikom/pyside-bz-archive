p = range(1159)
for i in p:
	print "curl \"http://bugs.pyside.org/show_bug.cgi?id={i}\"".format(i=i) + " > " + str(i) + ".html"


