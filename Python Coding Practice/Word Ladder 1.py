from collections import deque
class Solution:
	def wordLadderLength(self, startWord, targetWord, wordList):
		Q = deque([(startWord, 1)])
		wordList = set(wordList)
		wordList.discard(startWord)
		
		while Q:
		    word, step = Q.popleft()
		    if word == targetWord:
		        return step
		        
		    for i in range(len(word)):
		        for ch in ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]:
		            replaced_word = word[:i] + ch + word[i+1:]
		            
		            if replaced_word in wordList:
		                Q.append((replaced_word, step+1))
		                wordList.discard(replaced_word)
		return 0 


#{ 
 # Driver Code Starts
# from collections import deque 
if __name__ == '__main__':
	T=int(input())
	for tt in range(T):
		n = int(input())
		wordList = []
		for i in range(n):
			wordList.append(input().strip())
		startWord = input().strip()
		targetWord = input().strip()
		obj = Solution()
		ans = obj.wordLadderLength(startWord, targetWord, wordList)
		print(ans)

# } Driver Code Ends
