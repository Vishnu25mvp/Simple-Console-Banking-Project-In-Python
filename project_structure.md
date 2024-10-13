### Create a file as database.py

1. In that create a database and make connectivity between python and sql 
2. Then create a table
3. Table name and attribute's 
> Database Name : Bank 
>> #### Table 1
> > ##### Customer 
> > ##### Customer_id int primary key AUTO_INCREMENT
> >##### Name varchar(30) not null
> >#### Phone_no int not null unique
> >#### Email varchar(20) not null unique
> > #### Password varchar(100) not null 
> 
>
>> #### Table 2
> > ##### Account 
> > ##### Account_no int primary key AUTO_INCREMENT
> >#### Customer_id int foreign key   
> >##### Total_Amount int 
> 
> > #### Table 3
> > #### Transcation
> > ####  Transcation_id int primary key AUTO_INCREMENT
> > #### Account_no int foreign key
> >####  Type (withdraw or Deposit) varchar(10) not null
> >#### Amount float not null

## Console View

1.  log in page Authentication or create a account  with two factor authentication
   2. for log in
      Input data 
      1. user_name 
      2. password 
   >       check this both are present in the database else return to the home page 
   >                               (or)
   >       ask the user to create new account 
2. After login it show
   1. deposit
   2. withdraw
   3. transaction history
   4. account balance
   5. change password (with two factor authentication )


## Operations
1. Sign in:

    fist of all get the information about the user
    like

    Name

    Phone_no

    Email
    
    password
    
    After geting the info we pass a opt to the customer mail by using restapi 
    if the opt is matched with the customer enter one print Account created else not print invaild opt 
    again return to the home page


2. Log in 

   frist of all get the userid and password from user if is matches allow the user to perform bbussince operation


3. deposit 

    after verifyed the user allow user to deposit it will add amount to the Total_amount column in Account table and add the trancation to the 
    transcation table like we need to store account no, type->deposit and amount 

4. withdraw

    after verify the user allow user to withdraw amount from the account if the user withdraw any ammount 
    it affect two table one is account table Total_amount then it must add to transcatino table
    we need to store account no, type->withdraw and amount 
    
5. transcation 

    it show all the transcation done by the user in descending order
    with account balance in account table

5. Balance
    
    it show balance with customer name and account id

6. Password
   
    process change the existing password to new one with authentication
