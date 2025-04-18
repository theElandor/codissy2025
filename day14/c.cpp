#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;
void d_vector(vector<int> &v){
  for(int i=0; i < v.size(); i++){
	cout<<v[i]<<" ";
  }
  cout<<endl;
}
void d_mat(vector<vector<int>> &dp){
  for(int i = 0; i < dp.size(); i++){
	d_vector(dp[i]);
	cout<<endl;
  }
}
void print_map(map<string, vector<int>> &m){
  for(auto &p:m){
	cout<<p.first<<" ";
	d_vector(p.second);
  }
}
int main(int argc, char** argv){
  int line, v;
  string id;
  string temp;
  map<string, vector<int>> m;
  while(true){
	vector<int> vals;
    cin>>line;
	cin.ignore();
	cin>> id;
	for(int i =0; i < 3; i++){
	  getline(cin, temp, ':');
	  cin>>v;
	  vals.push_back(v);
	}
	m[id] = vals;
	if (cin.peek() == EOF){break;}
  }
  int cols = 30;
  int rows = m.size();
  vector<vector<int>> dp(rows+1, vector<int>(cols+1, 0));
  vector<vector<int>> items;
  for(auto &p:m){
	vector<int> temp;
	temp.push_back(p.second[1]); // cost
	temp.push_back(p.second[0]); // quality
	items.push_back(temp);
  }
  sort(items.begin(), items.end());
  for(int i = 0; i < items.size(); i++){
	d_vector(items[i]);
	cout<<endl;
  }
  for(int i = 1; i <= rows; i++){
	int c_qual = items[i-1][1];
	int c_cost = items[i-1][0];	
	for(int j = 1; j <= cols; j++){
	  if(j < c_cost){
		dp[i][j] = dp[i-1][j];
	  }
	  else{
		dp[i][j] = max(c_qual + dp[i-1][j-c_cost], dp[i-1][j]); 
	  }
		
	}
  }
  cout<<dp[rows][cols]<<endl;
  //  d_mat(dp);
  return 0;
}
