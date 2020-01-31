#include <bits/stdc++.h>
using namespace std;

// 木と根となる頂点を入力とし、根までのパスの集合を返す関数()
vector<set<int>> ne_path(vector<vector<int>> hen, int ne) {
    vector<set<int>> path(hen.size());
    queue<int> tyoten;
    tyoten.push(ne);
    queue<set<int>> s;
    s.push(set<int>({ne}));
    
    while(!tyoten.empty()) {
        int parent = tyoten.front();
        tyoten.pop();
        set<int> p = s.front();
        s.pop();
        path[parent] = p;
        for (int i = 0; i < hen[parent].size(); i++) {
            if (!p.count(hen[parent][i])) {
                set<int> p_c(p);
                tyoten.push(hen[parent][i]);
                p_c.insert(hen[parent][i]);
                s.push(p_c);
            }
        }
    }
    return path;
}

// graphは隣接表現
vector<vector<long long>> warshall_floyd(vector<vector<long long>> graph) {
    for (int k = 0; k < graph.size(); k++){
        for (int i = 0; i < graph.size(); i++) {
            for (int j = 0; j < graph.size(); j++) {
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j]);
            }
        }
    }
    return graph;
}

int main() {
    vector<vector<int>> hen{{1, 2}, {0, 3}, {0}};
    vector<set<int>> path = ne_path(hen, 0);
    for (int i = 0; i < path.size(); i++) {
        for (auto x : path[i]) {
            cout << x << " ";
        }
        cout << endl;
    }
}