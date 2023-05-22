#include "stdio.h"
#include "string.h"
typedef struct
{
char name[8];
int parent; 
}PTreeNode;
typedef struct
{
PTreeNode nodes[100];
int n;
}PTree; 
PTree people;
void createTree()
{
	int i;
	printf("请输入家谱总人数:");
	scanf("%d", &people.n);
	for (i - 0; i < people.n; i++)
	{
		printf("请输入姓名和父亲编号:");
		scanf("%s%d", people.nodes[i].name, &people.nodes[i].parent);
	}
}
void Parent()
{
char nam[8];
int parent, i;
printf("请输入要查找的人员姓名（查找此人的父亲):");
getchar();
gets(nam);
for (i = 0; i < people.n; i++)
{
	if (strcmp(people.nodes[i].name, nam) == 0)
	{
		parent = people.nodes[i].parent;
		if (parent == -1)
		{
			printf("此人为最高辈分！\n");
			break;
		}
		printf("此人的父亲为:M%s\n", people.nodes[parent].name);
		break;
	}
	if (i == people.n)
		printf("没有此人!n");

}
void Child()
{
	char nam[8];
	int parent, i, j, tag = 0;
	printf("请输入要查找的人员姓名（查找此人的孩子):");
	gets(nam);
	for (i = 0; i < people.n; i++)
	{
		if (strcmp(people.nodes[i].name, nam) == 0"
		{
			parent = i;
				for (j = i + l; j < people.n; j++)
				{
					if (people.nodes[j].parent -0
					{
						printf("此人的孩子为：%s \n", people.nodes[j].name)
							tag = 1;
					}
				}
			if (tag -= 0)
				printf("此人没有孩子！n");
				break;
		}
	}
	if (i == people.n)
		printf("没有此人!n");
}
main()
{
	createTree();
	Parent();
	Child();
}
