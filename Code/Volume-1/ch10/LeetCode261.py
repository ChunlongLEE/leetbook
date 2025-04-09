class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        self.Init(n)
        for i in range(0,len(edges)):
            a=edges[i][0]
            b=edges[i][1]
            if not self.Union(a,b):return False
        cnt=0                   #求子树个数
        for i in range(0,n):
            if self.parent[i]==i: cnt+=1
        return cnt==1
    def Init(self,n):                             #并查集初始化
        self.parent=[0]*n         #并查集存储结构
        self.rnk=[0]*n            #子树的秩(与高度成正比)
        for i in range(0,n):
            self.parent[i]=i
            self.rnk[i]=0
    def Find(self,x):                        #递归算法：并查集中查找x结点的根结点
        if x!=self.parent[x]:
            self.parent[x]=self.Find(self.parent[x])          #路径压缩
        return self.parent[x]
    def Union(self,x,y):                     #并查集中x和y的两个集合的合并
        rx=self.Find(x)
        ry=self.Find(y)
        if rx==ry:                            #x和y属于同一棵树的情况
            return False
        else:
            if self.rnk[rx]<self.rnk[ry]:
                self.parent[rx]=ry                 #rx结点作为ry的孩子
            else:
                if self.rnk[rx]==self.rnk[ry]:           #秩相同，合并后rx的秩增1
                    self.rnk[rx]+=1
                self.parent[ry]=rx                      #ry结点作为rx的孩子
            return True
