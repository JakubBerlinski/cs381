import time
from ent import Entity
from vector import MyVector

def main():
	entities = []
	for i in range(0,2):
		entities.append(Entity("Entity"+str(i), vel = MyVector(10,0.0,0.0)))
	
	oldTime = time.time() # time.clock() for windows
	for i in range(2000):
		now = time.time()
		dtime = now - oldTime
		oldTime = now
		for ent in entities:
			ent.tick(dtime)
			print str(ent)

if __name__ == '__main__':
	main()
