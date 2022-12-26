class Node:
    def __init__(self, data=None, next_node= None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None


    def print_ll(self):
        ll_string = ""
        node = self.head
        if node is None:
            print(None)
        while node:
            ll_string += f"{str(node.data)}->"

            node = node.next_node

        ll_string += "None"            
        print(ll_string)


    def insert_beginning(self, data):
        if self.head is None:        
            new_node = Node(data, self.head)
            self.head = new_node
        
            self.last_node = new_node
            
        new_node = Node(data, self.head)
        self.head = new_node

    def insert_at_end(self, data):
        if self.head is None:
            self.insert_beginning(data)
        # if self.last_node is None:
        #     print("Last Node is None")
            # node = self.head
            # while node.next_node:
            #     node = node.next_node
            # node.next_node = Node(data,None)
            # self.last_node= node.next_node

        # else:
        self.last_node.next_node = Node(data, None)
        self.last_node = self.last_node.next_node

    def to_array(self):
        arr = []
        if self.head is None:
            return arr
    
        node = self.head

        while node:
            arr.append(node.data)
            node = node.next_node
        return arr

    def get_user_by_id(self,id):
        node = self.head
        while node:
            if node.data["id"] == id:
                return node.data
            node = node.next_node
        return None


# ll = LinkedList()
# node5 = Node("data5", None)
# node4 = Node("data4", node5)
# node3 = Node("data3", node4)
# node2 = Node("data2", node3)
# node1 = Node("data", node2)


# ll.head = node1
# ll.insert_beginning("test")
# ll.insert_at_end("final")
# print(ll.print_ll())
# ll.insert_at_end("rest")
# print(ll.print_ll())



