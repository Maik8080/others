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
  ,[Period]
  ,SUM(CASE WHEN ISNUMERIC([Spend]) = 1
  THEN CAST([Spend] AS FLOAT)
  ELSE 0
  END) AS [Spend]
  ,COUNT(DISTINCT [Brand]) AS [BrandCount]
  FROM [DM_1219_ColgateGlobal].[dbo].[DFID065658_SampleDataForDashboard_Extracted]
  WHERE YEAR([Period]) = '2017'
  GROUP BY
   [Region]
  ,[Country]
  ,[Advertiser]
  ,[Period]
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
	Period = '2017-03-01'
