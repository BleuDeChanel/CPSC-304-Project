CREATE TABLE Club_Memberships (
 membershipID int not null,
 tier int NOT NULL,
 SID char(8),
 PRIMARY KEY (membershipID),
 FOREIGN KEY (tier) REFERENCES Membership_Plans,
 FOREIGN KEY (SID) REFERENCES Student_Members ON DELETE CASCADE ON UPDATE CASCADE,
 UNIQUE (SID)
);


INSERT INTO club_memberships(membershipID, tier)
VALUES (1,1);

INSERT INTO club_memberships(membershipID, tier)
VALUES (2,2);

INSERT INTO club_memberships(membershipID, tier)
VALUES (3,3);

INSERT INTO club_memberships(membershipID, tier)
VALUES (4,4);

INSERT INTO club_memberships(membershipID, tier)
VALUES (5,5);



CREATE TABLE Membership_plans (
  tier int,
  fee decimal(7,2),
  PRIMARY KEY (tier)
);


INSERT INTO Membership_Plans(tier, fee)
VALUES (1,5);

INSERT INTO Membership_Plans(tier, fee)
VALUES (2,10);

INSERT INTO Membership_Plans(tier, fee)
VALUES (3,15);

INSERT INTO Membership_Plans(tier, fee)
VALUES (4,50);

INSERT INTO Membership_Plans(tier, fee)
VALUES (5,100);



CREATE TABLE Student_Members (
 membershipID int not null,
 SID char(8) not null,
 PRIMARY KEY (membershipID),
 FOREIGN KEY (membershipID) REFERENCES Club_Memberships
);


INSERT INTO Student_Members(membershipID, SID)
VALUES (1, 40018153);

INSERT INTO Student_Members(membershipID, SID)
VALUES (2, 27299163);

INSERT INTO Student_Members(membershipID, SID)
VALUES (3, 29634145);

INSERT INTO Student_Members(membershipID, SID)
VALUES (4, 36789148);

INSERT INTO Student_Members(membershipID, SID)
VALUES (5, 12308164);



CREATE TABLE Customers (
 phoneNumber char(12),
 name char(50),
 email char(20),
 address char(50),
 membershipID int,
 PRIMARY KEY (phoneNumber, name),
 FOREIGN KEY (membershipID) REFERENCES Club_Memberships ON DELETE CASCADE ON UPDATE CASCADE
);


INSERT INTO Customers(phoneNumber, name, email, address, membershipID)
VALUES ('778-873-1165', 'Jin Min Lee', 'vfvxz@naver.com', '3355 Binning Rd, Vancouver, BC, V6S 0J1', 1);

INSERT INTO Customers(phoneNumber, name, email, address, membershipID)
VALUES ('778-886-5715', 'Mark Pawlowski', 'moopok@gmail.com', '2401 Wesbrookmall, Vancouver, BC, V6S 0S2', 2);

INSERT INTO Customers(phoneNumber, name, email, address, membershipID)
VALUES ('604-872-5815', 'Peyman Bateni', 'peylink@hotmail.com', '3377 Student Union BLVD, Vancouver, BC, V6T 0K1', 3);

INSERT INTO Customers(phoneNumber, name, email, address, membershipID)
VALUES ('604-883-5678', 'Qiao Zhu', 'juliaaa77@gmail.com', '2201 Wesbrookmall, Vancouver, BC, V6S 0S1', 4);

INSERT INTO Customers(phoneNumber, name, email, address, membershipID)
VALUES ('778-886-2413', 'Nadal Rafael', 'nadal.r@ubc.ca', '3355 Binning Rd, Vancouver, BC, V6S 0J1', 5);



CREATE TABLE Office_Employees (
 officeSIN char(9),
 phoneNumber char(12),
 name char(12),
 email char(20),
 PRIMARY KEY (officeSIN)
);


INSERT INTO Office_Employees(officeSIN, email,phoneNumber,name)
VALUES ('111111111', 'john@gmail.com', '111-222-4455', 'John Doe');

INSERT INTO Office_Employees(officeSIN, email,phoneNumber,name)
VALUES ('222222222', 'mary@gmail.com', '111-222-4466', 'Mary Smith');

INSERT INTO Office_Employees(officeSIN, email,phoneNumber,name)
VALUES ('333333333', 'mike@gmail.com', '111-222-4477', 'Mike Smith');

INSERT INTO Office_Employees(officeSIN, email,phoneNumber,name)
VALUES ('444444444', 'peyman@gmail.com', '111-222-4488', 'Peyman Dude');

INSERT INTO Office_Employees(officeSIN, email,phoneNumber,name)
VALUES ('555555555', 'sarah@gmail.com', '111-222-4499', 'Sarah Young');



CREATE TABLE Instructors (
 insSIN char(9),
 phoneNumber int,
 name char(12),
 email char(20),
 PRIMARY KEY (insSIN)
);


INSERT INTO Instructors(insSIN,phoneNumber,name,email)	
VALUES ('666666666',1112224455,'Roger','roger@gmail.com');

INSERT INTO Instructors(insSIN,phoneNumber,name,email)	
VALUES ('777777777',1112224466,'Mary','mary@gmail.com');

INSERT INTO Instructors(insSIN,phoneNumber,name,email)	
VALUES ('123456789',1112224477,'Mike','mike@gmail.com');

INSERT INTO Instructors(insSIN,phoneNumber,name,email)	
VALUES ('444455555',1112224488,'Mary','peyman@gmail.com');

INSERT INTO Instructors(insSIN,phoneNumber,name,email)	
VALUES ('555511111',1112224499,'Sarah','sarah@gmail.com');



INSERT INTO Program_taught(programTitle, numberOfPeople , fee, startDate, endDate, insSIN)
VALUES ('Intro to tennis', 100, 199.98, '2018-05-01', '2018-06-30', '666666666');

INSERT INTO Program_taught(programTitle, numberOfPeople , fee, startDate, endDate, insSIN)
VALUES ('Intermediate tennis', 65, 249.99, '2018/05/01', '2018-06-30', '777777777');

INSERT INTO Program_taught(programTitle, numberOfPeople , fee, startDate, endDate, insSIN)
VALUES ('Amatuer tennis', 35, 349.98, '2018-04-01', '2018-06-30', '123456789');

INSERT INTO Program_taught(programTitle, numberOfPeople , fee, startDate, endDate, insSIN)
VALUES ('Semi-pro tennis', 2, 500, '2018-03-02', '2018-07-31', '444455555');

INSERT INTO Program_taught(programTitle, numberOfPeople , fee, startDate, endDate, insSIN)
VALUES ('Professional tennis', 8, 1000, '2018-01-02', '2018-08-31', '555511111');



create table Program_court_reservation (
	courtNumber int not null,
 	date date not null,
 	startTime time not null,
 	endTime time not null,
 	officeSIN char(9) not null,
 	programTitle char(20) not null, 
 	PRIMARY KEY (courtNumber, date, startTime),
 	FOREIGN KEY (officeSIN) REFERENCES Office_Employees,
 	FOREIGN KEY (programTitle) REFERENCES Program_taught ON DELETE CASCADE ON UPDATE CASCADE
);

INSERT INTO Program_court_reservation(courtNumber, date, startTime,endTime, officeSIN, programTitle)	
VALUES (1, '2018/05/01', '10:00', '11:00', '111111111', 'Intro to tennis');

INSERT INTO Program_court_reservation(courtNumber, date, startTime, endTime, officeSIN, programTitle)	
VALUES (2, '2018/05/01', '10:00', '11:00', '222222222', 'Intermediate tennis');

INSERT INTO Program_court_reservation(courtNumber, date, startTime, endTime, officeSIN, programTitle)	
VALUES (3, '2018/04/01', '13:00', '14:30', '333333333', 'Amatuer tennis');

INSERT INTO Program_court_reservation(courtNumber, date, startTime, endTime, officeSIN, programTitle)	
VALUES (4, '2018/03/02', '13:00', '15:00', '444444444', 'Semi-pro tennis');

INSERT INTO Program_court_reservation(courtNumber, date, startTime, endTime, officeSIN, programTitle)	
VALUES (5, '2018/01/02', '14:00', '17:00', '555555555', 'Professional tennis');




-- CREATE TABLE Private_taught (
--  privateTitle char(20), 
--  private_fee decimal(7,2),
--  startDate date,
--  endDate date,
--  insSIN char(9),
--  PRIMARY KEY (privateTitle),
--  FOREIGN KEY (insSIN) REFERENCES Instructors
-- );

INSERT INTO Private_taught(privateTitle,private_fee,startDate,endDate,insSIN)
VALUES ('Master Lesson', 10000, '2018/06/20', '2018/07/20', '666666666');

INSERT INTO Private_taught(privateTitle,private_fee,startDate,endDate,insSIN)
VALUES ('Amateur Lesson', 299.99, '2018/06/20', '2018/08/20', '777777777');

INSERT INTO Private_taught(privateTitle,private_fee,startDate,endDate,insSIN)
VALUES ('Amateur Lesson 2', 499.99, '2018/06/20', '2018/07/20', '555511111');

INSERT INTO Private_taught(privateTitle,private_fee,startDate,endDate,insSIN)
VALUES ('Master Lesson 2', 8999.9, '2018/08/20', '2018/09/20', '666666666');

INSERT INTO Private_taught(privateTitle,private_fee,startDate,endDate,insSIN)
VALUES ('Master Lesson 3', 10000, '2018/10/20', '2018/11/20', '666666666');



CREATE TABLE Customer_reserves_court (
  phoneNumber char(12) not null,
  name char(50) not null,
  courtNumber int not null, 
  date date not null,
  startTime time not null,
  endTime time not null,
  officeSIN char(9) NOT NULL,
  PRIMARY KEY (courtNumber, date, startTime),
  FOREIGN KEY (officeSIN) REFERENCES Office_employees,
  FOREIGN KEY (phoneNumber, name) REFERENCES Customers ON DELETE CASCADE ON UPDATE CASCADE
);


INSERT INTO Customer_reserves_court(phoneNumber, name, courtNumber, date, startTime, endTime, officeSIN)
VALUES ('778-873-1165', 'Jin Min Lee', 1, '2018/04/30', '11:00', '12:30', '111111111');

INSERT INTO Customer_reserves_court(phoneNumber, name, courtNumber, date, startTime, endTime, officeSIN)
VALUES ('778-886-5715', 'Mark Pawlowski', 2, '2018/05/02', '13:00', '14:00', '222222222');

INSERT INTO Customer_reserves_court(phoneNumber, name, courtNumber, date, startTime, endTime, officeSIN)
VALUES ('604-872-5815', 'Peyman Bateni', 3, '2018/06/03', '16:00', '17:00', '333333333');

INSERT INTO Customer_reserves_court(phoneNumber, name, courtNumber, date, startTime, endTime, officeSIN)
VALUES ('604-883-5678', 'Qiao Zhu', 4, '2018/05/05', '16:00', '17:00', '444444444');

INSERT INTO Customer_reserves_court(phoneNumber, name, courtNumber, date, startTime, endTime, officeSIN)
VALUES ('778-886-2413', 'Nadal Rafael', 5,'2018/07/01','9:00','11:30','555555555');



CREATE TABLE Private_course_court_reservation (
 privateTitle char(20) not null, 
 courtNumber int not null,
 date date not null,
 startTime time not null,
 endTime time not null,
 officeSIN char(9) not null,

 PRIMARY KEY (courtNumber, date, startTime),
 FOREIGN KEY (privateTitle) REFERENCES Private_taught ON DELETE CASCADE ON UPDATE CASCADE,
 FOREIGN KEY (officeSIN) REFERENCES Office_employees
);


INSERT INTO Private_course_court_reservation(privateTitle, courtNumber, date, startTime, endTime, officeSIN)
VALUES ('Master Lesson', 1, '2018/06/20', '11:00', '13:00', '111111111');

INSERT INTO Private_course_court_reservation(privateTitle, courtNumber, date, startTime, endTime, officeSIN)
VALUES ('Amateur Lesson', 2, '2018/06/20', '11:00', '12:00', '222222222');

INSERT INTO Private_course_court_reservation(privateTitle, courtNumber, date, startTime, endTime, officeSIN)
VALUES ('Amateur Lesson 2',	1,	'2018/06/20',	'14:00',	'16:00', '333333333');

INSERT INTO Private_course_court_reservation(privateTitle, courtNumber, date, startTime, endTime, officeSIN)
VALUES ('Master Lesson 2',	2,	'2018/06/21', '14:00',	'16:00', '444444444');

INSERT INTO Private_course_court_reservation(privateTitle, courtNumber, date, startTime, endTime, officeSIN)
VALUES ('Master Lesson 3',	3,	'2018/06/22',	'14:00',	'17:00', '555555555');



CREATE TABLE Customer_register_program (
 phoneNumber char(12) NOT NULL,
 name char(50) NOT NULL,
 programTitle char(20) NOT NULL,
 programRegNumber int,
 officeSIN char(9), 
 PRIMARY KEY (programRegNumber),
 FOREIGN KEY (programTitle) REFERENCES Program_taught ON DELETE CASCADE ON UPDATE CASCADE,
 FOREIGN KEY (phoneNumber, name) REFERENCES Customers ON DELETE CASCADE ON UPDATE CASCADE,
 FOREIGN KEY (officeSIN) REFERENCES Office_Employees
);


INSERT INTO Customer_register_program(phoneNumber, name, programTitle, programRegNumber, officeSIN)
VALUES ('778-873-1165', 'Jin Min Lee', 'Intro to tennis', 1, '111111111');

INSERT INTO Customer_register_program(phoneNumber, name, programTitle, programRegNumber, officeSIN)
VALUES ('778-886-5715',	'Mark Pawlowski',	'Intermediate tennis',	2,	'222222222');

INSERT INTO Customer_register_program(phoneNumber, name, programTitle, programRegNumber, officeSIN)
VALUES ('604-872-5815',	'Peyman Bateni',	'Amatuer tennis',	3,	'333333333');

INSERT INTO Customer_register_program(phoneNumber, name, programTitle, programRegNumber, officeSIN)
VALUES ('604-883-5678',	'Qiao Zhu',	'Semi-pro tennis',	4,	'444444444');

INSERT INTO Customer_register_program(phoneNumber, name, programTitle, programRegNumber, officeSIN)
VALUES ('778-886-2413',	'Nadal Rafael',	'Professional tennis',	5,	'555555555');



-- we don't need officeSIN here, unlike the program register?

CREATE TABLE Customer_register_private (
 phoneNumber char(12) NOT NULL,
 name char(50) NOT NULL,
 privateTitle char(20) NOT NULL,
 privateRegNumber int, 
 PRIMARY KEY (privateRegNumber),
 FOREIGN KEY (phoneNumber, name) REFERENCES Customers ON DELETE CASCADE ON UPDATE CASCADE,
 FOREIGN KEY (privateTitle) REFERENCES Private_taught ON DELETE CASCADE ON UPDATE CASCADE,
 UNIQUE (privateTitle)
);


INSERT INTO Customer_register_private(phoneNumber, name, privateTitle, privateRegNumber)
VALUES ('778-873-1165',	'Jin Min Lee', 'Master Lesson', 1);

INSERT INTO Customer_register_private(phoneNumber, name, privateTitle, privateRegNumber)
VALUES ('778-886-5715',	'Mark Pawlowski', 'Amateur Lesson', 2);

INSERT INTO Customer_register_private(phoneNumber, name, privateTitle, privateRegNumber)
VALUES ('604-872-5815',	'Peyman Bateni', 'Amateur Lesson 2', 3);

INSERT INTO Customer_register_private(phoneNumber, name, privateTitle, privateRegNumber)
VALUES ('604-883-5678',	'Qiao Zhu', 'Master Lesson 2', 4);

INSERT INTO Customer_register_private(phoneNumber, name, privateTitle, privateRegNumber)
VALUES ('778-886-2413',	'Nadal Rafael', 'Master Lesson 3', 5);


---------------------- aboves are inserted