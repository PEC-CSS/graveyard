int main()
{
    int N,a,i,j,count=0;
    scanf("%d",&N);
    int A[500];
    for(a=0;a<N;a++)
    {
        scanf("%d",&A[a]);
    }
    for(i=0;i<N;i++)
    {
        for(j=0;j<N;j++)
        {
            if(i!=j)
            {
                if(A[i]==2*A[j])
                {
                    printf("True\n");
                    count++;
                    break;
                }
            }
        }
        if(count==1)
        break;
    }
    if(count==0)
    printf("False\n");
}