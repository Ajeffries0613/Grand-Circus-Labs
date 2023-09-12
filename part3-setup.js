// Run the following MongoDB shell command to create and populate the collection needed
// for the MongoDB questions on this assessment.

db.ticketsales.insertMany([
  { show: "Aretha Franklin", section: "Main Floor", sold: 200 },
  { show: "Aretha Franklin", section: "Balcony",    sold: 100 },
  { show: "The Temptations", section: "Main Floor", sold: 250 },
  { show: "The Temptations", section: "Balcony",    sold:  80 },
  { show: "The Supremes",    section: "Main Floor", sold: 250 },
  { show: "The Supremes",    section: "Balcony",    sold: 120 },
  { show: "The Supremes",    section: "Box Seats",  sold:   0 },
]);