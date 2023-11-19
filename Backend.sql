DROP DATABASE DB;
CREATE DATABASE DB;
USE DB;
CREATE TABLE TBL_STOCK (
	Product_ID Varchar(6) Not Null,
	Product_Name Varchar(20) Not Null,
	Quantity_On_Hand int Not Null,
	Product_Unit_Price Numeric(11,2) Not Null,
	Reorder_Level int Not Null,
	CONSTRAINT PK00 PRIMARY KEY(Product_ID),
	CONSTRAINT UQ01 UNIQUE(Product_Name),
	CONSTRAINT CH02 CHECK(Quantity_On_Hand >= 0),
	CONSTRAINT CH03 CHECK(Product_Unit_Price >= 0),
	CONSTRAINT CH04 CHECK(Reorder_Level >= 0)
);

CREATE TABLE TBL_SALES (
	Sales_ID Varchar(6) Not Null, 
	Sales_Date Date Not Null,
	Product_ID Varchar(6) Not Null,
	Quantity_Sold int(11) Not Null,
	Sales_Price_Per_Unit Numeric(11,2) Not Null,
	CONSTRAINT PK10 PRIMARY KEY(Sales_ID),
	CONSTRAINT FK11 FOREIGN KEY(Product_ID) REFERENCES TBL_STOCK(Product_ID),
	CONSTRAINT CH12 CHECK(Quantity_Sold >= 0),
	CONSTRAINT CH13 CHECK(Sales_Price_Per_Unit >= 0)
);

INSERT INTO TBL_STOCK VALUES('1001', 'REDMI Note 3', 20, 12000, 5);
INSERT INTO TBL_STOCK VALUES('1002', 'Iphone 5S', 10, 21000, 2);
INSERT INTO TBL_STOCK VALUES('1003', 'Panasonic P55', 50, 5500, 5);
	
CREATE VIEW V_SALES_REPORT AS
	SELECT Sales_ID, Sales_Date, Product_ID, Product_Name, 
	Quantity_Sold, Product_Unit_Price, Sales_Price_Per_Unit, 
	(Sales_Price_Per_Unit - Product_Unit_Price) Profit_Amount
	FROM TBL_STOCK NATURAL JOIN TBL_SALES
	ORDER BY Profit_Amount DESC, Sales_ID ASC;
CREATE TABLE LOGIN(
	USERRID VARCHAR(11) NOT NULL,
	PASSWORD VARCHAR(11) NOT NULL,
	NAME VARCHAR(15) NOT NULL,
	EMAIL VARCHAR(21) NOT NULL,
	MOBIL_NO VARCHAR(12) NOT NULL,
	CONSTRAINT PK01 PRIMARY KEY(USERRID),
	CONSTRAINT UQ11 UNIQUE(PASSWORD) 
);
INSERT INTO LOGIN VALUES('admin', 'admin','Null', 'null@gmail.com', '99XXXXXXXX05');


