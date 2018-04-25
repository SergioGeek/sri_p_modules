from bs4 import BeautifulSoup


class Filter:


	#Constructor
	def __init__( self, html_file = "" ):

		self.soup = BeautifulSoup( html_file, "lxml" ) # Objeto para parsear el html
		self.text = "" # texto plano extraido del fichero
		

	#Función que filtra los documentos html
	def filter ( self ):

	
		# Get Title
		self.text = self.soup.title.text


		# Get Date
		date = self.soup.find( "div", attrs = {"class" : "field-item odd"} )
		self.text = self.text + " " + date.find( "span" ).text

		#Get Body
		body = self.soup.find_all( "p" )
		for bd in body:
			self.text = self.text + " " + bd.text
	
	
		# Get Tags
		topics = self.soup.find_all( "a", attrs = {"rel" : "tag"} )
		for i in topics:
			self.text = self.text + " " + i.text

		# Get Rute
		rute = self.soup.find("div", attrs = {"class" : "breadcrumb"})
		for rt in rute.find_all("a"):
			self.text = self.text + " " + rt.text 
		

		# Get Author
		author = self.soup.find("div", attrs = {"class" : "submitted"})
		user = author.text.split()
		self.text = self.text + " " + user[2]
	

		return self.text
