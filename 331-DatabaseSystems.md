# **Database System - *Daniel Laevitt***

3 exams

Individual work only

Databases are composed of Data, Attributes(Domains), Primary key attributes

Facebook
* Relationships between facebook users
* User- username, first name, last name, password
* Status(online, offline, away, busy, vacation)
* Group(Private, Public, Family, Friends...)

Amazon
* Products(Product_Name, Product_type, price, quantity, prime_status(Y/N))
* Users ( email, (first_name, last_name), organization, dept, (street, state, city, zip, country, planet), prime_member)
* Staff( job_title, salary, (hours, date), )


Domain email = [....]@[....].[....]

Prime_member(Regular, Student, NotPrimeMember)

Title(driver, manager, warehouse operator, ap ar, ....)

Domain Product_Type(Beauty, clothing, warehouse, food)


<img src="./331-img/break.png">

## _Class 3 - 2/7/22_

# Relational Algebra
Theoretical language with operations that work on one or more relations to define another relation without changing the original

Relation are closed under algebra, as numbers are closed under arithmetic

**Closure** - Output from one operation can become input to another


* Unary(Single Relation)
  * **Selection** of selected tuples
  * **Projection** of relation and selected attributes

* Binary(Pairs of Relations)
  * **Cartesian Product** equivalent to *set multiplication*
  * **Union** of relations
  * **Set Difference** A-B = &forall;x s/t x&isin;A and x&notin;B
  * **Intersection** tuples in both relations
  * **Natural Join A&#10781;B** - extended relation tuples
  * **Semi Join &#8883;** - 

<img src="./331-img/03-01.png">


* &delta; predicate (R) - **Selection**
* &prod; col1,...,cikn (R) - **Projection**

### Selection **&sigma;<sub>predicate</sub>(R)**
Contains only tuples of R that satisfy the specified condition(*predicate*)

---
### Projection **&#120503;<sub>a<sub>1..n</sub></sub>(R)**
On a single relation R, defines a vertical subset of R, extracting values of specified attributes and eliminating duplicates

---
### Rename **&#120504;<sub>s<sub>1..n</sub></sub>(E)**
Provides a new relation with a specified name from the expression E, allowing attributes s<sub>1..n</sub> to be renamed


---
### Cartesian Product **R&#10005;S**
Concatenation of tuples, set multiplication

* List the names and comments of all clients who have viewed a property for rent

&#120503;<sub>clientID,fname,lname</sub>(Client) &#10005; &#120503;<sub>clientID, propertyID, comment</sub>(Viewing)

`This operation contains too much information, we need only tuples where the clientIDs are equal from both relations and the comment is not null`

**&sigma;**<sub>Client.clientID = Viewing.clientID</sub> (&#120503;<sub>clientID,fname,lname</sub>(Client) &#10005; &#120503;<sub>clientID, propertyID, comment</sub>(Viewing))

---
### Join Operations
Equivalent to performing a **Selection** operation, using the **join predicate** as the selection formula, **over the Cartesian Product** of the two operand relations
* Theta-join
* Equi-join
* Natural Join
* Outer join
* Semi-join

## <text2 style=color:orange>Theta join(&theta;-join) **R&#8904;<sub>F</sub>S**M</text>
 R&#8904;<sub>F</sub>S = **&sigma;**<sub>F</sub>(R &#10005; S) &rArr;  Relation that contains tuples satisfying **predicate F** over Cartesian Product R x S.

Predicate F is of the form **R**a<sub>i</sub> &theta; **S**b<sub>i</sub>

Theta operators: &lt; &leq; &gt; &geq; = &ne;

The degree of a Theta join is the sum of the degrees of the operand relations R and S.

## <text2 style=color:orange>Equijoin
A Theta join where the predicate F contains **only equality (=)**







---

## Decomposing complex operations (**&larr;**)
Giving a name to the results of intermediate operations to facilitate the extraction of desired cross-referencing. This allows the reuse of relations that result from intermediate operations 

TempView(clientID, propertyID, comment) &larr; &Pi;<sub>clientID, propertyID, comment)(Viewing)

TempClient(clientID, fName, lName) &larr; &#120504;<sub>clientID, fname, lname</sub>(Client)

Comment(clientID, fname, lname, vclientID, propertyID, comment) &larr; TempClient &#10005; TempView

Result &larr; **&sigma;**<sub>clientID=vclientID</sub>(Comment)



Used Cars | Attributes
-: | :-
car | mileage, make, model, color, picture
customer| fname, lname, street, city, zip
trans | 
recall | vins

Netflix | Attributes
-: | :-
customer |
shows | title, genres, year, rating, language, duration, actors 
watching |

**Domain**
* rating = PG-13, PG, G, R
* language = French, English, ...
* genre = Sci-Fi, action, comedy, ...

Hospital | Attributes
-: | :-
staff | staff_ID, staff_first, staff_last, staff_title
patient | patient_ID, patient_first, patient_last, (address), insurance
room | room_ID, building, dept, occupied, floor
admission | patient_id, room_id, assigned_date
department | dept_id, dept_name, dept_phone, room
staff_dept | staff_id, dept_id
visit | patient_id, staff_id, date_of_visit, room_id, procedure
diagnosis | 

Dept_id | Dept_name | Dept_phone | [] | Staff_id | Staff_first | Staff_last
:-: | :-: | :-: | :-: | :-: | :-: | :-:
100 | ER | null |[]| 111111 | Sally | Smith
200 | Surgery | null |[]| 222222 | Ben | Dover
302 | ENT | null |[]| 33333 | Pik | Achu
99 | Billing | 718-997-1111 | []

### **Domains**
Insurance = Medicare, Medicaid, Blue Cross, UHC, Oxford...
Dept_name = Cardiology, ER, Surgery, ENT, mental health, transplant...
Procedude = Check up, exam, xray, surgery, sonogram, CAT Scan, MRI, cast

### **Composite Primary Key**
A pseudo primary key that is acquired by combining 2 or more foreign keys. In general, foreign keys cannot be used as primary keys in a Relation due to its lack of uniqueness

Staff_id | Dept_id
:-: | :-: 
11111 | 99
22222 | 100
3333 | 200
22222 | 302
11111 | 200

`combining foreign keys ...`

**Surgeon &larr;
<text style=color:orange>SELECTION</text>
<text style=color:blue>Predicate</text>
<text style=color:red>Relation</text>
&rArr;
<text style=color:orange>&delta;</text>
<text style=color:blue>staff_title = "surgeon"</text>
<text style=color:red>(Staff)**</text> 

> Relations can be joined only if there is a common attribute using the Cartesian Product


<img src="./331-img/break.png">

## _Class 4 - 2/9/22_

*Identify the room for patient Stephanie Jones. Display the room.*

Step 1: Identify the relations
* Patient, Patient_Room

Step 2: Identify the attributes
* Patient_first, Patient_last, room_ID

Step 3: Identify common attribute if performing a certesian product
* Patient(Patient_ID)

Step 4: Perform the search

Step 5: Display the output

**A &larr;
<text style=color:orange>&delta;</text>
<text style=color:blue>patient_first="Stephanie" &and; patient_last="Jones"</text>
<text style=color:red>(Patient)</text>**

**B &larr;
<text style=color:orange>&delta;</text>
<text style=color:blue>A.patient_ID = Patient_Room.patient_ID</text>
<text style=color:red>(A &#10005; Patient_Room)</text>**

<img src="./331-img/04-01.png">