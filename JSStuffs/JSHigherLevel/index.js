const companies = [
    {name: "Company One", category: "Finance", start: 1981, end: 2003},
    {name: "Company Two", category: "Retail", start: 1992, end: 2008},
    {name: "Company Three", category: "Auto", start: 1999, end: 2007},
    {name: "Company Four", category: "Retail", start: 1989, end: 2010},
    {name: "Company Five", category: "Technology", start: 2009, end: 2014},
    {name: "Company Six", category: "Finance", start: 1987, end: 2010},
    {name: "Company Seven", category: "Auto", start: 1986, end: 1996},
    {name: "Company Eight", category: "Technology", start: 2011, end: 2016},
    {name: "Company Nine", category: "Retail", start: 1981, end: 1989}
  ];
  
  const ages = [33, 12, 20, 16, 5, 54, 21, 44, 61, 13, 15, 45, 25, 64, 32];

/*
    forEach Function
*/
  companies.forEach((company) => console.log(company.name));

/*
    Filter
*/

// get array of those who can drink no new array
const canDrink = ages.filter( (age) => {
    if (age >= 21) {
        true;
    }
});
console.log(canDrink);

// get companies that are retail 
const retailCompanies = companies.filter( company => company.category === 'Retail')
console.log(retailCompanies);

// get companies in 80s
const company80 = companies.filter( company => (company.start > 1979 && company.start < 1990))
console.log(company80)

// get companies that lasted 10 years or more
const companies10Yr = companies.filter (company => (company.end - company.start) >= 10)
console.log(companies10Yr)

/*
    Map
*/

// Create array of company names
const companyNames = companies.map ( company => company.name)
console.log(companyNames)

// Test Map
const testMap = companies.map( company => `${company.name}: ${company.end - company.start} yrs`)
console.log(testMap)

const agesSquare = ages.map (age => Math.sqrt(age))
console.log(agesSquare)

const ageMap = ages
    .map(age => Math.sqrt(age))
    .map(age => age * 2);
console.log(ageMap)

/*
    Sort
*/

//Sort companies by start date
const sortedCompanies = companies.sort((a, b) => a.start > b.start ? 1 : -1)
console.log(sortedCompanies)

const sortAges = ages.sort((a, b) => a - b);
console.log(sortAges)

/*
    Reduce
*/

// get Age sum
const ageSum = ages.reduce((tot, age) => tot + age, 0)
console.log(ageSum)

// get Tot years of companies
const totYearsCompanies = companies.reduce((total, company) => total + (company.end - company.start), 0)
console.log(totYearsCompanies)

/*

    Combining Methods
    --------------------------
*/

const combined = ages
    .map(age => age * 2)
    .filter( age => age >= 40)
    .sort((a,b) => a - b)
    .reduce((a,b) => a + b, 0)

console.log(combined)