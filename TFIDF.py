import math

list1 = ['딥러닝', '케라스', 'TFIDF', '인공지능']
list2 = ['인공지능', '컴퓨터공학', '자연어처리', 'NLP']
list3 = ['인공지능', '컴퓨터공학', '딥러닝', '신경망']

a = [['딥러닝', '케라스', 'TFIDF', '인공지능'], ['인공지능', '컴퓨터공학', '자연어처리', 'NLP'], ['인공지능', '컴퓨터공학', '딥러닝', '신경망']]


class tfidf():
    def tf(self, list, word):
        result = 0
        for i in list:
            if word == i:
                result = result + 1
        return result / len(list)

    def idf(self, lists, word):
        n = 0
        for list in lists:
            for targetword in list:
                if word == targetword:
                    n = n + 1
                    break
        try:
            return math.log(len(lists) / n)
        except:
            return 0

    def tfidf(self, list, lists, word):
        return self.tf(list, word) * self.idf(lists, word)


tfidf = tfidf()

for word in list1:
    print(str(word) + " - > " + str(tfidf.tfidf(list1, a, word)))