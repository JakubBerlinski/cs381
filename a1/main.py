import sys, time
from ent import Entity
from vector import MyVector

def main():
	entities = []
	for i in range(0,2):
		entities.append(Entity("Entity"+str(i), vel = MyVector(10,0.0,0.0)))
	
	oldTime = time.clock() if sys.platform == 'win32' else time.time()
	for i in range(2000):
		now = time.clock() if sys.platform == 'win32' else time.time()
		dtime = now - oldTime
		oldTime = now
		for ent in entities:
			ent.tick(dtime)
			print str(ent)

if __name__ == '__main__':
	main()
