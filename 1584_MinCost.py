class Solution:
    def minCostConnectPoints(self, points) -> int:
        Num_nodes=len(points)
        if Num_nodes < 2:
            return 0
        NumofEdge=0
        result=0
        uf = UnionFind(Num_nodes)
        edge_val = []
        for i in range (0,Num_nodes):
            for j in range (i+1, Num_nodes):
             edge_val.append([i,j,(abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]))])
        edge_val=sorted(edge_val, key=lambda x: x[2])
        
        for i in range (len(edge_val)):
            if NumofEdge==Num_nodes-1:
                break
            if not uf.Isconnected(edge_val[i][0],edge_val[i][1]):
                uf.union(edge_val[i][0],edge_val[i][1])
                NumofEdge=NumofEdge+1
                result=result+edge_val[i][2]
        return result
                
           
class UnionFind:
    def __init__(self,size):
        self.root = [i for i in range (size)]
        self.rank = [1]* size
    
    def find (self, x):
        while x != self.root[x]:
            x= self.root[x]
        return x
    
    def union (self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX]> self.rank[rootY]:
                self.root[rootY]=rootX
            elif self.rank[rootY]> self.rank[rootX]:
                self.root[rootX]=rootY
            else:
                self.root[rootY]=rootX
                self.rank[rootX]=self.rank[rootX]+1

    def Isconnected(self, x,y):
        if self.find(x)==self.find(y):
            return True
        else:
            return False