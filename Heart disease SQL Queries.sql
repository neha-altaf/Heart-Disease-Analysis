--create table
create table Heart(
age int,
sex varchar(10),
cp int,
trestbps int,
chol int,
fbs int,
restecg int,
thalach int,
exang int,
oldpeak float,
slope int,
ca int,
thal int,
target int
);

--changing table name
Alter table Heart rename to cardiovascular_data;


--i mistakenly set datatype of sex into varchar . lets change it to integer as our data is in integer format
--first create new column
alter table cardiovascular_data add column sex_new integer;
--copy data from old column to new column
update cardiovascular_data set sex_new=sex::integer;
--drop previous column
alter table cardiovascular_data drop column sex;
--change column name
alter table cardiovascular_data rename column sex_new to sex;


--access whole table record
select * from cardiovascular_data;

--Count total patients in the dataset
select count(*) as total_patients from cardiovascular_data;

--Number of patients with and without heart disease
select target, count(*) as count from cardiovascular_data group by target;

--Average age of patients with and without heart disease
select target, avg(age) as avg_age from cardiovascular_data group by target;

--retrieve records where age is greater than 50
select * from cardiovascular_data where age> 50;

--find the avg cholestrol level in male
select avg(chol) from cardiovascular_data where sex=1;

--Average cholesterol levels for patients with and without heart disease
SELECT target, avg(chol) AS avg_cholesterol FROM cardiovascular_data GROUP BY target;

--find average cholestrol level of each age group
select age, avg(chol) as avg_chol from cardiovascular_data group by age order by age;

--retrieve records with cholestrol levels above 250
select * from cardiovascular_data where chol>250 order by chol;

--age distribution
select age,count(*) as count from cardiovascular_data group by age order by age;

--Age group distribution for patients with heart disease
SELECT 
    CASE 
        WHEN age BETWEEN 20 AND 30 THEN '20-30'
        WHEN age BETWEEN 31 AND 40 THEN '31-40'
        WHEN age BETWEEN 41 AND 50 THEN '41-50'
        WHEN age BETWEEN 51 AND 60 THEN '51-60'
        ELSE '60+'
    END AS age_group, COUNT(*) AS count
FROM cardiovascular_data WHERE target = 1
GROUP BY age_group;

--Heart disease cases among males vs. females
SELECT sex, COUNT(*) AS count FROM cardiovascular_data  WHERE target = 1 GROUP BY sex;

--Average max heart rate achieved (thalach) based on gender
SELECT sex, AVG(thalach) AS avg_max_hr FROM cardiovascular_data GROUP BY sex;

--Distribution of chest pain types (cp) among heart disease patients
SELECT cp, COUNT(*) AS count FROM cardiovascular_data WHERE target = 1 GROUP BY cp;

--BUILDING DECISION TREES
with decision_tree as (select age,sex,chol,count (*) as count from cardiovascular_data group by age,sex,chol;)
select * from decision_tree order by count desc;
