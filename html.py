
s = range(1159)
for i in s:
	if i == 0:
		print "<table> <tr>"
		continue
	if i % 20 == 0:
		print "</tr>"
		print "<tr>"
		print " <td> <a href={h}.html> {l} </a> </td>".format(h=i, l=i)
	else:
		print " <td> <a href={h}.html> {l} </a> </td>".format(h=i, l=i)
		

print "</tr> </table>"


