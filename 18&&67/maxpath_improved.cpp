/*
http://projecteuler.net/problem=18 && 67
Maximum path sum I
Maximum path sum II
by Alexandre Pinto
*/

#include <stdio.h>
#include <algorithm>

#define MAX 100

using namespace std;

int N;
int triangle[MAX][MAX];

int search();

int main(){

	int i,j,nlines=1;

	/*receive input*/
	scanf("%d",&N);
	for(i=0;i<N;i++){
		for(j=0;j<nlines;j++)
			scanf("%d",&triangle[i][j]);	
		nlines++;
	}
	printf("%d\n",search());

	return 0;
}

int search(){

	int i,j;
	for(i=N-2;i>=0;i--){
		for(j=0;j<=i;j++){
			triangle[i][j]+=max(triangle[i+1][j],triangle[i+1][j+1]);		/*bottom-up dynamic programming*/
		}
	}
	return triangle[0][0];
}
