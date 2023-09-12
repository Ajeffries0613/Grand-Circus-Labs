// Paste your answers for each question in the appropriate spot below. (Keep the number headings)


// #1 Using one MongoDB command, find all data for shows by The Supremes or The Temptations.

db.ticketsales.find({
    $or: [
        { show: "The Supremes"},
        { show: "The Temptations"}
    ]
});

// #2  Use projection to show only the number sold for Aretha Franklin on the Main Floor.

db.ticketsales.find(
    {show: "Aretha Franklin", section: "Main Floor"},
    { _id: 0, sold: 1}
);