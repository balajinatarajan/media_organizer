create table mediaindex (
  source varchar(50),
  filetype varchar(50),
  year int,
  month int,
  filename varchar(255),
  fullfilename varchar(1000),
  filesize bigint,
  filehash varchar(255)
);
-- READ QUERIES
select
  *
from mediaindex;
-- ADD QUERIES
  -- Insert test data
insert into mediaindex (
    source,
    filetype,
    year,
    month,
    filename,
    fullfilename,
    filesize,
    filehash
  )
VALUES
  (
    "Golden",
    "Video",
    2010,
    01,
    "lala.mp4",
    "F:/lala.mp4",
    12345,
    "asdf"
  );
-- UPDATE QUERIES
  -- DELETE QUERIES
delete from mediaindex