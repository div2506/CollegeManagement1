#include<stdio.h>
#define N 4
main()
{
	int a[N][N]={0};
	int i,j,k=1,l;

		
			for(j=0;j<N;j++)
			{
				a[0][j]=k;
				k=k+1+j;			
			}
		
		for(i=0;i<N;i++)
		{
			k=a[0][i]+i+2;
			for(j=1;j<N;j++)
			{
				a[j][i]=k;
				k=k+j+2;
			}
			
			
			k++;
		}
		
	
	
	for(i=0;i<N;i++)
	{
		for(j=0;j<5;j++)
		{
			printf("%d ",a[i][j]);
		}
		printf("\n");
	}

}
