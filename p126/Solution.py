class Solution(object):
	def findLadders(self, beginWord, endWord, wordList):
		"""
		:type beginWord: str
		:type endWord: str
		:type wordList: List[str]
		:rtype: List[List[str]]
		"""

		word_len = len(wordList)

		if word_len == 0:
			return []

		wl = len(wordList[0])

		hasEnd = False

		for i in range(word_len):
			if endWord == wordList[i]:
				hasEnd = True

		if hasEnd == False:
			return []


		wordDict = {}
		for i in range(word_len):
			wordDict[wordList[i]] = i

		preWord = {}
		depth = {beginWord: 1}
		queue = [beginWord]
		idx = 0
		maxDepth = 100000000
		route = []
		ans = []

		def combine(current, depth, preWord, maxd):
			if depth == maxd:
				nr = []
				for i in range(maxd-2, -1, -1):
					nr.append(route[i])
				nr.append(endWord)
				ans.append(nr)
				return

			for word in preWord[current]:
				route.append(word)
				combine(word, depth + 1, preWord, maxd)
				route.pop()

		while True:
			if idx == len(queue):
				break

			current = queue[idx]
			currentDeep = depth[current]

			if currentDeep == maxDepth:
				break

			for i in range(wl):
				l = current[:i]
				r = current[i+1:]
				for ch in "abcdefghijklmnopqrstuvwxyz":
					ne = l + ch + r

					if ne not in wordDict:
						continue

					if ne not in preWord:
						preWord[ne] = [current]
						depth[ne] = currentDeep + 1
						queue.append(ne)
					elif ne in preWord and depth[ne] == currentDeep + 1:
						preWord[ne].append(current)
						depth[ne] = currentDeep + 1

					if ne == endWord:
						maxDepth = currentDeep + 1

			idx += 1

		if maxDepth == 100000000:
			return []

		# print (queue)
		combine(endWord, 1, preWord, maxDepth)

		return ans
