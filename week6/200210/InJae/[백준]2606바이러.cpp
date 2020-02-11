//#include <stdio.h>
//#define N 101
//
//int parents[N] = { 0, };
//
//int FindSet(int v) {
//	if (parents[v]>=0)
//		return FindSet(parents[v]);
//	return v;
//}
//
//void UnionSet(int u, int v) {
//	int root1 = FindSet(u);
//	int root2 = FindSet(v);
//
//	if (root1 == root2) return;
//	parents[root2] += parents[root1];
//	parents[root1] = root2;
//	return;
//}
//
//int GetSetSize(int v) {
//	return -parents[FindSet(v)];
//}
//
//int main(void) {
//	for (int i = 0; i < N; i++)//1번부터 번호가 매겨지므로 101개
//		parents[i] = -1;
//	
//	int comNum,cnt; 
//	scanf("%d", &comNum);
//	scanf("%d", &cnt);
//
//	int u, v;
//	for (int i = 0; i < cnt; i++)
//	{	
//		scanf("%d %d", &u, &v);
//		UnionSet(u, v);
//	}
//
//	printf("%d\n", GetSetSize(1)-1);
//}