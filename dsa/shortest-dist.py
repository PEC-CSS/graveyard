class Solution:
    def closetTarget(self, words: list[str], target: str, startIndex: int) -> int:
        
        
        n = len(words)
        count_1 = 0
        count_2 = 0
        m = startIndex
        
        if target not in words:
            return -1

        else:

            original_start_index = 0
            for word in words:
                target_index = words.index(target)
                if startIndex+1 < n:
                    nextword = words[startIndex+1]
                    count_1 += 1

                    if nextword == words[target_index]:
                        break

                    startIndex += 1

                if startIndex+1 == n:
                    nextword = words[original_start_index]
                    count_1 +=1

                    if nextword == words[target_index]:
                        break

                    original_start_index += 1

            target_index = words.index(target) 
            startIndex = m
            for word_2 in words:
                original_start_index_2 = len(words)
                target_index = words.index(target)
                
                if startIndex - 1 >= 0:
                    prevword = words[startIndex-1]
                    count_2 += 1

                    if prevword == words[target_index]:
                        break

                    startIndex -= 1
                if startIndex-1 < 0:
                    prevword = words[original_start_index_2-1]
                    count_2 += 1
                    
                    if prevword == words[target_index]:
                        break

                    original_start_index_2 -= 1

            if count_1 > count_2:
                shortest_dist = count_2
            else:
                shortest_dist = count_1

            return shortest_dist