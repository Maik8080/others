/****** Script for SelectTopNRows command from SSMS  ******/
SELECT TOP (1000) [Region]
      ,[Country]
      ,[Period]
      ,[Advertiser]
      ,[Product_Category]
      ,[Category]
      ,[Subcategory]
      ,[Brand]
      ,[Subbrand]
      ,[Variant]
      ,[Network]
      ,[Creative]
      ,[Media]
      ,[Currency]
      ,[Spend]
      ,[TRP]
      ,[Normalized_Trp]
      ,[Insertions]
      ,[Impressions]
      ,[Spot_Length]
      ,[AcquireID]
  FROM [DM_1219_ColgateGlobal].[dbo].[DFID065658_SampleDataForDashboard_Extracted]

SELECT 
  [Region]
  ,[Country]
  ,[Advertiser]
  ,YEAR([Period]) AS Period
  ,SUM(CASE WHEN ISNUMERIC([Spend]) = 1
  THEN CAST([Spend] AS FLOAT)
  ELSE 0
  END) AS [Spend]
  ,COUNT(DISTINCT [Brand]) AS [BrandCount]
  FROM [DM_1219_ColgateGlobal].[dbo].[DFID065658_SampleDataForDashboard_Extracted]
  --WHERE YEAR([Period]) = '2017'
  GROUP BY
   [Region]
  ,[Country]
  ,[Advertiser]
  ,YEAR([Period])
  ORDER BY 
  1,2,3,4



    SELECT DISTINCT Brand
    FROM [DM_1219_ColgateGlobal].[dbo].[DFID065658_SampleDataForDashboard_Extracted]
	WHERE 
	Region = 'Latin America'
	AND
	Country = 'Argentina'
	AND
	Advertiser = 'COTY'
	AND 
	YEAR(Period) = '2018' -- => Koleston, Rimmel London, Sally Hansen
	--YEAR(Period) = '2017' -- => Coty, Koleston, Rimmel London, Sally Hansen

	


  SELECT 
  [Region]
  ,[Country]
  ,[Advertiser]
  ,YEAR([Period]) AS Period
  ,SUM(CASE WHEN ISNUMERIC([Spend]) = 1
  THEN CAST([Spend] AS FLOAT)
  ELSE 0
  END) AS [Spend]
  ,COUNT(DISTINCT [Brand]) AS [BrandCount]
  INTO [DM_1219_ColgateGlobal].[dbo].[DFID065658_Temp]
  FROM [DM_1219_ColgateGlobal].[dbo].[DFID065658_SampleDataForDashboard_Extracted]
  GROUP BY
   [Region]
  ,[Country]
  ,[Advertiser]
  ,YEAR([Period])
  ORDER BY 
  1,2,3,4 -- 1609 rows


  SELECT -- this gives me Country, Advertiser, Brand level spend; But I need a roll up for 
  [Region]
  ,[Country]
  ,[Advertiser]
  ,[Brand]
  ,YEAR([Period]) AS Period
  ,SUM(CASE WHEN ISNUMERIC([Spend]) = 1
  THEN CAST([Spend] AS FLOAT)
  ELSE 0
  END) AS [Spend]
  ,COUNT(DISTINCT [Brand]) AS [BrandCount]
  INTO [DM_1219_ColgateGlobal].[dbo].[DFID065658_Temp1]
  FROM [DM_1219_ColgateGlobal].[dbo].[DFID065658_SampleDataForDashboard_Extracted]
  GROUP BY
   [Region]
  ,[Country]
  ,[Advertiser]
  ,[Brand]
  ,YEAR([Period])
  ORDER BY 
  1,2,3,4 --9066 rows

  SELECT 
  a.[Region]
  ,a.[Country]
  ,a.[Period]
  ,a.[Advertiser]
  ,a.[Brand]
  ,b.[Spend] AS [SumByAdvertiser]
  ,a.[Spend] AS [SumByBrand]
  ,b.BrandCount AS [BrandCountByAdvertiserInAPeriod]
  FROM DFID065658_Temp1 as a
  LEFT JOIN DFID065658_Temp as b
  ON
	a.[Region] = b.[Region]
	AND a.[Country] = b.[Country]
	AND a.[Advertiser] = b.[Advertiser]
	--AND a.[Brand] = b.[Brand]
	AND a.[Period] = b.[Period]
ORDER BY 1,2,3,4,5,7--,8

WITH T1
AS (
	SELECT *
	    ,SUM(CASE WHEN ISNUMERIC([Spend]) = 1 THEN CAST([Spend] AS FLOAT) ELSE 0 END) over (partition by [Region],[Country],YEAR([Period]),[Advertiser]) AS [SumByAdvertiser]
		,DENSE_RANK() OVER (
			PARTITION BY [Region]
			,[Country]
			,[Advertiser]
			,YEAR([Period]) ORDER BY Brand
			) AS [dr]
	FROM DFID065658_SampleDataForDashboard_Extracted
	)
	,T2
AS (
	SELECT *
		,MAX([dr]) OVER (
			PARTITION BY [Region]
			,[Country]
			,[Advertiser]
			,YEAR([Period])
			) AS [UniqBrandCount]
	FROM T1
	)
SELECT [Region]
	,[Country]
	,YEAR([Period]) AS [Period]
	,[Advertiser]
	,[Brand]
	,[SumByAdvertiser]
	,SUM(CASE 
			WHEN ISNUMERIC([Spend]) = 1
				THEN CAST([Spend] AS FLOAT)
			ELSE 0
			END) AS [SumByBrand]
	,MAX([UniqBrandCount]) AS [BrandCountByAdvertiserInAPeriod]
FROM T2
GROUP BY [Region]
	,[Country]
	,YEAR([Period])
	,[Advertiser]
	,[Brand]
	,[SumByAdvertiser]
ORDER BY [Region]
	,[Country]
	,YEAR([Period])
	,[Advertiser]
	,[Brand]

	
SELECT [Region]
	,[Country]
	,[Advertiser]
	,[Brand]
	,YEAR([Period]) AS [Period]
	,dense_rank() OVER (
		PARTITION BY [Region]
		,[Country]
		,[Advertiser]
		,YEAR([Period]) ORDER BY Brand
		) + dense_rank() OVER (
		PARTITION BY [Region]
		,[Country]
		,[Advertiser]
		,YEAR([Period]) ORDER BY Brand DESC
		) - 1 AS [BrandCount]
	,SUM(CASE 
			WHEN ISNUMERIC([Spend]) = 1
				THEN CAST([Spend] AS FLOAT)
			ELSE 0
			END) OVER (
		PARTITION BY [Region]
		,[Country]
		,[Advertiser]
		,[Brand]
		,YEAR([Period])
		) AS [Spend]
FROM [DM_1219_ColgateGlobal].[dbo].[DFID065658_SampleDataForDashboard_Extracted]
ORDER BY 1,2,3,4



-- decided to transform the source table a bit
SELECT [Region]
      ,[Country]
      ,[Period]
	  ,YEAR([Period]) AS [Year]
      ,[Advertiser]
      ,[Product_Category]
      ,[Category]
      ,[Subcategory]
      ,[Brand]
      ,[Subbrand]
      ,[Variant]
      ,[Network]
      ,[Creative]
      ,[Media]
      ,[Currency]
	  ,CASE WHEN ISNUMERIC([Spend]) = 1 THEN CAST([Spend] AS FLOAT) ELSE 0 END AS [Spend]
	  ,CASE WHEN ISNUMERIC([TRP]) = 1 THEN CAST([TRP] AS FLOAT) ELSE 0.0 END AS [TRP]
      ,CASE WHEN ISNUMERIC([Normalized_Trp]) = 1 THEN CAST([Normalized_Trp] AS FLOAT) ELSE 0.0 END AS [Normalized_Trp]
      ,CASE WHEN ISNUMERIC([Insertions]) = 1 THEN CAST([Insertions] AS FLOAT) ELSE 0 END AS [Insertions]
      ,CASE WHEN ISNUMERIC([Impressions]) = 1 THEN CAST([Impressions] AS FLOAT) ELSE 0.0 END AS [Impressions]
      ,CASE WHEN ISNUMERIC([Spot_Length]) = 1 THEN CAST([Spot_Length] AS FLOAT) ELSE 0 END AS [Spot_Length]
      ,[AcquireID]
  INTO [DM_1219_ColgateGlobal].[dbo].[DFID065658_SampleDataForDashboard_Extracted]
  FROM [DM_1219_ColgateGlobal].[dbo].[DFID065658_SampleDataForDashboard_Extracted_old]

  
-- These are my draft attempts to optimze the hierarchy table
--SELECT -- this works
--		SUM([Spend]) AS [SumOfSpend],
--		COUNT(DISTINCT [Brand]) AS UniqBrandCount,
--		COUNT(DISTINCT [Region]) AS UniqRegionCount, -- 3
--		COUNT(DISTINCT [Country]) AS UniqCountryCount, -- 3
--		COUNT(DISTINCT [Advertiser]) AS UniqAdvertiserCount -- 3
--FROM [DM_1219_ColgateGlobal].[dbo].[DFID065658_SampleDataForDashboard_Extracted]


---- QA
--SELECT SUM(Spend) --61214199281.9903
--FROM [DM_1219_ColgateGlobal].[dbo].[DFID065658_SampleDataForDashboard_Extracted]
--WHERE [YEAR]=2018

--SELECT SUM(Spend) --17739587.7628
--FROM [DM_1219_ColgateGlobal].[dbo].[DFID065658_SampleDataForDashboard_Extracted]
--WHERE [YEAR]=2018 AND Region='South Pacific'

--SELECT SUM(Spend) --7459672.2994
--FROM [DM_1219_ColgateGlobal].[dbo].[DFID065658_SampleDataForDashboard_Extracted]
--WHERE [YEAR]=2018 AND Region='South Pacific' AND Country='New Zealand'

--SELECT SUM(Spend) --2624741.6
--FROM [DM_1219_ColgateGlobal].[dbo].[DFID065658_SampleDataForDashboard_Extracted]
--WHERE [YEAR]=2018 AND Region='South Pacific' AND Country='New Zealand' AND Advertiser='UNILEVER'


-- For distinct count of brands
SELECT [Year], [Region], [Country], [Advertiser], 
       COUNT(DISTINCT [Brand])
FROM [DM_1219_ColgateGlobal].[dbo].[DFID065658_SampleDataForDashboard_Extracted]
GROUP BY GROUPING SETS ( ([Year]),
                         ([Year], [Region]),
                         ([Year], [Region], [Country]), 
                         ([Year], [Region], [Country], [Advertiser])
                        )
---- QA
--SELECT COUNT(DISTINCT Brand) --421
--FROM [DM_1219_ColgateGlobal].[dbo].[DFID065658_SampleDataForDashboard_Extracted]
--WHERE [YEAR]=2018

--SELECT COUNT(DISTINCT Brand) --67
--FROM [DM_1219_ColgateGlobal].[dbo].[DFID065658_SampleDataForDashboard_Extracted]
--WHERE [YEAR]=2018 AND Region='South Pacific'

--SELECT COUNT(DISTINCT Brand) --40
--FROM [DM_1219_ColgateGlobal].[dbo].[DFID065658_SampleDataForDashboard_Extracted]
--WHERE [YEAR]=2018 AND Region='South Pacific' AND Country='New Zealand'

--SELECT COUNT(DISTINCT Brand) --3
--FROM [DM_1219_ColgateGlobal].[dbo].[DFID065658_SampleDataForDashboard_Extracted]
--WHERE [YEAR]=2018 AND Region='South Pacific' AND Country='New Zealand' AND Advertiser='Colgate'


-- finally, I reached to conclusion that we must run this query below everytime we upload new data to our DB
-- for sum of spend on various levels
-- This is the most efficient way to collect hierarchy stats over different groupings that I know of
SELECT CONVERT(VARCHAR,[Year]) AS [YEAR]
		, [Region]
		, [Country]
		, [Advertiser]
		, [Brand]
		, SUM([Spend]) AS [SumOfSpend]
		, COUNT(DISTINCT [Region]) AS UniqRegionCount -- 0:07 secs 
		, COUNT(DISTINCT [Country]) AS UniqCountryCount -- 0:23 secs
		, COUNT(DISTINCT [Advertiser]) AS UniqAdvertiserCount -- 2:29 mins
		, COUNT(DISTINCT [Brand]) AS UniqBrandCount -- 4:30 mins
INTO [DM_1219_ColgateGlobal].[dbo].[DFID065658_SampleDataForDashboard_Hierarchy]
FROM [DM_1219_ColgateGlobal].[dbo].[DFID065658_SampleDataForDashboard_Extracted]
GROUP BY GROUPING SETS ( (),
						 ([Year]),
                         ([Year], [Region]),
                         ([Year], [Region], [Country]), 
                         ([Year], [Region], [Country], [Advertiser]),
                         ([Year], [Region], [Country], [Advertiser], [Brand])
                        );

						
SELECT [Year]
      ,[Region]
      ,[Country]
      ,[Advertiser]
	  ,[Brand]
      ,[SumOfSpend]
      ,[UniqBrandCount]
      ,[UniqRegionCount]
      ,[UniqCountryCount]
      ,[UniqAdvertiserCount]
  FROM [DM_1219_ColgateGlobal].[dbo].[DFID065658_SampleDataForDashboard_Hierarchy]
  ORDER BY 5,4,3,2,1  
  
  
Step1:  
select distinct [Currency]
FROM [DM_1219_ColgateGlobal].[dbo].[DFID065658_SampleDataForDashboard_Extracted]
order by 1

Currency
ARS
AUD
BRL
CAD
CLP
COP
CRC
DOP
HNL
MXP
NZD
PYG
USD
UYP
VEF

Step2: Get currency rates from Google (e.g., Dropbox\...\DashboardCurrencyRates)
Step3: Loaded currency rates into to [DFID065738_Dashboard_CurrencyRates_Extracted]
Step4: Run this to join raw data with currency rate table
SELECT [Region]
      ,[Country]
      ,[Period]
      ,[Year]
      ,[Advertiser]
      ,[Product_Category]
      ,[Category]
      ,[Subcategory]
      ,[Brand]
      ,[Subbrand]
      ,[Variant]
      ,[Network]
      ,[Creative]
      ,[Media]
      ,a.[Currency]
      ,[Spend] AS [Raw_Spend]
	  ,(a.[Spend] * b.[RateToUSD]) AS [Spend_USD]
      ,[TRP]
      ,[Normalized_Trp]
      ,[Insertions]
      ,[Impressions]
      ,[Spot_Length]
INTO [DM_1219_ColgateGlobal].[dbo].[DFID065658_SampleDataForDashboard_Currency_Adjusted]
FROM [DM_1219_ColgateGlobal].[dbo].[DFID065658_SampleDataForDashboard_Extracted] a
INNER JOIN [DM_1219_ColgateGlobal].[dbo].[DFID065738_Dashboard_CurrencyRates_Extracted] b
ON a.[Currency] = b.[Currency]

Step5:
SELECT CONVERT(VARCHAR,[Year]) AS [YEAR]
		, [Region]
		, [Country]
		, [Advertiser]
		, [Brand]
		, SUM([Raw_Spend]) AS [SumOfRawSpend]
		, SUM([Spend_USD]) AS [SumOfSpend]
		, COUNT(DISTINCT [Region]) AS UniqRegionCount -- 0:07 secs 
		, COUNT(DISTINCT [Country]) AS UniqCountryCount -- 0:23 secs
		, COUNT(DISTINCT [Advertiser]) AS UniqAdvertiserCount -- 2:29 mins
		, COUNT(DISTINCT [Brand]) AS UniqBrandCount -- 4:30 mins
INTO [DM_1219_ColgateGlobal].[dbo].[DFID065658_SampleDataForDashboard_Hierarchy]
FROM [DM_1219_ColgateGlobal].[dbo].[DFID065658_SampleDataForDashboard_Currency_Adjusted]
GROUP BY GROUPING SETS ( (),
						 ([Year]),
                         ([Year], [Region]),
                         ([Year], [Region], [Country]), 
                         ([Year], [Region], [Country], [Advertiser]),
                         ([Year], [Region], [Country], [Advertiser], [Brand])
                        );

						
SELECT [Year]
      ,[Region]
      ,[Country]
      ,[Advertiser]
	  ,[Brand]
      ,[SumOfSpend]
      ,[UniqBrandCount]
      ,[UniqRegionCount]
      ,[UniqCountryCount]
      ,[UniqAdvertiserCount]
  FROM [DM_1219_ColgateGlobal].[dbo].[DFID065658_SampleDataForDashboard_Hierarchy]
  ORDER BY 5,4,3,2,1  

Step 6: Generate spend by brand and subbrand table:
SELECT [Year] --55158 rows
	  ,[Period] 
	  ,[Region]
      ,[Country]
      ,[Advertiser]
      ,[Brand]
      ,[Subbrand]
      ,SUM([Spend_USD]) AS [SumOfSpend]
  INTO [DM_1219_ColgateGlobal].[dbo].[DFID065658_SampleDataForDashboard_Spend_By_Brand_And_Subbrand]
  FROM [DM_1219_ColgateGlobal].[dbo].[DFID065658_SampleDataForDashboard_Currency_Adjusted]
  GROUP BY 
  [Year]
	,[Period]
	,[Region]
	,[Country]
	,[Advertiser]
	,[Brand]
	,[Subbrand]
  ORDER BY 1,2,3,4,5


SELECT [Period] -- 40030 rows
	,[Region]
	,[Country]
	,[Advertiser]
	,[Brand]
	,SUM([SumOfSpend]) AS [SumOfSpend]
INTO [DM_1219_ColgateGlobal].[dbo].[DFID065658_SampleDataForDashboard_Spend_By_Brand]
FROM [DM_1219_ColgateGlobal].[dbo].[DFID065658_SampleDataForDashboard_Spend_By_Brand_And_Subbrand]
GROUP BY [Period]
	,[Region]
	,[Country]
	,[Advertiser]
	,[Brand]
ORDER BY 1,2,3,4

SELECT [Period] -- 55158 rows
	,[Region]
	,[Country]
	,[Advertiser]
	,[Subbrand]
	,SUM([SumOfSpend]) AS [SumOfSpend]
INTO [DM_1219_ColgateGlobal].[dbo].[DFID065658_SampleDataForDashboard_Spend_By_Subbrand]
FROM [DM_1219_ColgateGlobal].[dbo].[DFID065658_SampleDataForDashboard_Spend_By_Brand_And_Subbrand]
GROUP BY [Period]
	,[Region]
	,[Country]
	,[Advertiser]
	,[Subbrand]
ORDER BY 1,2,3,4