import math
import numpy as np
from collections import Counter

def calc_abc_from_line_2d(x0, y0, x1, y1):
	a = y0 - y1
	b = x1 - x0
	c = x0*y1 - x1*y0
	return a, b, c

class hex2rgb:
	def h2r(hex_code):
		hex_code = hex_code.strip('#')
		r = int(hex_code[0:2], 16)
		g = int(hex_code[2:4], 16)
		b = int(hex_code[4:6], 16)
		return [r, g, b, 1]

class lenproperties:
	def islen():#判断棱镜是否存在
		pass

class linetool:
	def linesequence(faceside):#faceside={line1:[[x1,y1],[x2,y2]],line2:[[x1,y1],[x2,y2]]}
		keylist = []
		valuelist = []
		dotvalue = None
		NewFaceSequence = {}
		for key,value in faceside.items():
			keylist.append(key)
			valuelist.append(value)
		tempindex = []
		for index,val in enumerate(valuelist):
			dot1 = val[0]
			dot2 = val[1]
			if dotvalue:
				if dotvalue == dot1:
					dotvalue = dot2
					tempindex.append(index)
				elif dotvalue == dot2:
					dotvalue == dot1
					tempindex.append(index)
			else:
				dotvalue = dot2
				tempindex.append(index)
		oldestindex = tempindex[0]
		latestindex = tempindex[-1]
		if valuelist[oldestindex][0] == valuelist[latestindex][0] or valuelist[oldestindex][0] == valuelist[latestindex][1] or valuelist[oldestindex][1] == valuelist[latestindex][0] or valuelist[oldestindex][1] == valuelist[latestindex][1]:
			for i in tempindex:
				NewFaceSequence[keylist[i]] = valuelist[i]
		else:
			NewFaceSequence = None#代表给的条件有误
		return NewFaceSequence

class faceproperties:
	def isface(faceside):#判断三维中面是否是闭合	faceside={line1:[[x1,y1],[x2,y2]],line2:[[x1,y1],[x2,y2]]}一定要首尾相接
		result = None
		dotlist = []
		dotagain = []
		for key,value in faceside.items():
			for val in value:
				if val in dotlist:
					dotagain.append(val)
				else:
					dotlist.append(val)
		n1 = list(set(map(tuple, dotlist)))
		n2 = list(set(map(tuple, dotagain)))
		if len(n1) == len(dotlist) and len(n2) == len(dotagain):
			counter1 = Counter(map(tuple, dotlist))
			counter2 = Counter(map(tuple, dotagain))
			if counter1 == counter2:
				result = True
				return result
			else:
				result = False
				return result
		else:
			result = False
			return result

	def face3D(faceside):#判断是凸还是凹
		conclusion_m = None
		result = None
		vectorlist = []
		dot_all = []
		conclusion = {}
		for key,value in faceside.items():
			dotlist = []
			dotlist2 = []
			for val in value:
				dotlist2.append(val)
				dot = np.array(val)
				dotlist.append(dot)
			apex1 = dotlist[0]
			apex2 = dotlist[1]
			vector = apex2 - apex1
			vectorlist.append(vector)
			dot_all.append(dotlist2)
		#取一个点作为基准点判断角是内角or外角
		start = dot_all[0]
		dot_all_1 = []
		direction = []
		vectorder = vectorlist[0]
		apexs = np.array(start[1])
		dtemp = dot_all.pop(0)
		dtemp2 = dot_all.pop(0)
		for f in dot_all:
			apex1 = np.array(f[0])
			apex2 = np.array(f[1])
			vector1 = apex1 - apexs
			vector2 = apex2 - apexs
			cos_1o = np.dot(vector1,vectorder)/(np.linalg.norm(vector1) * np.linalg.norm(vectorder))
			cos_2o = np.dot(vector2,vectorder)/(np.linalg.norm(vector2) * np.linalg.norm(vectorder))
			cos_12 = np.dot(vector1,vector2)/(np.linalg.norm(vector1) * np.linalg.norm(vector2))
			if cos_2o > cos_12 and cos_1o > cos_12:
				result = "IN"
				direction.append(result)
			if cos_12  == cos_2o or cos_1o == cos_12:
				result = "EDGE"
				direction.append(result)
			if cos_12 > cos_2o or cos_12 > cos_1o:
				result = "OUT"
				direction.append(result)
		dot_all_1.append(dtemp)
		dot_all_1.append(dtemp2)
		for tp in dot_all:
			dot_all_1.append(tp)
		for d in direction:
			if d != "OUT":
				conclusion_m = False#该点(第一个点)对应的是内角
				break
			else:
				conclusion_m = True#该点(第一个点)对应的是外角

		sumnum = len(vectorlist)
		cross_all = []
		for i in range(len(vectorlist)):
			if i == (sumnum - 1):
				cross_product = np.cross(vectorlist[i],vectorlist[0])
				cross_all.append(cross_product)
			else:
				cross_product = np.cross(vectorlist[i],vectorlist[i + 1])
				cross_all.append(cross_product)
		num_zero_vectors = 0
		cross_products = []
		cross_all_1 = cross_all
		for i in range(len(cross_all)):
			coslist = []
			ctemp = cross_all_1.pop(0)

			for j in range(len(cross_all_1)):
				cos = np.dot(ctemp,cross_all_1[j])/(np.linalg.norm(ctemp) * np.linalg.norm(cross_all_1[j]))
				coslist.append(cos)
			break
		if conclusion_m:
			keyroot = "dot"
			keylist = list(faceside)
			key1 = keyroot + "1"
			value1 = [start[1],[keylist[0],keylist[1]],conclusion_m]
			conclusion[key1] = value1
			number = 0
			for c in coslist:
				if c < 0:
					keynum = number + 2
					keynum2 = number + 1
					c = 0
					if keynum <= len(dot_all_1):
						key2 = keyroot + str(keynum)
						dotn = dot_all_1[keynum2]
						conclusion[key2] = [dotn[1],[keylist[keynum2],keylist[keynum]],bool(c)]
					else:
						key2 = keyroot + str(keynum)
						dotn = dot_all_1[keynum2]
						conclusion[key2] = [dotn[1],[keylist[keynum2],keylist[0]],bool(c)]
				else:
					keynum = number + 2
					keynum2 = number + 1
					if keynum < len(dot_all_1):
						key2 = keyroot + str(keynum)
						dotn = dot_all_1[keynum2]
						conclusion[key2] = [dotn[1],[keylist[keynum2],keylist[keynum]],bool(c)]
					else:
						key2 = keyroot + str(keynum)
						dotn = dot_all_1[keynum2]
						conclusion[key2] = [dotn[1],[keylist[keynum2],keylist[0]],bool(c)]
						
				number += 1

		else:
			keyroot = "dot"
			keylist = list(faceside)
			key1 = keyroot + "1"
			value1 = [start[1],[keylist[0],keylist[1]],conclusion_m]
			conclusion[key1] = value1
			number = 0
			for c in coslist:
				if c < 0:
					keynum = number + 2
					keynum2 = number + 1
					if keynum <= len(dot_all_1):
						key2 = keyroot + str(keynum)
						dotn = dot_all_1[keynum2]
						conclusion[key2] = [dotn[1],[keylist[keynum2],keylist[keynum]],bool(c)]
					else:
						key2 = keyroot + str(keynum)
						dotn = dot_all_1[keynum2]
						conclusion[key2] = [dotn[1],[keylist[keynum2],keylist[0]],bool(c)]
				else:
					keynum = number + 2
					keynum2 = number + 1
					c = 0
					if keynum < len(dot_all_1):
						key2 = keyroot + str(keynum)
						dotn = dot_all_1[keynum2]
						conclusion[key2] = [dotn[1],[keylist[keynum2],keylist[keynum]],bool(c)]
					else:
						key2 = keyroot + str(keynum)
						dotn = dot_all_1[keynum2]
						conclusion[key2] = [dotn[1],[keylist[keynum2],keylist[0]],bool(c)]
						
				number += 1
		return conclusion

class pointlight:
	def determine2D(der,start,face2D):#der=[x,y];start=[x,y];face2D=[[[x1,y1],[x2,y2],n]]判断光线是否会与线接触
		direction = []
		vectorder = np.array(der)
		apexs = np.array(start)
		for f in face2D:
			apex1 = np.array(f[0])
			apex2 = np.array(f[1])
			vector1 = apex1 - apexs
			vector2 = apex2 - apexs
			cos_1o = np.dot(vector1,vectorder)/(np.linalg.norm(vector1) * np.linalg.norm(vectorder))
			cos_2o = np.dot(vector2,vectorder)/(np.linalg.norm(vector2) * np.linalg.norm(vectorder))
			cos_12 = np.dot(vector1,vector2)/(np.linalg.norm(vector1) * np.linalg.norm(vector2))
			if cos_2o > cos_12 and cos_1o > cos_12:
				result = "IN"
				direction.append(result)
			if cos_12  == cos_2o or cos_1o == cos_12:
				result = "EDGE"
				direction.append(result)
			if cos_12 > cos_2o or cos_12 > cos_1o:
				result = "OUT"
				direction.append(result)
		return direction

	def determine3D(der,start,conclusions,face3D):#	conclusions = [conclison1,conclusion2,……]	face3D = [[[line1],[line2],[line3]],[face2]]判断光线是否会与面接触
		direction = []
		d = np.array(der)
		q = np.array(start)
		number = 0	#计数器
		for f in face3D:
			conclusion = conclusions[number]
			number += 1
			anydot = conclusion.get("dot1")
			p = anydot[0]
			newface = {}
			deldot = {}
			for key,value in conclusion.items():
				if value[-1]:
					newface[key] = value
				else:
					deldot[key] = value
			print(newface)
			if f:
				apex1 = np.array(f[0])
				apex2 = np.array(f[1])
				apex3 = np.array(f[2])
				apex12 = apex1 - apex2
				apex13 = apex1 - apex3
				# 计算面的法向量
				n = np.cross(apex12, apex13)
				print(n)
				print(d)
				print(np.dot(n,d))
				# 判断法向量与方向向量是否垂直
				if np.dot(n, d) == 0:
					result = "NONE"
					direction.append(result)
				else:
					# 计算参数t
					t = np.dot(n, p - q) / np.dot(n, d)
					# 计算交点R
					r = q + t * d
					print("交点R的坐标为：", r)
					newfacedotname = list(newface)
					allline = []
					for i in range(len(newfacedotname)):
						dotdot1 = newface[newfacedotname[i]]
						if i + 1 == len(newfacedotname):
							dotdot2 = newface[newfacedotname[0]]
						else:
							dotdot2 = newface[newfacedotname[i + 1]]
						dotdot1 = dotdot1[0]
						dotdot2 = dotdot2[0]
						dotdot1 = np.array(dotdot1)
						dotdot2 = np.array(dotdot2)
						oneline = [dotdot1,dotdot2]
						allline.append(oneline)
					sdo1 = allline[0][1]
					sdo2 = allline[0][0]
					sdo1 = np.array(sdo1)
					sdo2 = np.array(sdo2)
					sdod = sdo2 - sdo1
					startder = np.array(sdod)
					startder2 = - startder
					startder3 = np.cross(startder,n)
					startder4 = - startder3
					#起点是交点，然后取第一个向量作为方向向量，遍历所有线看有没有交点，之后取反向量，两个正交向量
					vectorders = [startder,startder2,startder3,startder4]
					pool = []
					for vectorder in vectorders:
						dotsum = 0
						for f in allline:
							ap1 = f[0]
							ap2 = f[1]
							vector1 = ap1 - r
							vector2 = ap2 - r
							cos_1o = np.dot(vector1,vectorder)/(np.linalg.norm(vector1) * np.linalg.norm(vectorder))
							cos_2o = np.dot(vector2,vectorder)/(np.linalg.norm(vector2) * np.linalg.norm(vectorder))
							cos_12 = np.dot(vector1,vector2)/(np.linalg.norm(vector1) * np.linalg.norm(vector2))
							if cos_2o > cos_12 and cos_1o > cos_12:
								vectorder1 = - vectorder
								cos_1o = np.dot(vector1,vectorder1)/(np.linalg.norm(vector1) * np.linalg.norm(vectorder1))
								cos_2o = np.dot(vector2,vectorder1)/(np.linalg.norm(vector2) * np.linalg.norm(vectorder1))
								cos_12 = np.dot(vector1,vector2)/(np.linalg.norm(vector1) * np.linalg.norm(vector2))
								if cos_2o > cos_12 and cos_1o > cos_12 and cos_1o > 0 and cos_2o > 0:
									dotsum += 0
								else:
									dotsum += 1
							if cos_12  == cos_2o or cos_1o == cos_12:
								dotsum += 0.5
							if cos_12 > cos_2o or cos_12 > cos_1o:
								dotsum += 0
						if dotsum == 1:
							result = "TRUE"
							pool.append(result)
						else:
							result = "NONE"
							pool.append(result)
					print(pool)
					if "NONE" in pool:
						# print(1)
						result = "NONE"
						direction.append(result)
					else:
						print(deldot)
						if not bool(deldot):
							result = r
							direction.append(result)
							print(direction)
							return direction
						else:
							print(1)
							delline = []
							for i in range(len(newfacedotname)):
								faceone = []
								dotdot1num = int(newfacedotname[i][-1])
								dotdot1 = newface[newfacedotname[i]]
								if i + 1 == len(newfacedotname):#末尾点另外讨论
									dotall = list(conclusion)
									dotallsum = len(dotall)
									dotdot2 = newface[newfacedotname[0]]
									if dotdot1num == dotallsum:
										pass
									else:
										dotdot1 = dotdot1[0]
										dotdot2 = dotdot2[0]
										dotdot1 = np.array(dotdot1)
										dotdot2 = np.array(dotdot2)
										line1 = [dotdot1,dotdot2]
										line1 = np.array(line1)
										faceone.append(line1)
										z = dotallsum - dotdot1num
										for d in range(dotdot1num + 1,dotallsum + 1):
											if d == dotallsum:
												newdotname2 = "dot" + str(0)
												newdotname1 = "dot" + str(d)
												newdot2 = conclusion[newdotname2]
												newdot1 = conclusion[newdotname1]
												newdot2 = newdot2[0]
												newdot1 = newdot1[0]
												newdot2 = np.array(newdot2)
												newdot1 = np.array(newdot1)
												line = [newdot1,newdot2]
												faceone.append(line)
											else:
												newdotname2 = "dot" + str(d)
												newdotname1 = "dot" + str(d - 1)
												newdot2 = conclusion[newdotname2]
												newdot1 = conclusion[newdotname1]
												newdot2 = newdot2[0]
												newdot1 = newdot1[0]
												newdot2 = np.array(newdot2)
												newdot1 = np.array(newdot1)
												line = [newdot1,newdot2]
												faceone.append(line)

								else:
									dotdot2 = newface[newfacedotname[i + 1]]
									dotdot2num = int(newfacedotname[i + 1][-1])
									z = dotdot2num - dotdot1num - 1
									if z > 0:
										dotdot1 = dotdot1[0]
										dotdot2 = dotdot2[0]
										dotdot1 = np.array(dotdot1)
										dotdot2 = np.array(dotdot2)

										line1 = [dotdot1,dotdot2]
										faceone.append(line1)
										for d in range(dotdot1num + 1,dotdot2num + 1):
											newdotname2 = "dot" + str(d)
											newdotname1 = "dot" + str(d - 1)
											newdot2 = conclusion[newdotname2]
											newdot1 = conclusion[newdotname1]
											newdot2 = newdot2[0]
											newdot1 = newdot1[0]
											newdot2 = np.array(newdot2)
											newdot1 = np.array(newdot1)

											line = [newdot1,newdot2]
											faceone.append(line)
										delline.append(faceone)
									else:
										pass
							# print(delline)
							pool = []
							poolall = []
							for vectorder in vectorders:
								for f in delline:
									pool2 = []
									for l in f:
										dotsum = 0
										ap1 = l[0]
										ap2 = l[1]
										vector1 = ap1 - r
										vector2 = ap2 - r
										cos_1o = np.dot(vector1,vectorder)/(np.linalg.norm(vector1) * np.linalg.norm(vectorder))
										cos_2o = np.dot(vector2,vectorder)/(np.linalg.norm(vector2) * np.linalg.norm(vectorder))
										cos_12 = np.dot(vector1,vector2)/(np.linalg.norm(vector1) * np.linalg.norm(vector2))
										if cos_2o > cos_12 and cos_1o > cos_12:
											dotsum += 1
										if cos_12  == cos_2o or cos_1o == cos_12:
											dotsum += 1
										if cos_12 > cos_2o or cos_12 > cos_1o:
											dotsum += 0
										# print(dotsum)
										if dotsum == 1:
											result = "TRUE"
											pool2.append(result)
										else:
											result = "NONE"
											pool2.append(result)
									pool.append(pool2)
								# print(pool)
							poolall.append(pool)
							# print(poolall)
							for p in poolall:
								num = 0
								for pp in p:
									if "TRUE" in pp:
										num += 1
								# print(num)
								if num == len(p):
									result = "NONE"
									direction.append(result)
									print(direction)
									return direction
								else:
									result = r
									direction.append(r)
									return direction
									print(direction)

	def raytrace2D(der,start,face,n_all):#der = np.array()2D情况下光线的路径
		Intersection = []
		for fa in face:
			line2 = fa[0] + fa[1]
			vec2 = np.array(fa[1]) - np.array(fa[0])
			vec2 = list(vec2)
			derl = list(der)
			start2 = [start[0] + derl[0],start[1] + derl[1]]
			line1 = start + start2
			a0, b0, c0 = calc_abc_from_line_2d(*line1)
			a1, b1, c1 = calc_abc_from_line_2d(*line2)
			D = a0 * b1 - a1 * b0
			if D == 0:
				return None
			x = (b0 * c1 - b1 * c0) / D
			y = (a1 * c0 - a0 * c1) / D
			intersection = [x,y]
			Intersection.append(intersection)
		print(Intersection)
		if len(Intersection) == 1:
			n = n_all[0]
			n1 = n[0]
			n2 = n[1]
			vecn1 = [- vec2[1], vec2[0]]
			vecn1 = np.array(vecn1)
			vecn2 = [vec2[1], - vec2[0]]
			vecn2 = np.array(vecn2)
			cos1 = np.dot(vecn1,der)/(np.linalg.norm(vecn1) * np.linalg.norm(der))
			cos2 = np.dot(vecn2,der)/(np.linalg.norm(vecn2) * np.linalg.norm(der))
			if cos1 > 0:
				cross_product = np.cross(der,vecn1)
				magnitude_product = np.linalg.norm(der) * np.linalg.norm(vecn1)
				sin_value = np.abs(cross_product)/magnitude_product
				sin2 = sin_value*n1/n2
				cos2 = abs(math.sqrt(1 - sin2 * sin2))
				if cross_product > 0:#逆时针
					vecn1l = list(vecn1)
					vecn1n1 = [- vecn1l[1],vecn1l[0]]
					vecn1n2 = [vecn1l[1],- vecn1l[0]]
					vecn1n1 = np.array(vecn1n1)
					vecn1n2 = np.array(vecn1n2)
					cross_product1 = np.cross(vecn1,vecn1n1)
					if cross_product1 < 0:
						tan2 = sin2/cos2
						vecn1n1 = list(vecn1n1)
						vecn1n1 = [vecn1n1[0]*tan2,vecn1n1[1]*tan2]
						vecn1n1 = np.array(vecn1n1)
						der2 = vecn1 + vecn1n1
						print(der2)
					else:
						tan2 = sin2/cos2
						vecn1n2 = list(vecn1n2)
						vecn1n2 = [vecn1n2[0]*tan2,vecn1n2[1]*tan2]
						vecn1n2 = np.array(vecn1n2)
						der2 = vecn1 + vecn1n2
						print(der2)
				else:#顺时针
					vecn1l = list(vecn1)
					vecn1n1 = [- vecn1l[1],vecn1l[0]]
					vecn1n2 = [vecn1l[1],- vecn1l[0]]
					vecn1n1 = np.array(vecn1n1)
					vecn1n2 = np.array(vecn1n2)
					cross_product1 = np.cross(vecn1,vecn1n1)
					if cross_product1 > 0:
						tan2 = sin2/cos2
						vecn1n1 = list(vecn1n1)
						vecn1n1 = [vecn1n1[0]*tan2,vecn1n1[1]*tan2]
						vecn1n1 = np.array(vecn1n1)
						der2 = vecn1 + vecn1n1
						print(der2)
					else:
						tan2 = sin2/cos2
						vecn1n2 = list(vecn1n2)
						vecn1n2 = [vecn1n2[0]*tan2,vecn1n2[1]*tan2]
						vecn1n2 = np.array(vecn1n2)
						der2 = vecn1 + vecn1n2
						print(der2)

			else:
				cross_product = np.cross(der,vecn2)
				magnitude_product = np.linalg.norm(der) * np.linalg.norm(vecn2)
				sin_value = np.abs(cross_product)/magnitude_product
				sin2 = sin_value*n1/n2
				cos2 = abs(math.sqrt(1 - sin2 * sin2))
				if cross_product > 0:#逆时针
					vecn1l = list(vecn2)
					vecn1n1 = [- vecn1l[1],vecn1l[0]]
					vecn1n2 = [vecn1l[1],- vecn1l[0]]
					vecn1n1 = np.array(vecn1n1)
					vecn1n2 = np.array(vecn1n2)
					cross_product1 = np.cross(vecn2,vecn1n1)
					if cross_product1 < 0:
						tan2 = sin2/cos2
						vecn1n1 = list(vecn1n1)
						vecn1n1 = [vecn1n1[0]*tan2,vecn1n1[1]*tan2]
						vecn1n1 = np.array(vecn1n1)
						der2 = vecn2 + vecn1n1
						print(der2)
					else:
						tan2 = sin2/cos2
						vecn1n2 = list(vecn1n2)
						vecn1n2 = [vecn1n2[0]*tan2,vecn1n2[1]*tan2]
						vecn1n2 = np.array(vecn1n2)
						der2 = vecn2 + vecn1n2
						print(der2)
				else:#顺时针
					vecn1l = list(vecn2)
					vecn1n1 = [- vecn1l[1],vecn1l[0]]
					vecn1n2 = [vecn1l[1],- vecn1l[0]]
					vecn1n1 = np.array(vecn1n1)
					vecn1n2 = np.array(vecn1n2)
					cross_product1 = np.cross(vecn2,vecn1n1)
					if cross_product1 > 0:
						tan2 = sin2/cos2
						vecn1n1 = list(vecn1n1)
						vecn1n1 = [vecn1n1[0]*tan2,vecn1n1[1]*tan2]
						vecn1n1 = np.array(vecn1n1)
						der2 = vecn2 + vecn1n1
						print(der2)
					else:
						tan2 = sin2/cos2
						vecn1n2 = list(vecn1n2)
						vecn1n2 = [vecn1n2[0]*tan2,vecn1n2[1]*tan2]
						vecn1n2 = np.array(vecn1n2)
						der2 = vecn2 + vecn1n2
						print(der2)
		else:
			num = 0
			minnum = None
			dic = None
			for i in Intersection:
				dx = i[0] - start[0]
				dy = i[1] - start[1]
				s = math.sqrt(dx*dx + dy*dy)
				if not bool(dic):
					dic = s
				if s < dic:
					dic = s
					minnum = num
				num += 1
			print(Intersection[minnum])
			face1 = face[minnum]
			n = n_all[minnum]
			n1 = n[0]
			n2 = n[1]
			vec2 = np.array(face1[1]) - np.array(face1[0])
			vec2 = list(vec2)
			vecn1 = [- vec2[1], vec2[0]]
			vecn1 = np.array(vecn1)
			vecn2 = [vec2[1], - vec2[0]]
			vecn2 = np.array(vecn2)
			cos1 = np.dot(vecn1,der)/(np.linalg.norm(vecn1) * np.linalg.norm(der))
			cos2 = np.dot(vecn2,der)/(np.linalg.norm(vecn2) * np.linalg.norm(der))
			if cos1 > 0:
				cross_product = np.cross(der,vecn1)
				magnitude_product = np.linalg.norm(der) * np.linalg.norm(vecn1)
				sin_value = np.abs(cross_product)/magnitude_product
				sin2 = sin_value*n1/n2
				cos2 = abs(math.sqrt(1 - sin2 * sin2))
				if cross_product > 0:#逆时针
					vecn1l = list(vecn1)
					vecn1n1 = [- vecn1l[1],vecn1l[0]]
					vecn1n2 = [vecn1l[1],- vecn1l[0]]
					vecn1n1 = np.array(vecn1n1)
					vecn1n2 = np.array(vecn1n2)
					cross_product1 = np.cross(vecn1,vecn1n1)
					if cross_product1 < 0:
						tan2 = sin2/cos2
						vecn1n1 = list(vecn1n1)
						vecn1n1 = [vecn1n1[0]*tan2,vecn1n1[1]*tan2]
						vecn1n1 = np.array(vecn1n1)
						der2 = vecn1 + vecn1n1
						print(der2)
					else:
						tan2 = sin2/cos2
						vecn1n2 = list(vecn1n2)
						vecn1n2 = [vecn1n2[0]*tan2,vecn1n2[1]*tan2]
						vecn1n2 = np.array(vecn1n2)
						der2 = vecn1 + vecn1n2
						print(der2)
				else:#顺时针
					vecn1l = list(vecn1)
					vecn1n1 = [- vecn1l[1],vecn1l[0]]
					vecn1n2 = [vecn1l[1],- vecn1l[0]]
					vecn1n1 = np.array(vecn1n1)
					vecn1n2 = np.array(vecn1n2)
					cross_product1 = np.cross(vecn1,vecn1n1)
					if cross_product1 > 0:
						tan2 = sin2/cos2
						vecn1n1 = list(vecn1n1)
						vecn1n1 = [vecn1n1[0]*tan2,vecn1n1[1]*tan2]
						vecn1n1 = np.array(vecn1n1)
						der2 = vecn1 + vecn1n1
						print(der2)
					else:
						tan2 = sin2/cos2
						vecn1n2 = list(vecn1n2)
						vecn1n2 = [vecn1n2[0]*tan2,vecn1n2[1]*tan2]
						vecn1n2 = np.array(vecn1n2)
						der2 = vecn1 + vecn1n2
						print(der2)

			else:
				cross_product = np.cross(der,vecn2)
				magnitude_product = np.linalg.norm(der) * np.linalg.norm(vecn2)
				sin_value = np.abs(cross_product)/magnitude_product
				sin2 = sin_value*n1/n2
				cos2 = abs(math.sqrt(1 - sin2 * sin2))
				if cross_product > 0:#逆时针
					vecn1l = list(vecn2)
					vecn1n1 = [- vecn1l[1],vecn1l[0]]
					vecn1n2 = [vecn1l[1],- vecn1l[0]]
					vecn1n1 = np.array(vecn1n1)
					vecn1n2 = np.array(vecn1n2)
					cross_product1 = np.cross(vecn2,vecn1n1)
					if cross_product1 < 0:
						tan2 = sin2/cos2
						vecn1n1 = list(vecn1n1)
						vecn1n1 = [vecn1n1[0]*tan2,vecn1n1[1]*tan2]
						vecn1n1 = np.array(vecn1n1)
						der2 = vecn2 + vecn1n1
						print(der2)
					else:
						tan2 = sin2/cos2
						vecn1n2 = list(vecn1n2)
						vecn1n2 = [vecn1n2[0]*tan2,vecn1n2[1]*tan2]
						vecn1n2 = np.array(vecn1n2)
						der2 = vecn2 + vecn1n2
						print(der2)
				else:#顺时针
					vecn1l = list(vecn2)
					vecn1n1 = [- vecn1l[1],vecn1l[0]]
					vecn1n2 = [vecn1l[1],- vecn1l[0]]
					vecn1n1 = np.array(vecn1n1)
					vecn1n2 = np.array(vecn1n2)
					cross_product1 = np.cross(vecn2,vecn1n1)
					if cross_product1 > 0:
						tan2 = sin2/cos2
						vecn1n1 = list(vecn1n1)
						vecn1n1 = [vecn1n1[0]*tan2,vecn1n1[1]*tan2]
						vecn1n1 = np.array(vecn1n1)
						der2 = vecn2 + vecn1n1
						print(der2)
					else:
						tan2 = sin2/cos2
						vecn1n2 = list(vecn1n2)
						vecn1n2 = [vecn1n2[0]*tan2,vecn1n2[1]*tan2]
						vecn1n2 = np.array(vecn1n2)
						der2 = vecn2 + vecn1n2
						print(der2)


	def raytrace3D(der,start,Intersection,face3D,n_all):#3D情况下光线的路径
		if len(Intersection) == 1:
			n = n_all[0]
			n1 = n[0]
			n2 = n[1]
			face = face3D[0]
			line1 = np.array(face[0])
			line2 = np.array(face[1])
			linen1 = np.cross(line1,line2)
			linen2 = np.cross(line2,line1)
			cos1 = np.dot(linen1,der)/(np.linalg.norm(linen1) * np.linalg.norm(der))
			cos2 = np.dot(linen2,der)/(np.linalg.norm(linen2) * np.linalg.norm(der))
			if cos1 > 0:
				vecn1 = linen1
				cross_product = np.cross(der,vecn1)
				cross_product_cos = np.dot(der,vecn1)
				magnitude_product = np.linalg.norm(der) * np.linalg.norm(vecn1)
				cos_value = np.abs(cross_product_cos)/magnitude_product
				sin_value = abs(math.sqrt(1 - cos_value * cos_value))
				print(sin_value)
				sin2 = sin_value*n1/n2
				print(sin2)
				cos2 = abs(math.sqrt(sin2 * sin2 - 1))
				if 1:
					vecn1l = list(vecn1)
					vecn1n1 = np.cross(vecn1,cross_product)
					vecn1n2 = np.cross(vecn1,cross_product)
					print(vecn1)
					print(vecn1n1)
					cross_product1 = np.cross(vecn1,vecn1n1)
					print(cross_product1)
					if np.dot(cross_product,cross_product1) < 0:
						tan2 = sin2/cos2
						vecn1n1 = vecn1n1 * tan2
						der2 = vecn1 + vecn1n1
						print(der2)
					else:
						tan2 = sin2/cos2
						vecn1n1 = vecn1n1 * tan2
						der2 = vecn1 + vecn1n2
						print(der2)
			else:
				vecn1 = linen2
				cross_product = np.cross(der,vecn1)
				cross_product_cos = np.dot(der,vecn1)
				magnitude_product = np.linalg.norm(der) * np.linalg.norm(vecn1)
				cos_value = np.abs(cross_product_cos)/magnitude_product
				sin_value = abs(math.sqrt(1 - cos_value * cos_value))
				print(sin_value)
				sin2 = sin_value*n1/n2
				cos2 = abs(math.sqrt(1 - sin2 * sin2))
				if 1:
					vecn1l = list(vecn1)
					vecn1n1 = np.cross(vecn1,cross_product)
					vecn1n2 = np.cross(vecn1,cross_product)
					print(vecn1)
					print(vecn1n1)
					cross_product1 = np.cross(vecn1,vecn1n1)
					print(cross_product1)
					if np.dot(cross_product,cross_product1) < 0:
						tan2 = sin2/cos2
						vecn1n1 = vecn1n1 * tan2
						der2 = vecn1 + vecn1n1
						print(der2)
					else:
						tan2 = sin2/cos2
						vecn1n1 = vecn1n1 * tan2
						der2 = vecn1 + vecn1n2
						print(der2)
		else:
			num = 0
			minnum = None
			dic = None
			for intersection in Intersection:
				start = np.array(start)
				sv = intersection - start
				s = np.linalg.norm(sv)
				if not bool(dic):
					dic = s
				if s < dic:
					dic = s
					minnum = num
				num += 1
			n = n_all[minnum]
			n1 = n[0]
			n2 = n[1]
			face = face3D[minnum]
			line1 = np.array(face[0])
			line2 = np.array(face[1])
			linen1 = np.cross(line1,line2)
			linen2 = np.cross(line2,line1)
			cos1 = np.dot(linen1,der)/(np.linalg.norm(linen1) * np.linalg.norm(der))
			cos2 = np.dot(linen2,der)/(np.linalg.norm(linen2) * np.linalg.norm(der))
			if cos1 > 0:
				vecn1 = linen1
				cross_product = np.cross(der,vecn1)
				cross_product_cos = np.dot(der,vecn1)
				magnitude_product = np.linalg.norm(der) * np.linalg.norm(vecn1)
				cos_value = np.abs(cross_product_cos)/magnitude_product
				sin_value = abs(math.sqrt(1 - cos_value * cos_value))
				print(sin_value)
				sin2 = sin_value*n1/n2
				cos2 = abs(math.sqrt(1 - sin2 * sin2))
				if 1:
					vecn1l = list(vecn1)
					vecn1n1 = np.cross(vecn1,cross_product)
					vecn1n2 = np.cross(vecn1,cross_product)
					print(vecn1)
					print(vecn1n1)
					cross_product1 = np.cross(vecn1,vecn1n1)
					print(cross_product1)
					if np.dot(cross_product,cross_product1) < 0:
						tan2 = sin2/cos2
						vecn1n1 = vecn1n1 * tan2
						der2 = vecn1 + vecn1n1
						print(der2)
					else:
						tan2 = sin2/cos2
						vecn1n1 = vecn1n1 * tan2
						der2 = vecn1 + vecn1n2
						print(der2)
			else:
				vecn1 = linen2
				cross_product = np.cross(der,vecn1)
				cross_product_cos = np.dot(der,vecn1)
				magnitude_product = np.linalg.norm(der) * np.linalg.norm(vecn1)
				cos_value = np.abs(cross_product_cos)/magnitude_product
				sin_value = abs(math.sqrt(1 - cos_value * cos_value))
				print(sin_value)
				sin2 = sin_value*n1/n2
				cos2 = abs(math.sqrt(1 - sin2 * sin2))
				if 1:
					vecn1l = list(vecn1)
					vecn1n1 = np.cross(vecn1,cross_product)
					vecn1n2 = np.cross(vecn1,cross_product)
					print(vecn1)
					print(vecn1n1)
					cross_product1 = np.cross(vecn1,vecn1n1)
					print(cross_product1)
					if np.dot(cross_product,cross_product1) < 0:
						tan2 = sin2/cos2
						vecn1n1 = vecn1n1 * tan2
						der2 = vecn1 + vecn1n1
						print(der2)
					else:
						tan2 = sin2/cos2
						vecn1n1 = vecn1n1 * tan2
						der2 = vecn1 + vecn1n2
						print(der2)

class linelight:
	def raytrace2D():
		pass

	def raytrace3D():
		pass

class facelight:
	def raytrace3D():
		pass

