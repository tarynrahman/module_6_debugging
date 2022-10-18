#!/usr/bin/env python
# coding: utf-8

# In[48]:


#One A
def wrong_add_function(arg1,arg2):
    arg1_index=0
    while arg1_index < len(arg1):
        arg_2_sum = 0
        for arg2_elements in arg2:
            arg_2_sum = sum([arg1[arg1_index]+i for i in arg2])
            print(f"we are making an error in the loop: {arg_2_sum}") #place print statement closest to point of error
        arg1[arg1_index]=arg_2_sum
        arg1_index+=1
    return arg1

arg1 = [1,2,3]
arg2 = [1,1,1]

correct_ans = [2,3,4]
print(f"The correct answer should be {correct_ans}") #print statement to represent what correct answer should be 

wrong_add_function(arg1, arg2)


# In[50]:


#One B
def correct_add_function(arg1,arg2):
    arg1_index=0
    while arg1_index < len(arg1):
        for arg2_elements in arg2:
            arg_2_sum = [arg1[arg1_index]+ i for i in arg2] #removing "sum" allows output of [2,2,2], [3,3,3], [4,4,4]
                                                            #therefore next edit should allow single index from each list
        arg1[arg1_index]=arg_2_sum[1]
        arg1_index+=1
    return arg1

arg1 = [1,2,3]
arg2 = [1,1,1]

correct_add_function(arg1, arg2)


# In[72]:


#two a - update numeric section of the code in order to use for two b and two c 

def wrong_add_function(arg1,arg2):
#numeric section
    if sum([type(i)==int for i in arg1])==len(arg1) and sum([type(i)==int for i in arg2])==len(arg2):
        arg1_index=0
        while arg1_index < len(arg1):
            arg_2_sum = 0
            for arg2_elements in arg2:
                arg_2_sum = arg1[arg1_index]+ sum(arg2) #sum(arg2) allows that the sum of all elements in arg 2 is added to each element in arg1
            arg1[arg1_index]=arg_2_sum  
            arg1_index+=1
        return arg1
#string section
    elif sum([type(i)==str for i in arg1])==len(arg1) and sum([type(i)==str for i in arg2])==len(arg2):
        arg1_index=0
        while arg1_index < len(arg1):
            arg_2_sum = ''
            for arg2_elements in arg2:
                arg_2_sum += arg2_elements
            arg1[arg1_index]=arg1[arg1_index]+str(arg_2_sum)
            arg1_index+=1
        return arg1
arg1 = [1, 2, 3]
arg2 = [1, 1, 1]
arg_str_1=['1','2','3']
arg_str_2=['1','1', '1']
print(wrong_add_function(arg1, arg2))
print(wrong_add_function(arg_str_1,arg_str_2))


# In[73]:


#two b

def exception_add_function(arg1,arg2):
#numeric section
    if sum([type(i)==int for i in arg1])==len(arg1) and sum([type(i)==int for i in arg2])==len(arg2):
        arg1_index=0
        while arg1_index < len(arg1):
            arg_2_sum = 0
            for arg2_elements in arg2:
                arg_2_sum = arg1[arg1_index]+ sum(arg2)
            arg1[arg1_index]=arg_2_sum  
            arg1_index+=1
        return arg1
#string section
    try:
        arg1_index=0
        while arg1_index < len(arg1):
            arg_2_sum = ''
            for arg2_elements in arg2:
                arg_2_sum += arg2_elements
            arg1[arg1_index]=arg1[arg1_index]+str(arg_2_sum)
            arg1_index+=1
        return arg1
    
    except TypeError:      
        mylist1 = []
        for i in arg1:
            if type(i) != str: 
                mylist1.append(i) #if the element in arg1 is not a string, then it appends to mylist1
            else:
                pass        
        mylist2 = []
        for i in arg2:
            if type(i) != str:
                mylist2.append(i) #if the element in arg1 is not a string, then it appends to mylist2
            else:
                pass
        
        print(f"Your input argument {arg1}, {arg2} include non-string element(s) {mylist1} and {mylist2}. These are not of the expected type. Please change this and rerun.")
arg1 = ["2","4",6]
arg2 = [1,2,'0']

exception_add_function(arg1,arg2)


# In[77]:


#two c

def correction_add_function(arg1,arg2):
    
#numeric section
    if sum([type(i)==int for i in arg1])==len(arg1) and sum([type(i)==int for i in arg2])==len(arg2):
        arg1_index=0
        while arg1_index < len(arg1):
            arg_2_sum = 0
            for arg2_elements in arg2:
                arg_2_sum = arg1[arg1_index]+ sum(arg2)
            arg1[arg1_index]=arg_2_sum  
            arg1_index+=1
        return arg1
#string section
    try:
        arg1_index=0
        while arg1_index < len(arg1):
            arg_2_sum = ''
            for arg2_elements in arg2:
                arg_2_sum += arg2_elements
            arg1[arg1_index]=arg1[arg1_index]+str(arg_2_sum)
            arg1_index+=1
        return arg1
    except:
        arg1_index=0
        while arg1_index < len(arg1): #while the index is within the arg1 parameters
            arg_2_sum = ''
            for arg2_elements in arg2:
                arg_2_sum += str(arg2_elements)
            arg1[arg1_index]=str(arg1[arg1_index])+str(arg_2_sum) #concatenate into string 
            arg1_index+=1
        return arg1

arg_str_1=['1','2','3']
arg_str_2=['1','1', 1]
correction_add_function(arg_str_1, arg_str_2)


# In[ ]:




