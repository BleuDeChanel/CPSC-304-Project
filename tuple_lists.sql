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




-- INSERT INTO Instructors(insSIN, email,phoneNumber,name)
-- VALUES ()







# needs Office_Employees 's table first
INSERT INTO Program_taught(programTitle, numberOfPeople , fee, startDate, endDate, insSIN)
VALUES ('Intro to tennis', 100, 199.98, '2018-05-01', '2018-06-30', '123456789');