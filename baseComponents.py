class Node:
	def __init__ (self, links, name, idx):
		self.links = links
		self.name = name
		self.idx = idx

class PerttNode(Node):
	def __init__ (self, x, y, startStamp, endStam, links, name, idx, shape, color):
		Node.__init__(self, links, name, idx)
		self.shape = shape
		self.color = color
		self.startStamp = startStamp
		self.endStamp = endStamp
		self.x = x
		self.y = y

	def renderNode():
		print 'Rendered PerttNode\n'

class Link:
	def __init__ (self, fromNode, toNode):
		self.fromNode = fromNode
		self.toNode = toNode

class PerttLink(Link):
	def __init__ (self, fromNode, toNode, style):
		Link.__init__(self,fromNode,toNode)
		self.style = style

class Chart:
	def __init__ (self, nodes):
		self.nodes = nodes;
