class Feature_Getting_Module:
    
    def __init__(self):
        
        self.output=[] #store the operand
        self.opertor=[] #store the opertor
        self.precedence={'==':1,'!=':1,'>':2,'<':2,'>=':2,'<=':2,'AND':0,'OR':0,'ALLOF':-1,'BETWEEN':-1,'NONEOF':-1}
        # self.precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}
        self.top=-1 
        
    
    def is_empty(self):
        return True if self.top==-1 else False
        
    def pop(self):
        if(not self.is_empty()):
            self.top -=1 
            return self.opertor.pop()
        else:
            return '$'
    def peek(self):
        return self.opertor[-1]
    
    def push(self,exp):
        self.opertor.append(exp)
        self.top+=1 
        
    def not_greater(self, i): 
        try: 
            a = self.precedence[i] 
            b = self.precedence[self.peek()] 
            return True if a  <= b else False
        except KeyError:  
            return False  
            
    def infix_to_postfix(self,expression):
        
        for exp in expression:
            if exp not in self.precedence:
                if(exp=='('):
                    self.push(exp)
                    
                elif(exp==')'):
                    while((not self.is_empty()) and self.peek()!='('):
                        a=self.pop()
                        self.output.append(a)
                        
                    if((not self.is_empty()) and self.peek()!='('):
                        return -1 
                    else:
                        self.pop()
                else:
                    self.output.append(exp)
            
            else:
                while((not self.is_empty()) and self.not_greater(exp)):
                    self.output.append(self.pop())
                self.push(exp)
                
        while not self.is_empty(): 
            self.output.append(self.pop())
        
            
    def is_Allowed(self,expression,feature_name,user_details):
        
        self.infix_to_postfix(expression)
        print(self.output)

# expression="a+b*(c^d-e)^(f+g*h)-i"
expression="(age > 45 AND gender != 'Male')"
opetors=['(',')','>','<','>=','<=','==','!=','ALLOF','NONEOF','BETWEEN','=','AND','OR']
# expression='age>45'
s=''
expression_list=[]
for i in expression:
    if(i==' '):
        if(len(s)!=0):
            expression_list.append(s)
            s=''
            
    elif(i in opetors):
        if(len(s)!=0):
            expression_list.append(s)
            s=''
        expression_list.append(i)
    else:
        if(i=="'"):
            pass
        else:
            s+=i
if(len(s)!=0):
    expression_list.append(s)

final_expression=[]

i=1 
while(i<len(expression_list)):
    if(expression_list[i]=='=' and (expression_list[i-1]=='=' or expression_list[i-1]=='!' or expression_list[i-1]=='>' or expression_list[i-1]=='<')):
        s=expression_list[i-1]+expression_list[i]
        s=''.join(s)
        final_expression.append(s)
        i+=1 
    else:
        final_expression.append(expression_list[i-1])
    i+=1
final_expression.append(expression_list[-1])


feature_name=['delivery within 2 days','free delivery']
user_details={'age':50,'name':'anand','gender':'Male'}


obj=Feature_Getting_Module()
print(obj.is_Allowed(final_expression,feature_name,user_details))


