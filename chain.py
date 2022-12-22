import numpy as np
import matplotlib.pyplot as plt

def random_vector(bond_length):
	v = np.random.uniform(-1.0,1.0,3)
	v_s = np.sqrt(np.sum(np.square(v)))
	v[:] = v[:] / v_s * bond_length
	return v

def random_chain(chain_length, bond_length=1.0):
	x,y,z = [0.0],[0.0],[0.0]
	bonds = []
	for i in range(1,chain_length):
		v = random_vector(bond_length)
		x.append(x[-1] + v[0])
		y.append(y[-1] + v[1])
		z.append(z[-1] + v[2])
		bonds.append((i, i + 1))
	x = np.array(x)
	y = np.array(y)
	z = np.array(z)
	return x,y,z, bonds

def print_picture(X, Y, Z, bonds, types, namefile = 'test'):
	file = open(namefile + '.ent', 'w')
	n = 0
	for x, y, z, t in zip(X, Y, Z, types): 
		n += 1        
		file.write(f'HETATM%5d  {t}%12d' % (n, n) +'%12.3f%8.3f%8.3f \n' % (x, y, z))
	for bond in bonds:
		file.write(f'CONECT%5d%5d' % (bond[0], bond[1]) + '\n')    
	file.close()


if __name__ == '__main__':
	n = 500
	x,y,z,b = random_chain(n)
	t = ['N'] * n
	print_picture(x, y, z, b, t)