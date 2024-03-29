
CREATE TABLE IF NOT EXISTS College (

collegeId int NOT NULL UNIQUE AUTO_INCREMENT,
collegeName varchar(100),
collegeAddressLineOne varchar(100),
collegeAddressLineTwo varchar(100),
collegeCity varchar(15),
collegeState varchar(20),
collegeCountry varchar(20),
collegePhoneNumber varchar(100),

-- Principle Details
collegePrincipleFirstName varchar(100),
collegePrincipleLastName varchar(100),
collegePrincipleEmail nvarchar(320) not null unique,
collegePrincipleContactNumber varchar(100) not null,

-- TPO Details
collegeTPOFirstName varchar(100),
collegeTPOLastName varchar(100),
collegeTPOEmail nvarchar(320) not null unique,
collegeTPOContactNumber varchar(100) not null unique,

-- TIMESTAMP DETAILS
collegeProfileCreateTimestamp TimeStamp,
collegeProfileUpdateTimestamp TimeStamp,

PRIMARY KEY(collegeId)
);
