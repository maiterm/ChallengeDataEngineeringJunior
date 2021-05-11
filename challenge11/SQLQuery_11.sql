SELECT country.[Name] as country_name
       , currency.[Name] as currency_name
       ,CONVERT(NUMERIC(6,2),ROUND(MAX(currencyRate.[AverageRate]),2)) as currency_rate
       , CONVERT(NUMERIC(6,2),ROUND(AVG(taxrate.[TaxRate]),2)) as average_tax_rate
FROM [AdventureWorks2014].[Sales].[Currency] as currency
JOIN [AdventureWorks2014].[Sales].[CountryRegionCurrency] as countryCurrency
ON countryCurrency.[CurrencyCode] = currency.[CurrencyCode]
JOIN [AdventureWorks2014].[Person].[CountryRegion] as country
ON countryCurrency.[CountryRegionCode] = country.[CountryRegionCode]
JOIN [AdventureWorks2014].[Person].[StateProvince] AS countryID
ON countryCurrency.[CountryRegionCode] = countryID.[CountryRegionCode]
INNER JOIN [AdventureWorks2014].[Sales].[SalesTaxRate] as taxrate
ON taxrate.[StateProvinceID] = countryID.[StateProvinceID]
INNER JOIN [AdventureWorks2014].[Sales].[CurrencyRate] as currencyRate
ON countryCurrency.[CurrencyCode] = currencyRate.[ToCurrencyCode]
GROUP BY country.[Name],currency.[Name]
ORDER By country.[Name]

