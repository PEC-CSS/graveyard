int main()
{
    int N,a,i,j,count=0;
    printf("Enter N=");
    scanf("%d",&N);
    if(2<=N<=500)
    {
        int A[500];
        for(a=0;a<N;a++)
        {
            printf("Enter Value at A[%d]=",a);
            scanf("%d",&A[a]);
            if(A[a]<=103 & A[a]>=-103)
            i++;
            else
            {
                printf("Invalid Input");
                exit(0);
            }
        }
        for(i=0;i<N;i++)
        {
            for(j=0;j<N;j++)
            {
                if(i!=j)
                {
                    if(A[i]==2*A[j])
                    {
                        printf("True");
                        count++;
                        break;
                    }
                }
            }
            if(count==1)
            break;
        }
        if(count==0)
        printf("False");

    }
    else
    {
        printf("Invalid Value of N");
    }
}