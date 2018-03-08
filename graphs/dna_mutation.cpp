/* Given a starting sequence of DNA, an ending sequence, and a list of valid mutations,
    determine if there is valid way to mutate the start sequence into the end sequence
    by changing one character at a time. All intermediate mutations must be in the list
    of valid mutations.

    -Assume that all sequences of DNA have the same length
*/

struct LightGraph {
    unordered_map<string, vector<string>> adjacent;
    
    LightGraph(vector<string> vertices) : adjacent() {
        for (string v : vertices) {
            adjacent[v] = vector<string>();
        }
    }
};

class Solution {
public:
    int minMutation(string start, string end, vector<string>& bank) {
        if (bank.size() == 0) { return -1; }
        
        // Create a graph with all valid mutations and the start (assumed valid)
        vector<string> allV = bank;
        allV.push_back(start);
        
        LightGraph g(allV);
        
        // Add all edges to graph.
        for (string u : allV) {
            for (string v : allV) {
                int hamm_dist = 0;
                for (int i = 0; i < start.length(); i++) {
                    if (u[i] != v[i]) { hamm_dist++; }
                }
                if (hamm_dist == 1) {
                    g.adjacent[u].push_back(v);
                    g.adjacent[v].push_back(u);
                }
            }
        }
        
        // Do BFS
        queue<pair<string, int>> q;
        unordered_set<string> visited;
        q.push(pair<string, int>(start, 0));
        
        while (!q.empty()) {
            pair<string, int> node = q.front();
            q.pop();
            
            if (node.first == end) {
                return node.second;
            }
            
            vector<string> adj = g.adjacent[node.first];
            for (string v : adj) {
                if (visited.find(v) == visited.end()) {
                    visited.insert(v);
                    q.push(pair<string, int>(v, node.second+1));
                }
            }
        }
        return -1;
    }
};