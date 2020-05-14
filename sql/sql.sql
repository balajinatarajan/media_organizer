create table mediaindex (
  source varchar(50),
  filetype varchar(50),
  year int,
  month int,
  filename varchar(255),
  fullfilename varchar(300),
  filesize bigint,
  filehash varchar(255),
  PRIMARY KEY (fullfilename)
);
-- READ QUERIES
select
  count(*)
from mediaindex;
select
  *
from mediaindex
limit
  1;
select
  filename
from mediaindex
where
  fullfilename like 'F:/NewOrganized/Pictures\\\\2013\\\\04\\\\IMG_9842.jpg';
-- ADD QUERIES
  -- Insert test data
insert ignore into mediaindex (
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
delete from mediaindex drop table mediaindex