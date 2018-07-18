#include <stdio.h>
int main()
{
    char t;
    printf("Enter a character: ");
    scanf("%c",&t);

    if( (t>='A' && t<='Z') || (t>='a' && t<='z'))
        printf("%c is an alphabet.",t);
    else
        printf("%c is not an alphabet.",t);

    return 0;
}
