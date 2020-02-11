//#include <stdio.h>
//#define N 1000001
//int parents[N] = { 0, };
//void MakeSet(int v) {
//	parents[v] = v;
//}
//
//int FindSet(int v) {
//	if (parents[v] != v)
//		return FindSet(parents[v]);
//	else
//		return v;
//}
//
//int AppendFindSet(int root1, int v)
//{
//	if (parents[v] != v)
//	{
//		int temp = parents[v];
//		parents[v] = root1;
//		return AppendFindSet(root1, temp);
//	}
//	else
//	{
//		parents[v] = root1;
//		return v;
//		}
//	
//}
//void UnionSet(int u, int v) {
//	int root1 = FindSet(v);
//	parents[AppendFindSet(root1,u)] = root1;
//}
//
//void IsSameSet(int u, int v) {
//	int root1 = FindSet(u);
//	int root2 = FindSet(v);
//	if (root1 == root2)
//		printf("YES\n");
//	else 
//		printf("NO\n");
//
//}
//int main(void) {
//	int n, m;
//	scanf("%d %d", &n, &m);
//	for (int v = 0; v <= n; v++)
//		MakeSet(v);
//
//
//	int control, a, b;
//	for (int i = 0; i < m; i++)
//	{
//		scanf("%d %d %d", &control, &a, &b);
//		if (control == 0)
//			UnionSet(a, b);
//
//		else
//			IsSameSet(a, b);
//	}
//	return 0;
//}