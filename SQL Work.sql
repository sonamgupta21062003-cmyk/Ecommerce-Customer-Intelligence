create database ecommerce_analytics;

use ecommerce_analytics;

CREATE TABLE Customers(
CustomerID VARCHAR(10) PRIMARY KEY,
CustomerName VARCHAR(100),
Gender VARCHAR(20),
Age INT,
City VARCHAR(50),
Region VARCHAR(30),
SignupDate date
);


-- Product Table
CREATE TABLE Products
(
ProductID VARCHAR(10) PRIMARY KEY,
ProductName VARCHAR(100),
Category VARCHAR(50),
CostPrice DECIMAL(12,2),
SellingPrice DECIMAL(12,2)
);

-- Order Table

CREATE TABLE Orders
(OrderID VARCHAR(10) PRIMARY KEY,
OrderDate DATE,
CustomerID VARCHAR(10),
PaymentMethod VARCHAR(30),
OrderStatus VARCHAR(20),

foreign key (CustomerID)
references Customers(CustomerID)

);

-- OrderDetails
create table OrderDetails
(
OrderDetailID VARCHAR(12) primary KEY,
OrderID VARCHAR(10),
ProductID VARCHAR(10),
Quantity INT,
UnitPrice DECIMAL(12,2),
DiscountPct DECIMAL(5,2),
SalesAmount DECIMAL(14,2),
Profit DECIMAL(14,2),

FOREIGN KEY (OrderID)
references Orders(OrderID),

foreign key (ProductID)
references Products(ProductID)

);

-- Returns
CREATE TABLE Returns
(
ReturnID VARCHAR(10) PRIMARY KEY,
OrderID VARCHAR(10),
ReturnDate DATE,
ReturnReason VARCHAR(50),

FOREIGN KEY (OrderID)
REFERENCES Orders(OrderID)

);

-- Tables check table

show tables;

describe Customers;

describe Products;

describe Orders;

describe Orderdetails;

describe returns;
SELECT * FROM Customers LIMIT 10;
SELECT COUNT(*) as Totalcustomers FROM Customers;

SELECT COUNT(*) as TotalProduct FROM Products;

SELECT COUNT(*) as TotalProduct FROM Orders;

SELECT COUNT(*) as TotalProduct FROM orderdetails;

SELECT COUNT(*) as TotalProduct FROM returns;

SELECT 'Customers' AS TABLENAME,COUNT(*) AS TOTALROWS FROM CUSTOMERS
UNION ALL

SELECT 'Products',COUNT(*) AS TOTALROWS FROM Products

UNION ALL

SELECT 'Orders',COUNT(*) AS TOTALROWS FROM Orders

UNION ALL

SELECT 'OrderDetails',COUNT(*) AS TOTALROWS FROM OrderDetails

UNION ALL

SELECT 'Returns',COUNT(*) AS TOTALROWS FROM returns;

-- Duplicate Check
select customerid,count(*) as DuplicateCount 
from Customers
group by customerid
having count(*)>1;

select productid,count(*) as DuplicateCount from products
group by productid having count(*)>1;

select OrderID,count(*) as DuplicateCount from Orders
group by OrderID having count(*)>1;

-- Null Values

SELECT Sum(CustomerID IS NULL) AS CustomerID_Null,
     Sum(CustomerName IS NULL) AS CustomerName_Null,
     Sum(Gender IS NULL) AS Gender_Null,
     Sum(Age IS NULL) AS Age_Null,
     Sum(City IS NULL) AS City_Null,
     Sum(Region IS NULL) AS Region_Null,
     Sum(SignupDate IS NULL) AS SignupDate_Null
FROM Customers;

-- foreign key Validation
SELECT o.orderid,o.customerid
from orders o  
left join customers c 
on o.customerid = c.customerid
where c.customerid is null;

-- Order Detail Validation

SELECT od.OrderID 
FROM OrderDetails od
Left Join Orders o 
On od.OrderID = o.OrderID
where o.orderID IS null;

-- Basic Bussiness Data check table
SELECT 
MIN(OrderDate) As FirstOrderDate,
Max(OrderDate) AS LastOrderDate,
COUNT(DISTINCT CustomerID) AS UniqueCustomers

From Orders;
-- Total Customers
SELECT COUNT(*) as TOTALOrders From orders;

-- Order Status analyze
SELECT orderstatus, count(*) as TotalOrders
from orders
group by orderstatus;

-- Delivered Orders
SELECT COUNT(*) as Deliveredorders
from orders
where orderstatus = 'delivered';

-- Total Revenue
SELECT 
SUM(od.salesAmount) AS TotalRevenue
FROM orders o 
join orderdetails od 
on o.orderid = od.orderid
where o.orderstatus =  'delivered';

-- Total Profit
SELECT 
SUM(od.profit) AS Totalprofit
FROM orders o 
join orderdetails od 
on o.orderid = od.orderid
where o.orderstatus =  'delivered';

-- Revenue + Profit Together
SELECT 
SUM(od.SalesAmount) AS TotalRevenue,
SUM(od.Profit) AS TotalProfit
FROM Orders o 
JOIN OrderDetails od
ON o.OrderID = od.OrderID 
WHERE o.OrderStatus = 'Delivered';

-- Average order values

SELECT 
SUM(od.SalesAmount) /COUNT(distinct o.OrderID) AS AverageOrderValue
FROM Orders o 
JOIN OrderDetails od
ON o.OrderID = od.OrderID 
WHERE o.OrderStatus = 'Delivered';

-- Category-wise Revenue
SELECT
p.Category,SUM(od.SalesAmount) AS REVENUE
From Orders o 
Join OrderDetails od
on o.Orderid = od.Orderid
Join Products p 
on od.productid = p.productid
where o.orderstatus = 'Delivered'
Group by p.category
order by revenue Desc;

-- Category-wise Profit
SELECT
p.Category,SUM(od.Profit) AS Profit
From Orders o 
Join OrderDetails od
on o.Orderid = od.Orderid
Join Products p 
on od.productid = p.productid
where o.orderstatus = 'Delivered'
Group by p.category
order by profit Desc;

-- Caterory Revenue+ Profit
SELECT 
p.Category,
SUM(od.SalesAmount) AS Revenue,
SUM(od.Profit) AS Profit,
SUM(od.profit) / SUM(od.SalesAmount) *100 AS ProfitMarginpct
FROM Orders o 
JOIN OrderDetails od
on o.Orderid = od.orderid
JOIN Products p 
on od.Productid = p.Productid
where o.OrderStatus = 'Delivered'
GROUP BY p.Category 
ORDER BY Revenue Desc;

-- Monthly Sales Trend
SELECT 
YEAR(o.OrderDate) AS SalesYear,
MONTH(o.OrderDate) AS SalesMonth,
SUM(od.SalesAmount) AS Revenue
From Orders o 
JOIN OrderDetails od
ON o.OrderID = od.OrderID 
WHERE o.OrderStatus = 'Delivered'
GROUP BY
YEAR(o.OrderDate),
Month(o.orderDate)
ORDER BY 
SalesYear,
SalesMonth;

-- Region-wise Revenue

SELECT 
c.Region,
SUM(od.SalesAmount) AS Revenue,
SUM(od.Profit) as Profit
FROM Customers c 
JOIN Orders o 
On c.CustomerID = o.CustomerID 
JOIN OrderDetails od
ON o.orderID = od.OrderID
WHERE o.OrderStatus = 'Delivered'
GROUP BY c.Region
ORDER BY Revenue Desc;

-- top 10 Customers
SELECT 
c.CustomerID,
c.CustomerName,
SUM(od.SalesAmount) AS Revenue,
SUM(od.Profit) AS Profit
FROM Customers c 
JOIN Orders o 
on c.CustomerID = o.CustomerID
JOIN OrderDetails od
on o.OrderID = od.OrderID
WHERE o.OrderStatus = 'Delivered'
GROUP BY 
c.CustomerID,
c.CustomerName
ORDER BY Revenue DESC
LIMIT 10;

-- top 10 Product 
SELECT 
p.ProductID,
p.ProductName,
p.Category,
SUM(od.Quantity) AS UnitsSold,
SUM(od.SalesAmount) AS Revenue,
SUM(od.Profit) AS Profit
FROM Products p  
JOIN OrderDetails od 
on p.ProductID = od.ProductID
JOIN Orders o
on od.OrderID = o.OrderID
WHERE o.OrderStatus = 'Delivered'
GROUP BY 
p.ProductID,
p.ProductName,
p.Category
ORDER BY Revenue DESC
LIMIT 10;
-- Payment Method Analysis
SELECT 
PaymentMethod,
COUNT(*) AS TotalOrders
FROM Orders
WHERE OrderStatus = 'Delivered'
GROUP BY PaymentMethod
ORDER BY TotalOrders DESC;

-- Return Analysis
SELECT 
r.ReturnReason,
Count(*) AS TotalReturns
FROM Returns r 
GROUP BY r.ReturnReason
ORDER BY TotalReturns DESC;


-- Return Rate
SELECT 
COUNT(DISTINCT r.OrderID) AS ReturnedOrders,
COUNT(DISTINCT o.OrderID) AS TotalOrders,
COUNT(DISTINCT r.OrderID) /
COUNT(DISTINCT o.OrderID) * 100 AS ReturnRatePct
FROM Orders o 
LEFT JOIN Returns r 
ON o.OrderID = r.OrderID;



