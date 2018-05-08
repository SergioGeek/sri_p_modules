
from math import log10, sqrt

class Index:


	def __init__( self ):

		self.loco = "Hola"

		self.nameIndex = []
		self.index = []
		self.normalizeIndex = []
		self.wordInDoc = {}
		self.IDFs = {}
		self.weights = []
		self.norm = []
		self.normalizeWeights = []
		self.title = []
		self.body = []
		


	def add( self, fichName, stmDic, tt, bd ):
		
		self.index.append( stmDic.copy() )
		self.nameIndex.append( fichName )
		self.title.append( tt )
		self.body.append( bd )



	def normalize( self ):
		
		aux = 0
		

		for li in self.index:

			auxDic = {}

			aux = max( li.values() )

			for di, vi in li.items():

				auxDic[di] = vi/aux

			self.normalizeIndex.append(auxDic)


	def wordInDocCalc( self ):

		for idx in self.index:
			
			for di in idx:

				if di not in self.wordInDoc:
					
					self.wordInDoc[di] = 1
				else:
					
					self.wordInDoc[di] += 1

	def idfCalc( self ):

		for widk, widv in self.wordInDoc.items():
			
			aux = log10( len(self.index) / widv )
			
			if aux != 0:

				self.IDFs[widk] = aux

		


	def weightsCalc( self ):


		for idx in self.normalizeIndex:
		
			auxDic = {}

			for dick, dicv in idx.items():


				if dick in self.IDFs:

					auxDic[dick] = dicv * self.IDFs[dick]

			self.weights.append( auxDic )
		


	def normCalc( self ):


		for wths in self.weights:

			aux = 0

			for wthsk, wthsv in wths.items():

				aux += pow( wthsv, 2 )

			self.norm.append( sqrt( aux ) )
	

	def normalizeWeightsCalc( self ):

		i = 0
		
		
		for wths in self.weights:

			auxDic = {}

			for wthsk, wthsv in wths.items():

				auxDic[wthsk] = wthsv / self.norm[i]
			

			self.normalizeWeights.append( auxDic )
			i += 1



	def normalizeNormCalc( self ):

		self.norm = []

		for wths in self.normalizeWeights:

			aux = 0

			for wthsk, wthsv in wths.items():

				aux += pow( wthsv, 2 )

			self.norm.append( sqrt( aux ) )

		
