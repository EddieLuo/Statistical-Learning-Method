import math
def getMedianInL(list,l):
    def sortasN(list):
        return list[l]
    list.sort(key=sortasN)
    median = len(list)//2
    medianco = list[median]
    return median,medianco

def dist(X,Y):
    sum = 0
    for i in range(len(X)):
        sum+=(X[i]-Y[i])**2
    return math.sqrt(sum)

class KdNode:
    def __init__(self,coordinate,k,depth):
        self.left = None
        self.right = None
        self.coordinate = coordinate
        self.parent = None
        self.k = k
        self.depth = depth

def buildTree(coorlist,k,Startdepth):
    if len(coorlist)>0:
        headNode = KdNode(None,k,Startdepth)
        splitD = headNode.depth%k
        median0,medianco0 = getMedianInL(coorlist,splitD)
        headNode.coordinate = medianco0
        Startdepth+=1
        headNode.left = buildTree(coorlist[:median0],k,Startdepth)
        headNode.right = buildTree(coorlist[median0+1:],k,Startdepth)
        if headNode.left!=None:
            headNode.left.parent = headNode
        if headNode.right!=None:
            headNode.right.parent = headNode
        return headNode
    else:
        return None

def search(tar_point,kdtree):
    def travel(tar_point,kdtree):
        if kdtree == None:
            return None
        else:
            nearest = kdtree
            cur_depth = nearest.depth
            splitD = cur_depth%nearest.k
            if tar_point[splitD] < nearest.coordinate[splitD]:
                if nearest.left != None:
                    nearest = nearest.left
                    return travel(tar_point,nearest)
                else:
                    return nearest
            else:
                if nearest.right != None:
                    nearest = nearest.right
                    return travel(tar_point,nearest)
                else:
                    return nearest
    nearest_node = travel(tar_point,kdtree)
    cur_node = nearest_node
    while cur_node!=kdtree:
        cur_dist = dist(tar_point,cur_node.coordinate)
        cur_father = cur_node.parent
        if cur_node == cur_father.left:
            cur_cousin = cur_father.right
        else:
            cur_cousin = cur_father.left
        father_depth = cur_father.depth
        father_splitD = father_depth%cur_father.k
        if cur_dist > dist(cur_father.coordinate,tar_point):
            nearest_node = cur_father
        if cur_cousin!=None:
            if cur_dist > abs(cur_father.coordinate[father_splitD]-tar_point[father_splitD]):
                cousin_near = search(tar_point,cur_cousin)
                if dist(tar_point,nearest_node.coordinate) > dist(cousin_near.coordinate,tar_point):
                    nearest_node = cousin_near
        cur_node = cur_father
    return nearest_node
x = [[2,3],[5,4],[9,6],[4,7],[8,1],[7,2]]
root= buildTree(x,2,0)
search([5,5],root).coordinate
