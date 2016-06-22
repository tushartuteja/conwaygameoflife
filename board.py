# use python 2.7 to run this file
import unittest

class Board:
	""" Life Board for game of life
	Attributes:
	state: set containing x,y coordinates of living cells
	xsize: horizontal size of board
	ysize: vertical size of board

	Methods:
	set(x,y): set the given cell to live
	tick: takes the board to the next generation
	__get_state(left,right,axis): a method to give coordinates to expand virtual grid

	"""

	def __init__(self, birth = (3,), survive = (2,3) ):
		""" Initialise with birth condtioions and survival conditions"""
		self.state = set()

		# The following 4 variables define boundary of virtual grid
		self.xright = 0
		self.yright = 0
		self.xleft = 0
		self.yleft = 0

		#conditions in which a dead cell will take birth
		self.birth = birth

		#conditions in which a live cell will survive
		self.survive = survive

	def set(self,xdx,ydx):
		""" xdx and ydx coordinates of the live cell"""
		self.state.add((xdx,ydx))
		
		#upgrade grid size if required
		self.xleft,self.xright = self.__get_state(self.xleft,self.xright,xdx)
		self.yleft,self.yright = self.__get_state(self.yleft,self.yright,ydx)
	

	def seed(self,cell_list):
		""" Helper function which takes a list of live cells to iniatilise the grid"""
		for cell in cell_list:
			self.set(cell[0],cell[1])


	def __get_state(self,left, right, axis):
		""" Helper Function to help maintain boundary of the 
		board """
		if axis > left and axis < right :
			return left,right
		elif axis >= right:
			return left, axis + 1
		else:
			return axis - 1, right
	
	def tick(self):
		#Define new state
		new_state = set()
		new_xleft = self.xleft
		new_xright = self.xright
		new_yleft = self.yleft
		new_yright = self.yright

		#iterate through the virtual grid
		for idx in range(self.xleft,self.xright + 1):
			for ydx in range(self.yleft, self.yright + 1):
				
				#count neighbouring cells
				neighbours = self.__get_neighbours(idx,ydx)
				live_neighbours = 0 
				for neighbour in neighbours:
					if neighbour in self.state:
						live_neighbours += 1

				new_cell = False
				
				#what to do if the cell was alive
				if (idx,ydx) in self.state:
					if live_neighbours in self.survive:
						new_state.add((idx,ydx))
						new_cell = True

				#what to do if the cell was dead
				else:
					if live_neighbours in self.birth:
						new_state.add((idx,ydx))
						new_cell = True
						
				#upgrade grid size if required
				if new_cell:				
					new_xleft,new_xright = self.__get_state(new_xleft,new_xright,idx)
					new_yleft,new_yright = self.__get_state(new_yleft,new_yright,ydx)


		self.state = new_state
		self.xleft = new_xleft
		self.xright = new_xright
		self.yleft = new_yleft
		self.yright = new_yright
		
	def __get_neighbours(self, idx, ydx):
		neighbours = set()
		neighbours.add((idx+1 , ydx+1))
		neighbours.add((idx-1 , ydx+1))
		neighbours.add((idx  , ydx+1))
		neighbours.add((idx , ydx-1))
		neighbours.add((idx-1 , ydx))
		neighbours.add((idx+1 , ydx))
		neighbours.add((idx+1 , ydx-1))
		neighbours.add((idx-1 , ydx-1))
		return neighbours

class TestBoard(unittest.TestCase):
	def test_block_pattern(self):
		b = Board()
		b.seed([(1,1),(1,2),(2,1),(2,2)])
		self.assertEqual(b.state,set([(1,1),(1,2),(2,1),(2,2)]))
		b.tick()
		self.assertEqual(b.state,set([(1,1),(1,2),(2,1),(2,2)]))

	def test_boat_pattern(self):
		b = Board()
		b.seed([(0,1),(1,0),(2,1),(0,2),(1,2)])
		self.assertEqual(b.state,set([(0,1),(1,0),(2,1),(0,2),(1,2)]))
		b.tick()
		self.assertEqual(b.state,set([(0,1),(1,0),(2,1),(0,2),(1,2)]))

	def test_ocillator_pattern(self):
		b = Board()
		zero_state = [(1,1),(1,0),(1,2)] 
		one_state = [(1,1),(0,1),(2,1)] 
		b.seed(zero_state)
		self.assertEqual(b.state,set(zero_state))
		b.tick()
		self.assertEqual(b.state,set(one_state))
		b.tick()
		self.assertEqual(b.state,set(zero_state))

	def test_toad_pattern(self):
		b = Board()
		zero_state = [(1,1),(1,3),(1,2),(2,2),(2,3),(2,4)] 
		one_state = [(0,2),(1,1),(1,4),(2,1),(2,4),(3,3)] 
		b.seed(zero_state)
		self.assertEqual(b.state,set(zero_state))
		b.tick()
		self.assertEqual(b.state,set(one_state))
		b.tick()
		self.assertEqual(b.state,set(zero_state))

if __name__ == '__main__':
    unittest.main()


