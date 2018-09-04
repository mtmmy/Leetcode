package com.leetcode._0133_CloneGraph;

import com.leetcode.utils.UndirectedGraphNode;

import java.util.Deque;
import java.util.HashMap;
import java.util.LinkedList;

public class CloneGraph {
    HashMap<Integer, UndirectedGraphNode> nodeMap = new HashMap<>();
    public UndirectedGraphNode solution(UndirectedGraphNode node) {
        return clone(node);
    }

    public UndirectedGraphNode clone(UndirectedGraphNode node) {
        if (node == null) {
            return node;
        }
        if (nodeMap.containsKey(node.label)) {
            return nodeMap.get(node.label);
        }
        UndirectedGraphNode newNode = new UndirectedGraphNode(node.label);
        nodeMap.put(newNode.label, newNode);
        for (UndirectedGraphNode neighbor : node.neighbors) {
            newNode.neighbors.add(clone(neighbor));
        }
        return newNode;
    }

    public UndirectedGraphNode bfsSolution(UndirectedGraphNode node) {
        if (node == null) {
            return null;
        }

        HashMap<Integer, UndirectedGraphNode> bfsNodeMap = new HashMap<>();
        UndirectedGraphNode newNode = new UndirectedGraphNode(node.label);

        bfsNodeMap.put(newNode.label, newNode);
        Deque<UndirectedGraphNode> queue = new LinkedList<>();
        queue.push(node);

        while (!queue.isEmpty()) {
            UndirectedGraphNode oldNode = queue.pollFirst();
            for (UndirectedGraphNode neighbor : oldNode.neighbors) {
                if (!bfsNodeMap.containsKey(neighbor.label)) {
                    bfsNodeMap.put(neighbor.label, new UndirectedGraphNode(neighbor.label));
                    queue.push(neighbor);
                }
                bfsNodeMap.get(oldNode.label).neighbors.add(bfsNodeMap.get(neighbor.label));
            }

        }
        return newNode;

//        if (node == null) return null;
//
//        UndirectedGraphNode newNode = new UndirectedGraphNode(node.label); //new node for return
//        HashMap<Integer, UndirectedGraphNode> map = new HashMap(); //store visited nodes
//
//        map.put(newNode.label, newNode); //add first node to HashMap
//
//        LinkedList<UndirectedGraphNode> queue = new LinkedList(); //to store **original** nodes need to be visited
//        queue.add(node); //add first **original** node to queue
//
//        while (!queue.isEmpty()) { //if more nodes need to be visited
//            UndirectedGraphNode n = queue.pop(); //search first node in the queue
//            for (UndirectedGraphNode neighbor : n.neighbors) {
//                if (!map.containsKey(neighbor.label)) { //add to map and queue if this node hasn't been searched before
//                    map.put(neighbor.label, new UndirectedGraphNode(neighbor.label));
//                    queue.add(neighbor);
//                }
//                map.get(n.label).neighbors.add(map.get(neighbor.label)); //add neighbor to new created nodes
//            }
//        }
//
//        return newNode;
    }
}
