class Detail(object):
	def __init__(self):
		self.__header = ''' <!DOCTYPE HTML>
		<html>
			<head>
				<title>Dinner Bills</title>
			<head>
			<body> 
		'''

		self.__form = ''' 
			<form action="" method="GET" name="bills" id="links">
				<a href="/?bill=1" name="bill" id="table1">Tabel 1</a>
				<a href="/?bill=2" name="bill" id="table2">Tabel 2</a>
				<a href="/?bill=3" name="bill" id="table3">Tabel 3</a>
				<a href="/?bill=4" name="bill" id="table4">Tabel 4</a>
				<a href="/?bill=5" name="bill" id="table5">Tabel 5</a>
		'''