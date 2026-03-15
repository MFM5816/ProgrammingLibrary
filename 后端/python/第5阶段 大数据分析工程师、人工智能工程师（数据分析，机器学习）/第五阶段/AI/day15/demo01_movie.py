"""
demo01_movie.py  电影推荐
"""
import numpy as np
import json

with open('../ml_data/ratings.json', 'r') as f:
	ratings = json.loads(f.read())
users = list(ratings.keys())
# 生成得分矩阵
scmat = []
for user1 in users:
	scrow = []
	for user2 in users:
		# user1与user2共同看过的电影
		movies = set()
		for movie in ratings[user1].keys():
			if movie in ratings[user2].keys():
				movies.add(movie)
		if len(movies) == 0:
			score = 0 # 两人没有共同语言
		else:
			# 计算两人相似度得分
			x, y = [], []
			for movie in movies:
				x.append(ratings[user1][movie])
				y.append(ratings[user2][movie])
			# 计算欧氏距离得分
			x = np.array(x)
			y = np.array(y)
			# score = \
			# 	1 / (1 + np.sqrt(((x-y)**2).sum()))
			score = np.corrcoef(x, y)[0, 1]
		scrow.append(score)
	scmat.append(scrow)
scmat = np.array(scmat)
print(np.round(scmat, 2)) # 输出相似度矩阵

# 针对每个用户给出推荐列表
users = np.array(users)
for i, user in enumerate(users):
	#找到所有相似用户,按照相似度倒序排列
	sorted_indices = scmat[i].argsort()[::-1]
	sorted_indices = \
		sorted_indices[sorted_indices != i]
	# 相似用户列表
	sim_users = users[sorted_indices]
	# 相似用户的相似度得分列表
	sim_scores = scmat[i][sorted_indices]
	# 找到皮尔逊系数正相关的用户
	pos_mask = sim_scores > 0
	sim_users = sim_users[pos_mask]
	# 遍历所有相似用户
	rec_movies = {}
	for sim_user in sim_users:
		# 看一下相似用户都看过什么电影
		for movie,score in ratings[sim_user].items():
			# 找到当前用户没看过的电影
			if movie not in ratings[user].keys():
				# 找到了一部可以推荐的电影，存起来
				if movie not in rec_movies.keys():
					rec_movies[movie] = [score]
				else:
					rec_movies[movie].append(score)

	print(user)
	# print(rec_movies)
	# 按照电影评分的均值进行排序
	mlist = sorted(rec_movies.items(), 
		key=lambda x: np.average(x[1]), reverse=True)
	print(mlist)




