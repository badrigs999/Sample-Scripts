/** 
 * A node data structure which  captures the parent, child relationship of the data
 * node is also capable of adding itself to the dom.
 * */
class Node {
    /**
     * constructor which takes in metadata and a parent
     * metadata should have name and type
     * */
    constructor(metadata, parent) {
        this.metadata = metadata;
        this.node_path = `${this.metadata.name}`;
        this.parent = parent;
        this.children = [];
        this.id = Math.floor(Math.random() * 1000);
        if (typeof (parent) !== "undefined") {
            parent.addChild(this);
            this.node_path = `${this.parent.node_path}/${this.node_path}`;
        }
        this.addToDom();
    }
    /**
     * adds a child to this node
    */
    addChild(child) {
        if (typeof (child.parent) === "undefined") child.parent = this;
        this.children.push(child);
        return child;
    }
    /**
     * finds a node with a specific path in the tree
    */
    findNode(value, node) {
        if (typeof (node) === "undefined") node = this;
        if (node.node_path == value) {
            return node;
        } else {
            let return_val = null;
            for (let i = 0; i < node.children.length; i++) {
                return_val = this.findNode(value, node.children[i]);
                if (return_val !== null) return return_val;
            }
            return return_val;
        }
    }
    /**
     * Adds this node to the dom
    */
    addToDom() {
        // check if you are in the dom other wise add 
        // create a li if you're the lone child othewise create a ul and then a li
        if (typeof (this.parent) === "undefined") {
            let n = document.createElement("li");
            n.setAttribute("id", this.id);
            n.innerHTML = this.metadata.name;
            if (this.metadata.type === "folder") {
                n.innerHTML += "/"
            }
            // add to the root of the tree
            document.getElementById("tree").appendChild(n);
        } else {
            let n = document.createElement("ul");
            let nc = document.createElement("li");
            nc.setAttribute("id", this.id);
            nc.innerHTML = this.metadata.name;
            if (this.metadata.type === "folder") {
                nc.innerHTML += "/"
            }
            n.appendChild(nc);
            // add to the parent of this node
            document.getElementById(this.parent.id).appendChild(n)
        }
    }
}

/**
 * Depth first traversal
 * Treverses the graph each level at a time while creating and updating the
 * dom.
 */
function dfs(graph, node, visited, current_parent) {
    if (typeof (graph) === "undefined") return false;
    if (typeof (node) === "undefined") node = graph;
    if (typeof (visited) === "undefined") visited = [];
    // adding a empty array to save failures when a node does not have the 
    // property defined
    if (typeof (node.children) === "undefined") node.children = [];
    // adds a new Node to the tree with this node as the current parent
    let this_node = new Node({ name: node.name, type: node.type }, current_parent);
    // marks the node as visited and adds it to the stack
    // so that its not picked up on next iterations
    node.visited = true;
    visited.push(node);
    // get all the children of this node that are not visited
    const unvisited_nodes = node.children.filter(child_node => {
        return !child_node.hasOwnProperty('visited');
    });
    // for each of the children, recursively do the above while 
    // setting this node as the parent
    for (var i = 0; i < unvisited_nodes.length; i++) {
        dfs(graph, unvisited_nodes[i], visited, this_node);
    }
    return true;
}

/**
 * Breadth first traversal
 * Traverses the graph lazily, visits all the parents first 
 * then queues up future visits to the children and grand_children. 
 */
function bfs(data) {
    // a fifo queue to hold where to visit next
    let queue = [data];
    // a root node to hold the node tree as its built
    let root_node = new Node({ name: ".." });
    while (queue.length) {
        let item = queue.shift();   // removes the first item from the queue
        let p_node = root_node.findNode(get_all_parents(item)); // finds its parent node
        if (p_node) new Node({ name: item.name, type: item.type }, p_node); // adds this node as a child of p_node
        // adding a empty array to save failures when a node does not have the 
        // property defined
        if (!item.hasOwnProperty("children")) item.children = [];
        for (var i = 0; i < item.children.length; i++) {
            let gc = item.children[i];
            // for all the children that we will visit next add this item as the 
            // parent
            gc.parent = item;
            queue.push(gc);
        }
    }
    return root_node;
}

/**
 * a function to walk up the tree and construt a path
 */
function get_all_parents(item, parents) {
    if (typeof (parents) === "undefined") parents = [];
    if (typeof (item.parent) === "undefined") return parents.reverse().join("/");
    parents.push(item.parent.name);
    return get_all_parents(item.parent, parents);
}