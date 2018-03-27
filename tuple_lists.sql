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




 -- insSIN char(9),
 -- phoneNumber int,
 -- name char(12),
 -- email char(20),

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


-- Program_court_reservation(court#,date, startTime,programTitle)			
-- court#	date	startTime	programTitle
-- 1	2018/05/01	10:00	Intro to tennis
-- 2	2018/05/01	10:00	Intermediate tennis
-- 3	2018/04/01	13:00	Amatuer tennis
-- 4	2018/03/02	13:00	Semi-pro tennis
-- 5	2018/01/02	14:00	Professional tennis

create table Program_court_reservation (
	courtNumber int not null,
 	date date not null,
 	startTime time not null,
 	endTime time not null,
 	officeSIN char(9) not null,
 	programTitle char(20) not null, 
 	PRIMARY KEY (courtNumber, date, startTime),
 	FOREIGN KEY (officeSIN) REFERENCES Office_Employees ON DELETE CASCADE ON UPDATE CASCADE,
 	FOREIGN KEY (programTitle) REFERENCES Program_taught
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


---------------------- aboves are inserted

