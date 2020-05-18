create table mediaindex (
  source varchar(50),
  filetype varchar(50),
  year int,
  month int,
  filename varchar(255),
  fullfilename varchar(300),
  filesize bigint,
  filehash varchar(255),
  void varchar(3),
  PRIMARY KEY (fullfilename)
);
-- READ QUERIES
select
  count(*)
from mediaindex
where
  void is NULL;
select
  *
from mediaindex
limit
  1;
select
  filename
from mediaindex
where
  fullfilename like 'F:/NewOrganized/Pictures/2013/04/IMG_9842.jpg';
-- GET DUPLICATE IMAGES
select
  count(*)
from mediaindex
where
  source = "Stage"
  and filetype = "Image"
  and filehash in (
    select
      filehash
    from mediaindex
    where
      source = "Live"
  )
select
  count(*)
from mediaindex m1,
  mediaindex m2
where
  m1.filetype = "Image"
  and m2.filetype = "Image"
  and m1.source = "Stage"
  and m2.source = "Live"
  and m1.filehash = m2.filehash
  and m1.year = m2.year
  and m1.month = m2.month -- GET DUPLICATE VIDEOS
select
  m1.fullfilename
from mediaindex m1,
  mediaindex m2
where
  m1.filetype = "Video"
  and m2.filetype = "Video"
  and m1.source = "Stage"
  and m2.source = "Live"
  and m1.void is NULL
  and m2.void is NULL
  and m1.filesize = m2.filesize
  and m1.filename = m2.filename
select
  count(*)
from mediaindex
where
  filetype = "Video"
  and void is null
  and source = "Stage"
select
  count(*)
from mediaindex
where
  source = "Stage"
  and filetype = "Image" -- ADD QUERIES
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
ALTER TABLE mediaindex
ADD
  COLUMN void varchar(3)
AFTER
  filehash;
-- DELETE QUERIES
delete from mediaindex drop table mediaindex