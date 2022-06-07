class Node: 
    def __init__(self, key): 
        self.key = key
        self.left = None
        self.right = None
         
def find_sum(root): 
    if (root == None):
        return 0
    return (root.key + find_sum(root.left) + find_sum(root.right)) 
 
if __name__ == '__main__':
    root = Node(2) 
    root.left = Node(3) 
    root.right = Node(4) 
    root.left.left = Node(5) 
    root.left.right = Node(6) 
    print("Soma de todos nos:", find_sum(root))