
from math import log10, sqrt

class Query:


	def __init__( self ):

		self.query = ""
		self.index = {}
		self.normalizeIndex = {}
		self.IDFs = {}
		self.weights = {}
		self.norm = 0
		self.normalizeWeights = {}


	def add( self, querySTR, stmDic ):
		
		self.index = stmDic.copy()
		self.query = querySTR



	def normalize( self ):

		aux = max( self.index.values() )

		for di, vi in self.index.items():

			self.normalizeIndex[di] = vi/aux



	def weightsCalc( self ):

		for dick, dicv in self.normalizeIndex.items():

			if dick in self.IDFs:

				self.weights[dick] = dicv * self.IDFs[dick]
		

	def normCalc( self ):

		for wthsk, wthsv in self.weights.items():

			self.norm += pow( wthsv, 2 )

		self.norm = sqrt( self.norm )
	

	def normalizeWeightsCalc( self ):

		for wthsk, wthsv in self.weights.items():

			self.normalizeWeights[wthsk] = wthsv / self.norm
			
