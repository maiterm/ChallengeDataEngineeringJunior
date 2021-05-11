SELECT p.[CountryRegionCode] as country_region_code, AVG(s.[TaxRate]) as avg_tax_rate 
FROM [AdventureWorks2014].[Sales].[SalesTaxRate] as s
INNER JOIN [AdventureWorks2014].[Person].[StateProvince] AS p
ON s.[StateProvinceID] = p.[StateProvinceID]
GROUP BY p.[CountryRegionCode]