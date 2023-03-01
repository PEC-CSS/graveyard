#include <iostream>
using namespace std;
class Graph{
    int V;
    int E;
    int source;
    int destination;
    bool **adjMatrix; //Adjacency Matrix
    public:
        Graph *createGraph(int V);
        void newEdge(Graph*e,int x, int y);
        void insertEdge(Graph *G,int x,int y);
        void findPath(Graph *G, int visited[],int start);
};
Graph *Graph::createGraph(int V){
    Graph *root;
    root = new Graph;
    root->V=V-1;
    root->E=0;
    root->adjMatrix = new bool*[V];
    for(int i=0; i<V; i++){
        root->adjMatrix[i]=new bool[V];
    }
    for(int i=0; i<V; i++){
        for(int j=0; j<V; j++){
            root->adjMatrix[i][j]=0;
        }
    }
    return root;
}
void Graph::newEdge(Graph *e,int x, int y){
    e->source=x;
    e->destination=y;
}
void Graph::insertEdge(Graph *G,int x,int y){
    newEdge(G,x,y);
    int v = G->V+1;
    int a,b;
    a=G->source;
    b=G->destination;
    if(a>v || b>v){
        cout<<"Error in inserting the edge";
    }
    else{
        if (G->adjMatrix[a][b]==0){
            G->adjMatrix[a][b]=1;
            G->adjMatrix[b][a]=1;
            G->E+=1;
        }
    }
}
void Graph::findPath(Graph *G, int visited[],int start){
    visited[start] = 1;
    for (int i=0; i<G->V+1; i++){
        if (G->adjMatrix[start][i]==1 && visited[i]==0){
            findPath(G,visited,i);
        }
    }
}
int main(){
    Graph G, *root;
    int N,source,dest,edge;
    cin>>N;
    root=G.createGraph(N);
    cout<<"Enter number of edges";
    cin>>edge;
    int edges[edge][2];
    for(int i=0; i<edge; i++){
        for (int j=0; j<2; j++){
            cin>>edges[i][j];
        }
    }
    cin>>source;
    cin>>dest;
    int rowsize = sizeof(edges)/sizeof(edges[0]);
    for (int i=0; i<rowsize; i++){
        G.insertEdge(root,edges[i][0],edges[i][1]);
    }
    int visited[N];
    for (int i=0; i<N; i++){
        visited[i]=0;
    }
    G.findPath(root,visited,source);
    if (visited[dest]){
        cout<<"true";
    }
    else{
        cout<<"false";
    } 
    return 0;
}