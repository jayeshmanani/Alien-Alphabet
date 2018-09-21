#Importing the pandas library
import pandas as pd

#Take User input for alphabetical order and string
a= input('Enter the order of alphabet : \n')
b= input('Enter the string you want to sort according to the Alphabet provided : \n')

df = []

#Combining both list to a new list
for i,j in zip(list(a),list(a.upper())):
    df.append(j)
    df.append(i)
#print(df)
a=df

#Converting list to the dataframe
alphabet = pd.DataFrame(index=range(0,len(a)),columns=['letter'])

spell = pd.DataFrame(index=range(0,len(b)),columns=['letter'])

alphabet['letter'] = list(a)
spell['letter'] = list(b)

#Sorting of String according to alphabet as per condition provided
alphabet=pd.merge(alphabet,spell,how='inner')

#Printing the final result
print(''.join(alphabet['letter'].values.tolist()))