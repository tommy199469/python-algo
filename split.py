from random import shuffle
class Solution(object):
    def romanToInt(self):
        group_stage = ['A','B','C' , 'D' , 'E' , 'F' , 'G' , 'H']
        group = {'A' : [],'B': [],'C': [] , 'D' : [], 'E' : [], 'F' : [], 'G': [] , 'H': [] }
        total_list = list(range(32))
        shuffle(total_list)
        i = 0
        for item in total_list:
            stage = group_stage[i]
            if len(group[ stage ] ) == 4:
                i += 1
                stage = group_stage[i]                
            group[stage].append(item+1)

        return group

if __name__ == '__main__':
    result = Solution().romanToInt()   
    print(result)
