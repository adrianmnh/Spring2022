<style>
r { color: red }
o { color: orange }
b { color: blue }
</style>


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

## <text style=color:orange>Decomposing complex operations (**&larr;**)
Giving a name to the results of intermediate operations to facilitate the extraction of desired cross-referencing. This allows the reuse of relations that result from intermediate operations 

TempView(clientID, propertyID, comment) &larr; &Pi;<sub>clientID, propertyID, comment)(Viewing)

TempClient(clientID, fName, lName) &larr; &#120504;<sub>clientID, fname, lname</sub>(Client)

Comment(clientID, fname, lname, vclientID, propertyID, comment) &larr; TempClient &#10005; TempView

Result &larr; **&sigma;**<sub>clientID=vclientID</sub>(Comment)

---
## <text style=color:orange>Selection **&sigma;<sub>predicate</sub>(R)**
Contains only tuples of R that satisfy the specified condition(*predicate*)

---
## <text style=color:orange>Projection **&#120503;<sub>a<sub>1..n</sub></sub>(R)**
On a single relation R, defines a vertical subset of R, extracting values of specified attributes and eliminating duplicates

---
## <text style=color:orange>Rename **&#120504;<sub>S</sub>(E)**
Provides a new name S to for the expression E. 

**&#120504;<sub>S<sub>1..n</sub></sub>(E)** : Optionally, the attributes S<sub>1..n</sub> may be renamed as well


---
## <text style=color:orange>Cartesian Product **R&#10005;S**
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

---
## <text style=color:orange>Theta join(&theta;-join) **R&#8904;<sub>F</sub>S**</text>
 R&#8904;<sub>F</sub>S = **&sigma;**<sub>F</sub>(R &#10005; S) &rArr;  Relation that contains tuples satisfying **predicate F** over Cartesian Product R x S.

Predicate F is of the form **R**a<sub>i</sub> &theta; **S**b<sub>i</sub>

Theta operators: &lt; &leq; &gt; &geq; = &ne;

The degree of a Theta join is the sum of the degrees of the operand relations R and S.

---
## <text style=color:orange>Equijoin
A Theta join where the predicate F contains **only equality (=)**

**(<text style=color:orange>&#120503;</text>
<text style=color:blue><sub>clientID, fname,lname</text>
<text style=color:red>(Client)</text>)
&#8904;
<sub>Client.clientID = Viewing.clientID</sub>
(<text style=color:orange>&#120503;</text>
<text style=color:blue><sub>clientID, propertyID, comment</text>
<text style=color:red>(Viewing)</text>)**

`or`

**Result** &larr; TempClient &#8904; <sub>TempClient.clientID = TempViewing.clientID</sub> TempViewing

---
## <text style=color:orange>Natural Join
An Equijoin of the relation R and S over all common attributes x. One ocurrence of each common attribute is eliminated from the result

**<text style=color:orange>&#120503;</text>
<text style=color:blue><sub>clientID, fname,lname</text>
<text style=color:red>(Client)</text>
&#8904;
<text style=color:orange>&#120503;</text>
<text style=color:blue><sub>clientID, propertyID, comment</text>
<text style=color:red>(Viewing)</text>**

`or`

**Result** &larr; TempClient &#8904; TempViewing

---
## <text style=color:orange>Outer Join **R &#10197; S**

Often, a tuple in one relation does not have a matching tuple in the other relation. We may want tuples from one of the relation to appear even when this is the case.

The **Left Outer join R &#10197; S** is a join in which **tuples from R** do **not have matching values** with the common attributes of S that **are included in the resulting relation**. Missing values are set to null.

> Outer join preserves tuples that would have been lost by other types of join

*Provide a status report on property viewings*

**(<text style=color:orange>&#120503;</text>
<text style=color:blue><sub>propertyID, street, city</text>
<text style=color:red>(PropertyForRent)</text>)
&#10197;
<text style=color:red>(Viewing)</text>**

<img src="./331-img/03-03.png">

A **Right Outer join** keeps every tuple in the right-hand relation in the result.

A **Full Outer join** keeps all tuples in both relations, padding tuples with nulls when there are not matches

---
## <text style=color:orange>Semi Join **R &#8883;<sub>F</sub> S**

Contains the tuples of R that participate in the join of R with S satisfying predicate F

Project over the attributes of the first operand **(R)**. It decreases the number of tuples to be handled.

* Computing joins in distributed systems

**R &#8883;<sub>F</sub> S = &#120503;<sub>A</sub>(R&#8904;<sub>F</sub>S)** &rArr; Projection of attributes A<sub>1..n</sub> from the relation join of R and S over predicate F **(Semi-Theta join)**

*List complete details of all staff who work at the branch in Glasgow*

**<text style=color:red>(Staff)</text>
&#8883;
<sub>Staff.branchID = Branch.branchID</sub>
(<text style=color:orange>&sigma;</text>
<text style=color:blue><sub>city='Glasgow'</text>
<text style=color:red>(Branch)</text>)**

<img src="./331-img/03-04.png">

> Only shows Staff relation atrributes

---
## <text style=color:orange>Division **R &div; S** 
Assume R is defined over atribute set A and S is defined over attribute set B such that B &sube; A. 

Let C = A - B &rArr; Set of Attributes of R that are not attributes of S

The **division operation R &div; S** defines a relation over the attributes C that consists of the set of tuples from R that match combination of **every** tuple in S

Division can be expressed as:

T<sub>1</sub> &larr; &#120503;<sub>c</sub>(R)

T<sub>2</sub> &larr; &#120503;<sub>c</sub>((T<sub>1</sub> &#10005; S) - R)

T &larr; T<sub>1</sub> - T<sub>2</sub>

*Identify all clients who have viewed all properties with three rooms*

> We can use Selection to find all properties with three rooms.

**3Room &larr; <text style=color:orange>&sigma;</text>
<text style=color:blue><sub>rooms=3</text>
<text style=color:red>(PropertyForRent)</text>**

>Projection to produce a relation containing only these properties

**3RoomIDs &larr; <text style=color:orange>&#120503;</text>
<text style=color:blue><sub>propertyID</text>
<text style=color:red>(3Room)</text>**

>Division: by projecting Viewing relation from attributes `clientID` and `propertyID` and dividing it by previous Projection

**T &larr; <text style=color:orange>&#120503;</text>
<text style=color:blue><sub>clientID, propertyID</text>
<text style=color:red>(Viewing)</text>**

>Result is a single attribute `clientID` relation

**Result &larr; T &div; 3RoomIDs** 

<img src="./331-img/03-05.png">

---
### Aggregation and Grouping
Often we want to perform a summation or aggregation of data, similar to the totals at the bottom of a report, or some form of grouping of data similar to subtotals.

## <text style=color:orange>Aggregate **<sub>AL</sub>(R)** 
Aggregate function list defines a relation over the aggregate list. Contains one or more **(function, attribute)** pair

* COUNT - returns the number of values associated with attribute
* SUM - returns the sum of the values on the associated attribute
* AVG - returns an average of attribute
* MIN/MAX - smallest/largest value in associated attribute

*How many properties cost more than $900/month to rent?*

---




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



<img src="./331-img/break.png">

## _Class 5 - 2/14/2022_


## UML

Unified Modeling Language

Multi-value indicator - `[1..x]`

Derived attribute - `\`

Arrows indicate relation between tables


<img src="./331-img/break.png">

## _Class 6 - 2/16/2022_

## Music Database

### 1. Questions the database should answer
1. Identify songs by genre, display count
2. Identify sounds and number of plays
3. Identify songs played more than once
4. Identify songs that started, but didn't complete playing(skipped)
5. Identify all songs by Motley Crue or Lagy Gaga
6. Identify song with specific words
7. Identify credit cards expiring soon. Display customer name and method of payment

### 2. Create UML Diagrams

### 3. Convert UML to relations
Artists(artist_id, artist_first, artist_last, artist_stage_name, artist_country, artist_language, artist_dob, artist_debute, artist_age)

artist_id | artist_first | artist_last | artist_stage_name | artist_country | artist_language | artist_dob
:-:|:-:|:-:|:-:|:-:|:-:|:-:
||Prince Rogers | Nelson | The artist; Camille; The artist formally known as prince | US | English | 6/7/58
||Stefani|Germanotta|Lagy Gaga|US; Canada|
||Jeffrey|Williams|Young Thug; SEX; Thugger; | US |English| 8/16/91
||Taylor|Swift||US; France | English



A solution to handle multi value attributes is by creating a separate relation that uniquely identifies each of the multiple attributes

ten commandments ofdatabases

minimize duplication: Make primary keys to prevent duplicate data

 Each realtion must have primary keys

 Ensure domain has limited values, foreign key second constraint

 attribute has a value, cannot be NULL

 Composite primary keys - Are all or some attributes going to be primary keys

 # `Com-PAH-sit` primary keys


 <img src="./331-img/break.png">

## _Class 7 - 2/23/2022_

# Convert UML Diagram entities into Relations


## Types of attributes
* Primary/Foreign Key
* Simple
* Composite
* Single value
* Multi-value
* Derived



song_id | song_name | song_length | song_lyrics 
:-:|:-:|:-:|:-:
999999 | Let's Go Crazy | 2:30 | lalala-lyrics
77777 | Bad Romance | 3:15 | Baby some lyrics go here

`artist_stage_names(artist_id, artist_stage_first, artist_stage_last)`

`artist_country(artist_id, country)`

`songs(song_id, song_name, song_length, song_genere, song_lyrics)`

`artist_song(artist_id, song_id)`

`customer(customer_email, customer_first, customer_last, customer_plan, customer_cc, customer_expire, customer_address(street, zipcode, state, country))`

`plays(play_id, customer_email, song_id, play_start, play_end, play_duration)`

### Question 1:
Identify the country for the artist who sing "Bad Romance". Display Country

* Relation: artist_country - `artist_id`
* Relation: songs - `song_id`
* Relation: artist_song - `artist_id` and `song_id`

BR &larr; ẟsongs.songname="Bad Romance"(songs)

A &larr; ẟsong.song_id = artist_song.song_id(BR X artist_song)

`or`

A &larr; ẟsong.song_id = artist_song.song_id(song X artist_song)

B &larr; ẟA.artist_id = artist_country.artist_id(A X artitst_country)

BR &larr; ẟ


### Question 2:
Identify artist with no songs. Display the artist name.

* Relation: artists
* Relation: artist_song

<img src="./331-img/07-01.png">
<img src="./331-img/07-02.png">



## _Class 8 - 2/28/2022_

# Aggregate Data

### Question 1: Identify the # of songs. Display the number

A &larr; **J** COUNT(song_id)(Songs)



### Question 2: Identify # of customers by state. Display 2 colums: state and # of customers

customer_state **J** COUNT(customer_id)(Customer)

### Identify the number of Songs by artist

Relation: artist
* Attributes: artist_first, artist_last, artist_id

Relation: artist_song
* Attributes: artist_id

begin cartesian product

identify common attribute

Cartesian Product:

`artist and songs where artist.artist_id = artist_song.artist_id`

`or`

artist_id **J** COUNT(song_id)(artist_song)

**A &larr; 
<o>ẟ</o>
<b>artist.artist_id = artist_song.artist_id</b>
(<r>Artist X artist_song</r>)**

**B &larr; 
<o>Artist_first, artist_last</o>
<b>Ͻ (COUNT)artist_id</b>
<r> (A)</r>**

`or`

**B &larr;
Ρ<sub>(Artist Name, Artist Last, Number of Songs)</sub>
<o>Artist_first, artist_last</o>
<b>Ͻ (COUNT)artist_id</b>
<r> (A)</r>**

### Question 4: Identify the number of ocurrences of a song name. Display song name and number of ocurrences

Relation: Songs
Attributes: song_name

**Answer &larr;
P<sub>(Song Name, number of song ocurrences)</sub>
<o>song_name</o>
<b>Ͻ (COUNT)song_id</b>
<r> (Songs)</r>**

### Question 5: Assume plan_cost is in Customer relation. Identify the monthly revenue for all Active Customers.

Domain(customer_plan) &rarr; plan_cost
* Student - 4.99
* Free - 0
* Premium - 9.99

**Answer &larr;
<b>Ͻ (SUM)plan_cost</b>
<r> (Customer)</r>**

### Identify monthly revenue by state
**Answer &larr;
<o>customer_state</o>
<b>Ͻ (SUM)plan_cost</b>
<r> (Customer)</r>**

### Identify monthly revenue by state and show number of customers

**Answer &larr;
<o>customer_state</o>
<b>Ͻ (SUM)plan_cost, COUNT(customer_id)</b>
<r>(Customer)</r>**

![](./331-img/08-01.png)


<img src="./331-img/break.png">

## _Class 9 - 3/2/2022_

# Relational Algebra

## SQL - 'see-quell'
`Structure Query Language`

<div style="display: flex; align-items:center;">
<div>

Relational Database Management System(DBMS)
1. Oracle
   * Windows
   * Unix
2. IBM
   * Windows
   * Unix
   * Mainframe
3. Microsoft
   * OS-Windows
</div>
<div>

## SQL
1. Search
2. Add
3. Change
4. Delete
</div>
</div>

## Different terminology:

<div style="display: flex; align-items:center;">
<div style="width:40%;">

**Relational Algebra** | **Database**
:-: | :-:
Relation | Table
Tuple | Row
Attribute | Column

Candy
* Manufacturer
* Expiration date
* Price
* Product Type
  * Drink
  * Candy
  * Been
  * Newspaper
* Size
  * Domain(S,M,L)
* Type
* Candy name
</div>

<div>

## Type of Data

1. Numbers
   * decimals
   * decimals
2. Text
   * any key on the keyboard
   * *&^%$S@ Symbols
   * 0-9
   * A-Z
   * 
   * unicode cjk
   * "y" or 'y'
   * 2/1-31/2021
   * char(25)
   * 
3. Boolean
   * Y/N - T/F
4. Data/Time
   * MM DD YY HH Mi SS
   * 5/1/2021
   * 
</div>
</div>


```SQL
CREATE TABLE PRODUCT

(PRODUCT_ID NUMBER PRIMARY KEY,

PRODUCT_PRICE DECIMAL(12,2)

```