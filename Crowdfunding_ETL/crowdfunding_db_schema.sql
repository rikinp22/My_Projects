CREATE TABLE "campaign" ( 
	"Cf_id" int NOT NULL, 
	"Contact_id" int PRIMARY KEY, 
	"Company_name" varchar(50) NOT NULL, 
	"Description" text NOT NULL, 
	"Goal" int NOT NULL, 
	"Pledged" int NOT NULL, 
	"Outcome" varchar(50) NOT NULL, 
	"Backers_count" int NOT NULL, 
	"Country" varchar NOT NULL, 
	"Currency" varchar NOT NULL, 
	"Launched_date" date NOT NULL, 
	"End_date" date NOT NULL, 
	"Category_id" varchar NOT NULL, 
	"Subcategory_id" varchar NOT NULL);
	
CREATE TABLE "category" (
	"Category_id" varchar NOT NULL,
	"Category" varchar NOT NULL);

CREATE TABLE "subcategory" (
	"Subcategory" varchar NOT NULL,
	"Category" varchar NOT NULL);

CREATE TABLE "contacts" (
	"Contact_id" int PRIMARY KEY,
	"First_name" varchar NOT NULL,
	"Last_name" varchar NOT NULL,
	"Email" varchar NOT NULL)