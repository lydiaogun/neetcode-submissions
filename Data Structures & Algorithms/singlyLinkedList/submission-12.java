
class Node {
    int val;
    Node next;

    public Node(int val, Node next) {
        this.val = val;
        this.next = next;
    }

    public Node(int val) {
        this(val, null);  // Calls the other constructor with null
    }
}

class LinkedList {
    Node list = null;
    Node tail;

    public LinkedList() {
        // Initialize empty list
    }

    public int get(int index) {
        int i = 0;
        Node current = list;

        while (current != null) {
            if (i == index) {
                return current.val;  // Return the value at the given index
            }
            i++;
            current = current.next;
        }
        return -1;  // Index out of bounds
    }

    public void insertHead(int val) {
        Node newNode = new Node(val);
        newNode.next = list;
        list = newNode;
    }

    public void insertTail(int val) {
        Node newNode = new Node(val);
        if (list == null) {  // If the list is empty, make the new node the head
            list = newNode;
            tail = newNode;
        } else {
            Node currentNode = list;
            while (currentNode.next != null) {
                currentNode = currentNode.next;
            }
            currentNode.next = newNode;  // Attach new node at the end
            tail = newNode;  // Update the tail pointer
        }
    }

    public boolean remove(int index) {
        int i = 0;
        Node current = list;

        // Special case: Removing the head node
        if (index == 0 && current != null) {
            list = current.next;  // Move head to the next node
            if (list == null) {  // If the list is now empty, update tail to null
                tail = null;
            }
            return true;
        }

        // Traverse the list to find the node before the one to remove
        while (current != null && current.next != null) {
            if (i == index - 1) {
                // Skip the node at the given index
                current.next = current.next.next;

                // If we removed the last node, update the tail
                if (current.next == null) {
                    tail = current;
                }
                return true;
            }
            i++;
            current = current.next;
        }

        return false;  // Index out of bounds or empty list
    }

    public ArrayList<Integer> getValues() {
        ArrayList<Integer> res = new ArrayList<>();
        Node curr = this.list;
        while (curr != null) {
            res.add(curr.val);
            curr = curr.next;
        }
        return res;
    }
}
