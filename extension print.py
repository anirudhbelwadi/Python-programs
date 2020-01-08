file=input("Enter file name with extension : ");
for i in range(len(file)):
    if file[i]==".":
        index=i;
print("Extension  : "+file[index+1:]);

