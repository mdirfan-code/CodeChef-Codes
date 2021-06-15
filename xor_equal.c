#include <stdio.h>
int main() {
	int t,n,k,l;
	scanf("%d",&t);
	while(t--)
	{   unsigned int ans=1;
	    l=2;
	    scanf("%d",&n);
        n-=1;
	    if(n>2)
        {l=4;
        k = n%2;
        n=(int)(n/2);
        ans+=k;
        }
        printf("%d  %d  %d\n",n,ans,k);
	 for(;n;n--)
    {
        ans = (ans * l)%1000000007;
    }
	    printf("%d\n",ans);
	}
	return 0;
}