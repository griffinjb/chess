# Just Another Chess App
# Author: Josh Griffin

# import pymouse

def combinations(l1,l2):
	lo = []
	for i1 in l1:
		for i2 in l2:
			lo.append([i1,i2])
	return(lo)

def rcombinations(l1,l2):
	lo = []
	for i1 in l1:
		lo.append([0,i1])
	for i2 in l2:
		lo.append([i2,0])
	return(lo)

def bcombinations():
	l = [i for i in range(1,9)]
	out = []
	for i in l:
		out.append([i,i])
		out.append([i,-i])
		out.append([-i,i])
		out.append([-i,-i])
	return(out)

class piece:
	color = ''
	rank  = ''
	rowcol = []
	moveset = []

	def p(self):
		if color == 'w':
			self.moveset.append([0,1])
		else:
			self.moveset.append([0,-1])
	def r(self):
		self.moveset = rcombinations([i for i in range(1,9)],[i for i in range(1,9)])
	def kn(self):
		mvs = [[1,2],[1,-2],[-1,2],[-1,-2]]
		self.moveset = zip([mv.reverse for mv in mvs])
	def b(self):
		self.moveset = bcombinations()
	def k(self):
		self.moveset = [[1,1],[1,-1],[-1,1],[-1,-1],[1,0],[-1,0],[0,1],[0,-1]]
	def q(self):
		mvs = [[1,1],[1,-1],[-1,1],[-1,-1],[1,0],[-1,0],[0,1],[0,-1]]
		for mv in mvs:
			for i in range(1,9):
				mvs.append([i*mv[0],i*mv[1]])
		self.moveset = mvs

class chess:
	px = 800
	# mouse = pymouse.PyMouse()
	pieces = [piece() for i in range(32)]


	def __init__(self):
		ranks = ['p','p','p','p','p','p','p','p','r','kn','b','k','q','b','kn','r','p','p','p','p','p','p','p','p','r','kn','b','k','q','b','kn','r']
		for i in range(32):
			if i<16:
				self.pieces[i].color = 'w'
			else:
				self.pieces[i].color = 'b'
			self.pieces[i].rank = ranks[i]

			eval('self.pieces[i].'+ self.pieces[i].rank)
			
		rows = [1,0,6,7]

		def ctr():
			i = 0
			while True:
				yield(i)
				i+=1

		for row in rows:
			for i in range(8):
				self.pieces[ctr()].rowcol = [row,i]






if __name__ == "__main__":

	# initialize everything

		# display
		# state object
		game = chess()

	# Monitor mouse
	# on click:
		# switch on state
			# if position valid
				# execute state transition





