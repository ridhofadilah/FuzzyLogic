def linierNaik(a,b,x):
	return ((x-a) / (b-a))

def linierTurun(a,b,x):
	return ((b-x) / (b-a))

def Emosi(x):
	if (x<=15):
		keanggotaanEmosi = [1,0,0,0,0]
	elif (x>=85) :
		keanggotaanEmosi = [0,0,0,0,1]
	elif (x==20) :
		keanggotaanEmosi = [0,1,0,0,0]
	elif ((x>=40) and (x<=60)) :
		keanggotaanEmosi = [0,0,1,0,0]
	elif (x==75):
		keanggotaanEmosi = [0,0,0,1,0]
	elif (x>75) and (x<85):
		keanggotaanEmosi = [0,0,0,linierTurun(75,85,x),linierNaik(75,85,x)]
	elif (x>60) :
		keanggotaanEmosi = [0,0,linierTurun(60,75,x),linierNaik(60,75,x),0]
	elif (x>20):
		keanggotaanEmosi = [0,linierTurun(20,40,x),linierNaik(20,40,x),0,0]
	elif (x>15):
		keanggotaanEmosi = [linierTurun(15,20,x),linierNaik(15,20,x),0,0,0]
	return keanggotaanEmosi

def Provokasi(x):
	if (x<=15):
		keanggotaanProvokasi = [1,0,0,0,0]
	elif (x>=87) :
		keanggotaanProvokasi = [0,0,0,0,1]
	elif (x==25) :
		keanggotaanProvokasi = [0,1,0,0,0]
	elif (x==50):
		keanggotaanProvokasi = [0,0,1,0,0]
	elif(x==75):
		keanggotaanProvokasi = [0,0,0,1,0]
	elif (x>75) and (x<85):
		keanggotaanProvokasi = [0,0,0,linierTurun(75,87,x),linierNaik(75,87,x)]
	elif (x>50) :
		keanggotaanProvokasi = [0,0,linierTurun(50,75,x),linierNaik(50,75,x),0]
	elif (x>25):
		keanggotaanProvokasi = [0,linierTurun(25,50,x),linierNaik(25,50,x),0,0]
	elif (x>15):
		keanggotaanProvokasi = [linierTurun(15,25,x),linierNaik(15,25,x),0,0,0]
	return keanggotaanProvokasi

def findMin(emosi,provokasi):
	if emosi <= provokasi :
		return emosi
	else :
		return provokasi

def inference(emosi,provokasi):
	x = -1
	KeanggotaanPercaya = [0,0,0]
	for i in emosi:
		x += 1
		y = -1
		for j in provokasi:
			y += 1
			if ((i>0) and (j>0)):
				if ((x==0) and ((y==0) or (y==1) or (y==2))):
					if (findMin(emosi[x],provokasi[y])>KeanggotaanPercaya[0]):
						KeanggotaanPercaya[0] = findMin(emosi[x],provokasi[y])
				elif ((x==0) and (y==3)):
					if (findMin(emosi[x],provokasi[y])>KeanggotaanPercaya[1]):
						KeanggotaanPercaya[1] = findMin(emosi[x],provokasi[y])
				elif ((x==0) and (y==4)):
					if (findMin(emosi[x],provokasi[y])>KeanggotaanPercaya[2]):
						KeanggotaanPercaya[2] = findMin(emosi[x],provokasi[y])
				elif ((x==1) and ((y==0) or (y==1))):
					if (findMin(emosi[x],provokasi[y])>KeanggotaanPercaya[0]):
						KeanggotaanPercaya[0] = findMin(emosi[x],provokasi[y])
				elif ((x==1) and (y==2)):
					if (findMin(emosi[x],provokasi[y])>KeanggotaanPercaya[1]):
						KeanggotaanPercaya[1] = findMin(emosi[x],provokasi[y])
				elif ((x==1) and ((y==3) or (y==4))):
					if (findMin(emosi[x],provokasi[y])>KeanggotaanPercaya[2]):
						KeanggotaanPercaya[2] = findMin(emosi[x],provokasi[y])
				elif ((x==2) and (y==0)):
					if (findMin(emosi[x],provokasi[y])>KeanggotaanPercaya[0]):
						KeanggotaanPercaya[0] = findMin(emosi[x],provokasi[y])
				elif ((x==2) and ((y==1) or (y==2) or (y==3))):
					if (findMin(emosi[x],provokasi[y])>KeanggotaanPercaya[1]):
						KeanggotaanPercaya[1] = findMin(emosi[x],provokasi[y])
				elif ((x==2) and (y==4)):
					if (findMin(emosi[x],provokasi[y])>KeanggotaanPercaya[2]):
						KeanggotaanPercaya[2] = findMin(emosi[x],provokasi[y])
				elif ((x==2) and (y==0)):
					if (findMin(emosi[x],provokasi[y])>KeanggotaanPercaya[0]):
						KeanggotaanPercaya[0] = findMin(emosi[x],provokasi[y])
				elif ((x==3) and ((y==1) or (y==2))):
					if (findMin(emosi[x],provokasi[y])>KeanggotaanPercaya[1]):
						KeanggotaanPercaya[1] = findMin(emosi[x],provokasi[y])
				elif ((x==3) and ((y==3) or (y==4))):
					if (findMin(emosi[x],provokasi[y])>KeanggotaanPercaya[2]):
						KeanggotaanPercaya[2] = findMin(emosi[x],provokasi[y])
				elif ((x==4) and ((y==0) or (y==1))):
					if (findMin(emosi[x],provokasi[y])>KeanggotaanPercaya[1]):
						KeanggotaanPercaya[1] = findMin(emosi[x],provokasi[y])
				elif ((x==4) and ((y==2) or (y==3) or (y==4))):
					if (findMin(emosi[x],provokasi[y])>KeanggotaanPercaya[2]):
						KeanggotaanPercaya[2] = findMin(emosi[x],provokasi[y])
	return KeanggotaanPercaya


def defuzzyfication(percaya):
	hasil = percaya[0] * 0.3
	hasil += percaya[1] * 0.6
	hasil += percaya[2] * 0.8
	hasil /= (percaya[0]+percaya[1]+percaya[2])
	hasil *= 100
	if (hasil >=70):
		return "hoax"
	else :
		return "tidak hoax"

def loadData():
	data = [[97,74],[36,85],[63,43],[82,90],[71,25],[79,81],[55,62],[57,45],[40,65],[57,45],[77,70],[68,75],[60,70],[82,90],[40,85],
			[80,68],[60,72],[50,95],[100,18],[11,99],[58,63],[68,70],[64,66],[57,77],[77,55],[98,64],[91,59],[50,95],[95,55],[27,79]]
	return data

def main():
	data = loadData()
	x = 0
	for i in data:
		x+=1
		percayaa = inference(Emosi(i[0]),Provokasi(i[1]))
		print (x,".",i[0],i[1],defuzzyfication(percayaa))

main()