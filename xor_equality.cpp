#include <iostream>
using namespace std;
int pwd( int n){
   int ans=1;
    for(auto i =0; i<n;i++)
    {
        ans = (ans * 2)%1000000007;
    }
    return ans;
    
}
int main() {
	int t,n,ans;
	scanf("%d",&t);
	for(int i=0;i<t;i++)
	{
	    scanf("%d",&n);
	    ans=pwd(n-1);
	    printf("%d\n",ans);
	}
	return 0;
}

#include <stdio.h>
int main() {
	int t,n;
	scanf("%d",&t);
	while(t--)
	{   int ans=1;
	    scanf("%d",&n);
	 for(;n-1;n--)
    {
        ans = (ans * 2)%1000000007;
    }
	    printf("%d\n",ans);
	}
	return 0;
}

