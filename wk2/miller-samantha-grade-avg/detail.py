class Detail(object):
	def __init__(self):
		self.__header = ''' <!DOCTYPE HTML>
		<html>
			<head>
				<title>Dinner Bills</title>
				<link rel='stylesheet' type='text/css' href='css/style.css'/>
				<link rel='stylesheet' type='text/css' href='css/base.css'/>
				<link rel='stylesheet' type='text/css' href='css/layout.css'/>
				<link rel='stylesheet' type='text/css' href='css/skeleton.css'/>
			</head>
			<body><div class='container'> 
		'''

		self.__form = ''' 
			<h1>Table Bills</h1>
			<form method="GET" name="bills" id="links">
				<a href="/?bill=1" name="bill" id="table_1">Tabel 1</a>
				<a href="/?bill=2" name="bill" id="table_2">Tabel 2</a>
				<a href="/?bill=3" name="bill" id="table_3">Tabel 3</a>
				<a href="/?bill=4" name="bill" id="table_4">Tabel 4</a>
				<a href="/?bill=5" name="bill" id="table_5">Tabel 5</a>
			</form>
		'''

		self.__footer = ''' 
		</div>
		</body>
		</html>
		'''

	def header(self):
		return self.__header
	def form(self):
		return self.__form
	def footer(self):
		return self.__footer