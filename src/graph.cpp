#include <iostream>
#include <vector>
#include <string>
#include <map>

// Adjacency Matrix Graph To represent a circuit 
/* 
EX;
Adjacency Matrix:
    AND OR NOT 
AND 0   1   0 
OR  1   0   1 
NOT 0   1   0 
- here a 1 represents an edge (a connection between two gates), and a 0 represents no connection.
// here is a program in C++ to represent a circuit as an undirected graph using an adjacency matrix.
*/

class CircuitGraph {
public:
    CircuitGraph() {}

    // Function to add a gate (node)
    void addNode(const std::string& gate) {
        if (nodeIndex.find(gate) != nodeIndex.end()) {
            std::cout << "Gate " << gate << " already exists!" << std::endl;
            return;
        }
        // Assign index for the new gate
        nodeIndex[gate] = nodes.size();
        nodes.push_back(gate);

        // Add a new row and column in the adjacency matrix (initializing with 0)
        for (auto& row : adjMatrix) {
            row.push_back(0);
        }
        adjMatrix.push_back(std::vector<int>(nodes.size(), 0));
    }

    // Function to remove a gate (node)
    void removeNode(const std::string& gate) {
        auto it = nodeIndex.find(gate);
        if (it == nodeIndex.end()) {
            std::cout << "Gate " << gate << " doesn't exist!" << std::endl;
            return;
        }
        
        // Get the index of the node to remove
        int index = it->second;
        nodeIndex.erase(it);
        
        // Remove the gate from the nodes list
        nodes.erase(nodes.begin() + index);

        // Remove the corresponding row and column from the adjacency matrix
        adjMatrix.erase(adjMatrix.begin() + index);
        for (auto& row : adjMatrix) {
            row.erase(row.begin() + index);
        }

        // Update indices in the map
        for (auto& pair : nodeIndex) {
            if (pair.second > index) {
                pair.second--;  // Shift indices down
            }
        }
    }

    // Function to add an edge (connection) between two gates
    void addEdge(const std::string& gate1, const std::string& gate2) {
        int index1 = getNodeIndex(gate1);
        int index2 = getNodeIndex(gate2);

        // Set both directions since it's an undirected graph
        adjMatrix[index1][index2] = 1;
        adjMatrix[index2][index1] = 1;
    }

    // Function to remove an edge (connection) between two gates
    void removeEdge(const std::string& gate1, const std::string& gate2) {
        int index1 = getNodeIndex(gate1);
        int index2 = getNodeIndex(gate2);

        // Remove both directions
        adjMatrix[index1][index2] = 0;
        adjMatrix[index2][index1] = 0;
    }

    // Function to print the graph as an adjacency matrix
    void printGraph() {
        std::cout << "Adjacency Matrix:\n";
        
        // Print the column headers (gates)
        for (const auto& node : nodes) {
            std::cout << "  " << node << " ";
        }
        std::cout << "\n";

        // Print each row of the adjacency matrix
        for (size_t i = 0; i < adjMatrix.size(); i++) {
            std::cout << nodes[i] << " ";
            for (size_t j = 0; j < adjMatrix[i].size(); j++) {
                std::cout << adjMatrix[i][j] << " ";
            }
            std::cout << "\n";
        }
    }

private:
    std::vector<std::string> nodes;  // List of gate names (nodes)
    std::vector<std::vector<int> > adjMatrix;  // Adjacency matrix (graph representation)
    std::map<std::string, int> nodeIndex;  // Map to get the index of a gate by its name

    // Helper function to get the index of a node by its name
    int getNodeIndex(const std::string& gate) {
        auto it = nodeIndex.find(gate);
        if (it == nodeIndex.end()) {
            std::cout << "Gate " << gate << " doesn't exist!" << std::endl;
            return -1;  // Error value
        }
        return it->second;
    }
};

int main() {
    CircuitGraph circuit;

    // Add gates (nodes)
    circuit.addNode("AND");
    circuit.addNode("OR");
    circuit.addNode("NOT");

    // Add edges (connections between gates)
    circuit.addEdge("AND", "OR");
    circuit.addEdge("OR", "NOT");

    // Print the graph (adjacency matrix)
    circuit.printGraph();

    // Remove an edge and print again
    circuit.removeEdge("AND", "OR");
    std::cout << "\nAfter removing the edge between AND and OR:\n";
    circuit.printGraph();

    // Remove a node and print again
    circuit.removeNode("NOT");
    std::cout << "\nAfter removing the NOT gate:\n";
    circuit.printGraph();

    return 0; // Success
}
